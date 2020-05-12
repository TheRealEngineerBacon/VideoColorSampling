#! usr/bin/env python3
from skimage import io
import numpy as np
import statistics as stat


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






    
    
    
    
    
    
    
    
    
    
    
    