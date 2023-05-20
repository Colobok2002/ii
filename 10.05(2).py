import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook
import numpy as np



def getImageMatrix():
    img_url = "C:\\Users\\ralek\\OneDrive\\Рабочий стол\\ii-fork\\assets\\images\\1602584754_1.jpg"

    with cbook.get_sample_data(img_url) as image_file:
        imageMatrix = plt.imread(image_file)
    # fig, ax = plt.subplots()
    # im = ax.imshow(imageMatrix)
    # ax.axis('off')
    # plt.show()

    return imageMatrix



def main():
    imageMatrix = getImageMatrix()

    initial_x = 448
    initial_y = 404

    arr_1 = np.zeros((initial_x, initial_y))

    # svertka = [[1 if i == 1 or i == 2 else -1 for j in range(4)] for i in range(4)]

    # out = []

    for i in range (initial_x):
        for j in range(initial_y):
            arr_1[i][j] = imageMatrix[i][j][1]

    counter = 0


    # for i in range(0, len(arr_1) - len(svertka), 2):
    #     out.append([])
    #     for j in range(0, len(arr_1[i]) - len(svertka[0]), 2):
    #         summ = 0
    #         for ii in range(len(svertka)):
    #             for jj in range(len(svertka[ii])):
                    
    #                 c = svertka[ii][jj] * arr_1[i + ii][j + jj]
    #                 summ += c
    #                 # if c < 0:
    #                 #     c = 0
    #         if summ < 0:
    #             summ = 0
    #         out[counter].append(summ)

    #     counter += 1

    # # 20.05

    # out_sloi_2 = []
    # counter = 0
    # for i in range(0, len(out) - len(svertka), 2):
    #     out_sloi_2.append([])
    #     for j in range(0, len(out[i]) - len(svertka), 2):
    #         # try:
    #             summ = max([out[i + 1][j + 1], out[i - 1][j - 1], out[i + 1][j - 1] , out[i - 1][j + 1]])
    #             out_sloi_2[counter].append(summ)

    #         # except: 
    #         #     continue
    #     counter += 1

    

    def func(out, arr_1, svertka):
        counter = 0
        for i in range(0, len(arr_1) - len(svertka), 2):
            out.append([])
            for j in range(0, len(arr_1[i]) - len(svertka[0]), 2):
                summ = 0
                for ii in range(len(svertka)):
                    for jj in range(len(svertka[ii])):
                        
                        c = svertka[ii][jj] * arr_1[i + ii][j + jj]
                        summ += c
                        # if c < 0:
                        #     c = 0
                if summ < 0:
                    summ = 0
                out[counter].append(summ)

            counter += 1

        # 20.05

        out_sloi_2 = []
        counter = 0
        for i in range(0, len(out) - len(svertka), 2):
            out_sloi_2.append([])
            for j in range(0, len(out[i]) - len(svertka), 2):
                try:
                    summ = max([out[i + 1][j + 1], out[i - 1][j - 1], out[i + 1][j - 1] , out[i - 1][j + 1]])
                    out_sloi_2[counter].append(summ)

                except: 
                    continue
            counter += 1

        return out

    svertka_1 = [[-1, -1, 1, 1],
                [-1, -1, 1, 1],
                [-1, -1, 1, 1],
                [-1, -1, 1, 1]]
    svertka_2 = [[-1, -1, -1, -1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [-1, -1, -1, -1]]
    svertka_3 = [[0, -1, -1, 0],
                [-1, 1, 1, -1],
                [-1, 1, 1, -1],
                [0, -1, -1, 0]]
    
    out_R = []
    out_RR = []
    out_G = []
    out_B = []

    out_R = func(out_R, arr_1, svertka_1)
    out_RR = func(out_RR, out_R ,svertka_2)
    out_G = func(out_G,arr_1, svertka_2)
    out_B = func(out_B,arr_1, svertka_3)


    final_out = []

    for i in range(len(out_R)):
        final_out.append([])
        for j in range(len(out_R[i])):
            final_out[i].append([out_R[i][j], out_G[i][j], out_B[i][j]])


    fig, ax = plt.subplots()
    im = ax.imshow(out_RR)
    ax.axis('off')
    plt.show()
    
    

    # # print(out)
    # fig, ax = plt.subplots()
    # im = ax.imshow(out)
    # ax.axis('off')
    # plt.show()

    # fig, ax = plt.subplots()
    # im = ax.imshow(out_sloi_2)
    # ax.axis('off')
    # plt.show()
    


if __name__=="__main__":
    main()