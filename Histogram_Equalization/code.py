import sys
import numpy as np
import cv2 as cv
from PIL import Image as pl
from matplotlib import pyplot as plt

def histogram(file, img):
    img = cv.imread(file)
    plt.hist(img.ravel(), 256, [0,256])
    plt.show()


# nome da imagem passada para o script na CLI
file_name = sys.argv[1]

# abre a imagem
img_color = pl.open(file_name)

# transforma a imagem para níveis de cinza
img_gray = img_color.convert('L')

# dimensões da imagem
width, height = img_gray.size

# transforma a imagem em níveis de cinza para matriz
img2mat = np.asarray(img_gray)

# quantidade total de pixels
mn = height*width


# cria um array de 256 elementos inicializados com zeros
eq = np.zeros(256)

# (nível de cinza) * (quantidade de pixel com nível de cinza zero) / quantidade total de pixel
eq[0] = (255 * np.count_nonzero(img2mat == 0) / mn)
for i in range(1, 256):
    # (nível de cinza) * (quantidade de pixel com nível de cinza [1-255]) / quantidade total de pixel + equalização anterior(somatório)
    eq[i] = (255 * np.count_nonzero(img2mat == i) / mn) + eq[i-1]


# cópia da matrix imagem em escala de cinza
eqImg = img2mat.copy()

# percorre todos os pixels e, com base na sua antiga escala de cinza, atribui as novas escalas(Sk)
for i in range(height):
    for j in range(width):
        eqImg[i, j] = int( eq[ img2mat[i,j] ] )


# save image
mat2img = pl.fromarray(img2mat)
mat2img.save('gray-'+file_name)

# save image
mat2img = pl.fromarray(eqImg)
mat2img.save('eq-'+file_name)

# mostra o histograma da imagem original
histogram('gray-'+file_name, img2mat)
# mostra o histograma da imagem equalizada
histogram('eq-'+file_name, eqImg)