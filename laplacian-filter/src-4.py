# Autores:
    # Yuri Nascimento
    # Erick Santos

import sys
import numpy as np
from PIL import Image as pl

# nome da imagem original
file_name = sys.argv[1];

# para abri a imagem
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

for i in range(1, height-1):
    for j in range(1, width-1):

        # laplaciano[i, j] = img2mat[i-1, j] + img2mat[i+1, j] + img2mat[i, j-1] + img2mat[i, j+1] - (4 * img2mat[i, j]) [ error ]

        '''
            Máscara que inclui os termos diagonais. Com o centro da máscara igual a +1.
        '''
        hold = 0
        hold -= img2mat[i-1, j]
        hold -= img2mat[i+1, j]
        hold -= img2mat[i, j-1]
        hold -= img2mat[i, j+1]

        hold -= img2mat[i-1, j-1]
        hold -= img2mat[i+1, j+1]
        hold -= img2mat[i-1, j+1]
        hold -= img2mat[i+1, j-1]
        hold += (8 * img2mat[i, j]) # valor lapaciano do pixel f(x,y)

        if hold < 0:
            final[i, j] = 0
        else:
            final[i, j] = hold # resultado final no pixel (x, y) da imagem
            

mat2img = pl.fromarray(final)
mat2img.save('laplaciano+8'+file_name)