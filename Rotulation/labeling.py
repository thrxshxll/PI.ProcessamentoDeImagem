import sys
import cv2 as cv
import random
from PIL import Image

def img2binary(img, threshold):
    binarized = img
    for i in range(width):
        for j in range(height):
            R, G, B = img.getpixel((i, j))
            if ( (R + G + B) / 3 <= threshold):
                # regions
                binarized.putpixel((i, j), (0, 0, 0))
            else:
                # backgrond
                binarized.putpixel((i, j), (255, 255, 255))
    return binarized



image_file_name = sys.argv[1]
original_image = Image.open(image_file_name)
width, height = original_image.size
print('------- Original dimensions of image:')
print("------> Height: ", height)
print("------> Width: ", width)


#Transforma a imagem original em uma imagem binária
binarized_image = img2binary(original_image, 200)

# save binarized image
binarized_image.save(f'binary-{image_file_name}')

img = cv.imread('binary-'+image_file_name)
cv.imshow('binarized image', img)
cv.waitKey()
cv.destroyAllWindows()

# copied matrix to apply labeling
labeling = binarized_image
case1 = 0
case2 = 0
case3 = 0
case4 = 0

# labeling process
for i in range(1, width):
    for j in range(1, height):
        s = binarized_image.getpixel((i - 1, j))
        r = binarized_image.getpixel((i, j - 1))
        p = binarized_image.getpixel((i, j))

        # p are black, regions
        if p != (255, 255, 255):

            # case 4
            # label collision, store the label pair as being equivalent
            if (s != (255, 255, 255) and r != (255, 255, 255)) and (labeling.getpixel((i - 1, j)) != labeling.getpixel((i, j - 1))):
                case4 += 1
                labeling.putpixel( (i, j), labeling.getpixel((i, j - 1)) )
                labeling.putpixel( (i-1, j), labeling.getpixel((i, j - 1)) )

            # case 3
            # s and r are black in binarized, s and r had equals labels in labeling
            elif (s != (255, 255, 255) and r != (255, 255, 255)) and (labeling.getpixel((i - 1, j)) == labeling.getpixel((i, j - 1))):
                case3 += 1
                labeling.putpixel( (i, j), labeling.getpixel((i, j - 1)) )

            # case 2
            # s or r are black, assing label of pixel tha has black pixel
            elif s != (255, 255, 255) or r != (255, 255, 255):
                case2 += 1
                if s != (255, 255, 255):
                    labeling.putpixel((i, j), labeling.getpixel((i - 1, j)))
                elif r != (255, 255, 255):
                    labeling.putpixel((i, j), labeling.getpixel((i, j - 1)))

            # case 1
            # s and r are white, assing new label
            elif s != (0, 0, 0) and r != (0, 0, 0):
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)

                labeling.putpixel((i, j), (r, g-50, b))
                case1 += 1

# save labeled image
labeling.save('labeled-'+image_file_name)
print('case1:', case1)
print('case2:', case2)
print('case3:', case3)
print('case4:', case4)

# using opencv to open image
img = cv.imread('labeled-'+image_file_name)
cv.imshow('labeled image', img)
cv.waitKey()
cv.destroyAllWindows()


