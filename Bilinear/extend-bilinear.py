
import numpy as np
from PIL import Image

# name da imagem passado para o programa
file_name = sys.argv[1]

img_colour = Image.open(file_name)
img_gray = img_colour.convert('L')   # L - use the ITU-R 601-2 luma transform to convert color to grayscale

# pega as dimensões da imagem
width, height = img_gray.size

# transforma a imagem para matriz
img2arr = np.asarray(img_gray)

# matriz extendida para armazenar a imagem extendida
extanded = np.resize(img_gray, (height*2, width*2))

# copia os pixels da foto original para a matriz extendida, sem colocar pixel nos elementos (i, j+1), (i+1), (i+1, j+1)
for l in range(0, height-1):
    for c in range(0, width-1):
        extanded[l*2, c*2] = img2arr[l,c]


# para cada pixel (i, j), aplicada a regra de interpolação bilinear nos elementos
# (i, j+1), (i+1, j), (i+1, j+1), (i+1, j+2), (i+2, j+1)
for l in range(0, height*2-1, 2):
    for c in range(0, width*2-1, 2):
        x = 0
        x += extanded[l, c]
        x += extanded[l, c+1]
        extanded[l,c+1] = (x/2)     # a

        x = 0
        x += extanded[l, c]
        x += extanded[l+1, c]
        extanded[l+1,c] = (x/2)     # b

        x = 0
        x += extanded[l, c]
        x += extanded[l, c+1]
        x += extanded[l+1, c]
        x += extanded[+1, c+1]
        extanded[l+1,c+1] = (x/4)   # c

        x = 0
        x += extanded[l, c+1]
        x += extanded[l+1, c+1]
        if c+2 <= width*2-1:
            extanded[l+1,c+2] = (x/2)   # d

        x = 0
        x += extanded[l+1, c]
        x += extanded[l+1, c+1]
        if l+2 <= height*2-1:
            extanded[l+2,c+1] = (x/2)     # e


arr2img = Image.fromarray(extanded)
arr2img.save('extanded:'+str(extanded.shape[0])+'x'+str(extanded.shape[1])+':'+file_name)