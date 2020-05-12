#! usr/bin/env python3
from skimage import io
import numpy as np
import statistics as stat


def contrast(x, t): #Using logistic function due to it's variability.
    #Function variables, adjust for variable contrast adjustment.
    #Variables are adjusted so that the function over (0<=x<=255) only gives output values of (0<=y<=255). 
    L, f, a, k, b = 255, 9.9, 127, 0.031, 5.02
    
    #This function increases the overall contrast of the image after Stage 0.
    #This must be done to reach an accurate portrayal of the frame's color.
    contrast = t * (((L + f) / (1 + (2.71828 ** ((-1 * k) * (x - a))))) - b) + (1 - t) * x
    return contrast


def brightness(b, t):
    #This function increases brightness to match frame's color more accurately.
    brightness = t * (255 * np.sin((np.pi/510)*b)) + (1-t) * b
    return brightness

a = int(input("What part of the script would you like to run? (0)Stills Processing, (1)Brightness/Contrast, or (2)Vertical Blurring "))

if a == 0:
    #image numbering
    start_number = int(input("Starting number of image sequence to be computed. "))
    
    end_number = int(input("End number of image sequence. Sequence will include this image. "))
    
    #Determine image dimensions
    test_image_path = f'C:/Program Files/Docker Toolbox/workDir/coosimages/source{start_number}.png'
    test_image = io.imread(test_image_path)
    h_pixels = int(len(test_image[:, 0, 0]))
    w_pixels = int(len(test_image[0, :, 0]))
    
    print(h_pixels)
    print(w_pixels)
    
    #Create image array. Automatically opens images as 8-bit RBG.
    final_image = np.ndarray((w_pixels, end_number - start_number + 1, 3), dtype='uint8')
    final_image.fill(0)
    
    #Cycle is needed in case the user wants to start in the middle of the source image sequence.
    cycle = 0
    for images in range(start_number, end_number + 1):
        working_image = io.imread(f'C:/Program Files/Docker Toolbox/workDir/coosimages/source{images}.png')
        for column in range(0, w_pixels):
            for color in range(0, 3):
                #Averages columns into pixels, then applies pixels to the relevant locations in the final_image array.
                final_image[column, cycle, color] = stat.mean(working_image[:, column, color])
        #Used to keep track of progress.
        print(images)
    
        cycle += 1
        
    io.imsave(f'C:/Program Files/Docker Toolbox/workDir/coosimages/save{start_number, end_number}.png', final_image)
    
if a == 1:
    #Used if brightness and constrast is needed. This operates on a post-Step1 image.
    image_name = input("What is the sequence image name without extension?")
    image_to_edit = io.imread(f'C:/Program Files/Docker Toolbox/workDir/coosimages/{image_name}.png')
    
    #Determine image dimensions, Image sequence should start with 0 or 1.
    h_pixels = int(len(image_to_edit[:, 0, 0]))
    w_pixels = int(len(image_to_edit[0, :, 0]))
    
    print(h_pixels)
    print(w_pixels)
    
    final_bc = np.ndarray((h_pixels, w_pixels, 3), dtype='uint8')
    final_bc.fill(0)
    
    for color in range(0, 3):
        for column in range(0, w_pixels):
            for row in range(0, h_pixels):
                #Apply contrast and brightness functions, the second variable in the functions varies the intensity of the effect.
                #0 = no effect, 1 = 100% effect
                step_1 = contrast(image_to_edit[row, column, color], 0) 
                step_2 = brightness(step_1, 0)
                final_bc[row, column, color] = int(step_2)
                print(color, column, row, image_to_edit[row, column, color], final_bc[row, column, color])
    io.imsave(f'C:/Program Files/Docker Toolbox/workDir/coosimages/{image_name}_bc.png', final_bc)
    
if a == 2:
    image_name = input("What is the sequence image name? (without extension extension) ")
    image_to_edit = io.imread(f'C:/Program Files/Docker Toolbox/workDir/coosimages/{image_name}.png')
    
    #Determine image dimensions, Image sequence should start with 0 or 1.
    h_pixels = int(len(image_to_edit[:, 0, 0]))
    w_pixels = int(len(image_to_edit[0, :, 0]))
    
    print(h_pixels)
    print(w_pixels)
    
    final_blur = np.ndarray((h_pixels, w_pixels, 3), dtype='uint8')
    final_blur.fill(0)
    
    blur_distance = 50
    
    for color in range(0, 3):
        for column in range(0, w_pixels):
            for row in range(0, h_pixels):
                if row < blur_distance:
                    low_limit = row + blur_distance
                    comp = [x**2 for x in image_to_edit[0:low_limit, column, color]]
                    blur_value = np.sqrt(stat.mean(comp))
                    
                    final_blur[row, column, color] = blur_value
                
                
                elif row >= blur_distance and row <= (h_pixels - blur_distance):
                    low_limit = row + blur_distance
                    high_limit = row - blur_distance
                    comp = [x**2 for x in image_to_edit[high_limit:low_limit, column, color]]
                    blur_value = np.sqrt(stat.mean(comp))
                    
                    final_blur[row, column, color] = blur_value
                
                
                elif row > (h_pixels - blur_distance):
                    high_limit = row - blur_distance
                    comp = [x**2 for x in image_to_edit[high_limit:h_pixels, column, color]]
                    blur_value = np.sqrt(stat.mean(comp))
                    
                    final_blur[row, column, color] = blur_value
                    
                print(color, column, row)
    io.imsave(f'C:/Program Files/Docker Toolbox/workDir/coosimages/{image_name}_blur.png', final_blur)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    