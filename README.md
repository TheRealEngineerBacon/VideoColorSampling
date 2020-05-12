# VideoColorSampling
Samples the colors of video frames then builds a representative image of each frame.

This program assumes png image files, though assumed file extensions can be easily changed in the code.

This program has three phases. First, an image sequence is averaged vertically and each frame's values are used to construct an image showing the color variation throughout the video. The image sequence can be easily created in Unix with ffmpeg. I found success with using both jpegs and pngs, though the quality of jpegs will need to be tailored when using ffmpeg. This script can then be used to conduct the initial image creation, any brightness or contrasting, and the final blurring step. The blurring step is necessary as it removes hard structure and creates a more artistic representation. Care should be taken to not use large numbers of source frames as computational time becomes significant with large images.
