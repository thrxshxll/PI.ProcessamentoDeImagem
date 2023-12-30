import sys
import numpy as np
from PIL import Image

file_name = sys.argv[1]

img_colour = Image.open(file_name)
img_gray = img_colour.convert('L')   # L - use the ITU-R 601-2 luma transform to convert color to grayscale

width, weight = img_gray.size

img2arr = np.asarray(img_gray)

# apaga linhas
for l in range(1, int(weight/2)):
    img2arr = np.delete(img2arr, l, 0)

# apaga colunas
for c in range(1, int(width/2)):
    img2arr = np.delete(img2arr, c, 1)

arr2img = Image.fromarray(img2arr)
arr2img.save('reduced:'+str(img2arr.shape[0])+'x'+str(img2arr.shape[1])+':'+file_name)