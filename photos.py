import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.
import matplotlib

filename = "main.jpg"

type = 'monoh' # Цвестна картинка или нет

myimage = Image.open(filename)

pix = myimage.load()
width = myimage.size[0]  # Определяем ширину
height = myimage.size[1]  # Определяем высоту
mat_pix = []


for x in range(width):
    kesh = []
    for y in range(height):
        pixel = []
        if type == 'monoh':
            pixel.append(pix[x, y][0])
        else:
            pixel.append(pix[x, y][0]) #узнаём значение красного цвета пикселя
            pixel.append(pix[x, y][1]) #зелёного
            pixel.append(pix[x, y][2]) #синего
        kesh.append(pixel)

    mat_pix.append(kesh)

hengh_max = len(mat_pix) - 1
width_max = len(mat_pix[0]) - 1



svertka = []


for hengh in range(hengh_max):
    kesh = []
    for width in range(width_max):

        sum = 0
        for i in range(3):
            try:
                sum += mat_pix[hengh][width+i][0]
            except:
                None
            try:
                sum += mat_pix[hengh+1][width+i][0]
            except:
                None
            try:
                sum -= mat_pix[hengh + 2][width+i][0]
            except:
                None
            try:
                sum -= mat_pix[hengh + 3][width+i][0]
            except:
                None
        if sum <= 0:
            kesh.append(0)
        else:
            kesh.append(sum)

    svertka.append(kesh)


import numpy as np

a = np.array(svertka)

img_new =Image.fromarray(a)

img_new.show()

