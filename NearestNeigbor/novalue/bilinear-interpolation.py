import cv2 as cv
import sys

"""
usage:
    $ python scriptname.py imagename.png
"""

# shape[0] = rows = weight
# shape[1] = coluns = width

image_path = sys.argv[1] # caminho e o nome da imagem passada para o script

img = cv.imread(image_path)
cv.imshow('original:'+str(img.shape[1])+'x'+str(img.shape[0]), img)
cv.waitKey()


# Nova quantidade de linhas e colunas que a imagem terá após ser redimensionada.
# Os novos valores aumentam/diminuem em 50 porcentos.
#

expand_size = (int(img.shape[1] + img.shape[1] * 50/100), int(img.shape[0] + img.shape[0] * 50/100))
expanded_img = cv.resize(img, expand_size, interpolation = cv.INTER_LINEAR)

cv.imshow('expanded:'+str(expanded_img.shape[1])+'x'+str(expanded_img.shape[0]), expanded_img)
cv.waitKey()


reduce_size = (int(img.shape[1] - img.shape[1] * 50/100), int(img.shape[0] - img.shape[0] * 50/100))
reduced_img = cv.resize(img, reduce_size, interpolation = cv.INTER_LINEAR)

cv.imshow('reduced:'+str(reduced_img.shape[1])+'x'+str(reduced_img.shape[0]), reduced_img)
cv.waitKey()


cv.destroyAllWindows()