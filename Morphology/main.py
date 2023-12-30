import sys
from PIL import Image as Img
import numpy as np


def img2binary(img, threshold):
    binarized = img
    for i in range(height):
        for j in range(width):
            R, G, B = img.getpixel((i, j))
            if ( (R + G + B) / 3 <= threshold):
                # black
                binarized.putpixel((i, j), (0, 0, 0))
            else:
                # white
                binarized.putpixel((i, j), (255, 255, 255))

    return binarized


def erosion(img):
    final = img.copy()

    for i in range(1, height-1):
        for j in range(1, width-1):
            # Elemento Estruturante
            # [0 1 0]
            # [1 1 1]
            # [0 1 0]

            if (img.getpixel((i-1,j)) != (255, 255, 255)) or (img.getpixel((i,j-1)) != (255, 255, 255)) or (img.getpixel((i,j)) != (255, 255, 255)) or (img.getpixel((i,j+1)) != (255, 255, 255)) or (img.getpixel((i+1,j)) != (255, 255, 255)):
                final.putpixel((i-1, j), (0, 0, 0))
                final.putpixel((i, j-1), (0, 0, 0))
                final.putpixel((i, j), (0, 0, 0))
                final.putpixel((i, j+1), (0, 0, 0))
                final.putpixel((i+1, j), (0, 0, 0))

    return final


# nome da imagem original
file_name = sys.argv[1]

# abre a imagem
img_color = Img.open(file_name)

#  dimensões imagem
width, height = img_color.size

# binariza imagem em cor
img_binary = img2binary(img_color, 128)

# salva imagem binária
img_binary.save(f'binary+{file_name}')

# converte imagem para matrix de pixels
# img2mat = np.asarray(img_binary)

# image erosion
img_erosion = erosion(img_binary)

# salva imagems
# mat2img = Img.fromarray(img_erosion)
img_erosion.save(f'erosion+{file_name}')
