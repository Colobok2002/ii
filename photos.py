import random
from PIL import Image, ImageDraw , ImageOps ,ImageEnhance #Подключим необходимые библиотеки.
# import matplotlib

filename = "main.jpg"

type = 'monoh' # Цвестна картинка или нет

myimage = Image.open(filename)


### Filters ###

# myimage = myimage.resize((myimage.size[0]-500, myimage.size[1]-500))

# myimage = myimage.rotate(90)

# enhancer = ImageEnhance.Brightness(myimage)

# factor = 0.5 

# myimage = enhancer.enhance(factor)


myimage.show()

pix = myimage.load()
width = myimage.size[0]  # Определяем ширину
height = myimage.size[1]  # Определяем высоту
mat_pix = []

for y in range(height):
    kesh = []
    for x in range(width):
        pixel = []
        if type == 'monoh':
            pixel.append(pix[x, y][0])
        else:
            pixel.append(pix[y, x][0]) #узнаём значение красного цвета пикселя
            pixel.append(pix[y, x][1]) #зелёного
            pixel.append(pix[y, x][2]) #синего
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

# a = np.rot90(np.array(svertka),k=3)

# img_new =ImageOps.mirror(Image.fromarray(a))

a = np.array(svertka)
img_new = Image.fromarray(a)
img_new.show()

pylling = []

for i in range(0, len(svertka)-1,2):
    kesh = []
    for j in range(0, len(svertka[i])-1,2):
        kesh.append(max(svertka[i][j],svertka[i+1][j],svertka[i][j+1],svertka[i+1][j+1]))
    pylling.append(kesh)



a = np.array(pylling)
img_new = Image.fromarray(a)
img_new.show()

