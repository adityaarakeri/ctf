from PIL import Image, ImageOps
import numpy as np


INPUT_FILE = 'input.jpg'
OUTPUT_FILE = 'output.jpg'

# read the image
input_image = Image.open('input.jpg', 'r')
print(f"Input file: {INPUT_FILE}")

# convert it into a numpy array for easier processing
np_array = np.array(input_image, dtype=np.uint8)

# since the pixels are arrange in a sequence 
# count the entire set of pixels
print(f"Number of Pixels: {len(np_array[0])}")

# extract the pixel array from np array
input_array = np_array[0]

# why 92?
# image width =  304
# number of pixels = 27968
# image height = 27968/304 i.e 92
# the input_array is a 1D array since the pixels are arranged in line 
# converting the input_array into a 2D array
two_dimensional_array = [input_array[i:i+92] for i in range(0, len(input_array), 92)]

# length of 2D array should be 304 which is the actual width of image
print(f"Length of 2D array (image width): {len(two_dimensional_array)}")

# convert the 2D array to np array for processing
np_array = np.array(two_dimensional_array, dtype=np.uint8)

# First level processing of the complete image
complete_image = Image.fromarray(np_array)

# image needs to be flipped(mirrored)
flip_image = ImageOps.mirror(complete_image)

# rotate the image 90
output_image = flip_image.transpose(Image.ROTATE_90)
output_image.save(OUTPUT_FILE)
print(f"Output file: {OUTPUT_FILE}")

