### Autores: Yuri de Sousa Nascimento e Érick Santos Marçal
### Disciplina: Processamento de Imagens

import sys
import numpy as np
import cv2 as cv
from PIL import Image as pl
from matplotlib import pyplot as plt


def segmentation(img, threshold):
  binarized = img.copy()
  for i in range(width):
    for j in range(height):
      gray = img.getpixel((i, j))
      if (gray >= (threshold, threshold, threshold)):
        # objetos
        binarized.putpixel((i, j), (255, 255, 255))
      else:
        # fundo
        binarized.putpixel((i, j), (0, 0, 0))
  return binarized


def histogram(file, img):
    img = cv.imread(file)
    plt.hist(img.ravel(), 256, [0,256])
    plt.show()

# nome da imagem passada para o script na CLI
file_name = sys.argv[1]

# abre a imagem
img = pl.open(file_name)

# dimensões da imagem
width, height = img.size

# # transforma a imagem em níveis de cinza para matriz
# img2mat = np.asarray(img)

# # save image
# mat2img = pl.fromarray(img2mat)
# mat2img.save('gray-'+file_name)

# segmenta imagem
img_binary = segmentation(img, 140)

# salva imagem segmentada
img_binary.save(f'segmented_{file_name}')

# mostra o histograma da imagem original
histogram(f'segmented_{file_name}', img_binary)
