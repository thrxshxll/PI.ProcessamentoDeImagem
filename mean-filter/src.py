# Autores:
#   Yuri Nascimento
#   Erick Santos

import sys
import numpy as np
from PIL import Image as pl

# nome da imagem original
file_name = sys.argv[1];

# abri a imagem
img_color = pl.open(file_name)

# converte imagem colorida, para escala de cinza
img_gray = img_color.convert('L')

#  dimensões imagem
width, height = img_gray.size

# imagem para matriz
img2mat = np.asarray(img_gray)

# Salva imagem em escala de cinza
mat2img = pl.fromarray(img2mat)
mat2img.save('gray-'+file_name)

# matriz onde ficará o resultado do processo 
final = img2mat.copy()

for i in range(1, height-1) :
    for j in range(1, width-1):

        '''
            Máscara de divisão onde os coeficientes são 1s e e divido pela soma dos valores
            de seus coeficientes.
        '''

        # final[i, j] = int(( img2mat[i-1, j-1] + img2mat[i-1, j] + img2mat[i-1, j+1] + img2mat[i, j-1] +img2mat[i, j] + img2mat[i, j+1] + img2mat[i+1, j-1] + img2mat[i+1, j] + img2mat[i+1, j+1] ) / 9)
        temp = 0
        temp += img2mat[i-1, j-1]
        temp += img2mat[i-1, j]
        temp += img2mat[i-1, j+1]
        temp += img2mat[i, j-1]
        temp += img2mat[i, j]
        temp += img2mat[i, j+1]
        temp += img2mat[i+1, j-1]
        temp += img2mat[i+1, j]
        temp += img2mat[i+1, j+1]
        final[i,j] = int( temp/9 )

mat2img = pl.fromarray(final)
mat2img.save('mean-filter'+file_name)