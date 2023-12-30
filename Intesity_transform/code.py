import sys
import cv2 as cv
import numpy as np
from PIL import Image as Img

# file name passed from CLI
file_name = sys.argv[1]

# open image file
img = Img.open(file_name)

# image dimensions
width, height = img.size

# convert color image to gray scale
img_gray = img.convert('L')

# convert image to numpy matrix
img2mat = np.asarray(img_gray)

# salva imagem preto e branco
mat2img = Img.fromarray(img2mat)
mat2img.save('BW-'+file_name)

# create an empty matrix with same dimensions from img
final = img2mat.copy()

for i in range(height):
    for j in range(width):
        # Negativo de imagem
        final[i,j] = int( 256 - 1 - img2mat[i,j] )


mat2img = Img.fromarray(final)
mat2img.save('negativo-'+file_name)