from PIL import Image
import numpy as np
import sys

file_name = sys.argv[1]

img_colour = Image.open(file_name)
img_gray = img_colour.convert('L')

# pega as dimensões da imagem original
width, height = img_gray.size

# transforma a imagem para matriz
img2arr = np.asarray(img_gray)

# reduce matrix
reduced = np.resize(img_gray, (int(height/2), int(width/2)))

# aplica a regra de interpolação bilinear na matriz com dimensões normais e o resultado da
# interpolação é atribuído à matriz reduzida
for l in range(0, height-1, 2):
    for c in range(0, width-1, 2):
        summ = 0
        summ += img2arr[l,c]
        summ += img2arr[l,c+1]
        summ += img2arr[l+1,c]
        summ += img2arr[l+1,c+1]
        reduced[int(l/2), int(c/2)] = (summ / 4)


file_name = file_name.split('.')
extenstion = file_name.pop()
filename = file_name.pop()

arr2img = Image.fromarray(reduced)
arr2img.save(filename+':reduced.'+extenstion)