### Autores: Yuri de Sousa Nascimento e Érick Santos Marçal
### Disciplina: Processamento de Imagens

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

# save image
mat2img = pl.fromarray(img2mat)
mat2img.save('gray_'+file_name)

# mostra o histograma da imagem original
histogram('gray_'+file_name, img2mat)