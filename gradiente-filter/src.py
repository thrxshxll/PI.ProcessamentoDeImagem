# Yuri
# Gradiente de Sobel

import sys
import numpy as np
from PIL import Image as pl

def gradient_filter(file_name):

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

    for i in range(1, height-1):
        for j in range(1, width-1):

            '''
                Uso dos operadores de Sobel para fazer a diferença entre a terceira ea primeira linha da máscara,
                na direção x; e a diferença entre a terceira e a primeira coluna, na direção y.
            '''
            hold = 0
            hold += (img2mat[i+1,j-1] + 2*img2mat[i+1,j] + img2mat[i+1,j+1]) + (-1*img2mat[i-1,j-1] -2*img2mat[i-1,j] -1*img2mat[i-1,j+1])
            hold += (img2mat[i-1,j+1] + 2*img2mat[i,j+1] + img2mat[i+1,j+1]) + (-1*img2mat[i-1,j-1] -2*img2mat[i,j-1] -1*img2mat[i+1,j-1])
            if hold < 0:
                final[i,j] = 0
            else:
                final[i,j] = hold


    mat2img = pl.fromarray(final)
    mat2img.save('gradiente-'+file_name)



if __name__ == "__main__":
    if sys.argv[1:]:
        gradient_filter(sys.argv[1])
    else:
        print('Passe a imagem como argumento para o script')