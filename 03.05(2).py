from random import random


def getData():
    Nn = 100
    Ni = 10
    re = 0.7
    Di = 1
    Wi = 0.2
    Ne = Ni * re
    Ne = int(Ne)


    wpp, wmm = 0.9, 0.6
    wpm, wmp = -0.2, -0.2

    dpp,  dmm, dpm, dmp = 1, 1, 1 , 3

    rpp, rmm = 1, 0.3
    rpm, rmp = 0.3, 0

    inp = [[True for i in range(Nn)] if j == 0 else [False for i in range(Nn)] for j in range(Ni)]

    return Nn, Ni, inp, Wi, wpp, wpm, wmp, wmm, Di, dpp, dpm, dmp, dmm, re, rpp, rpm, rmp, rmm, Ne


def getMatrixW(Nn, Ni, Wi, Ne, rpp, wpp, wpm, wmp, wmm, rmm, rpm, rmp):
    matrixW = [[0 for j in range(Nn + Ni)] for i in range(Nn)]


    for i in range(len(matrixW)):
        for j in range(Ni):
            if (random() < rpp):
                matrixW[i][j] = Wi

    for i in range(Ne):
        for j in range(Ni, Ni + Ne):
            if (random() < rpp):
                matrixW[i][j] = wpp

    for i in range(Ne, Nn):
        for j in range(Ni, Ni + Ne):
            if (random() < rpm):
                matrixW[i][j] = wpm

    for i in range(Ne):
        for j in range(Ni + Ne, Ni + Nn):
            if (random() < rmp):
                matrixW[i][j] = wmp

    for i in range(Ne, Nn):
        for j in range(Ni + Ne, Nn):
            if (random() < rmm):
                matrixW[i][j] = wmm

    return matrixW


def getMatrixD(Nn, Ni, Di,Ne, rpp, dpp, dpm, dmp, dmm):
    matrixD = [[1 for j in range(Nn + Ni)] for i in range(Nn)]

    for i in range(len(matrixD)):
        for j in range(Ni):
            matrixD[i][j] = Di

    for i in range(Ne):
        for j in range(Ni, Ni + Ne):
            matrixD[i][j] = dpp

    for i in range(Ne, Nn):
        for j in range(Ni, Ni + Ne):
            matrixD[i][j] = dpm

    for i in range(Ne):
        for j in range(Ni + Ne, Ni + Nn):
            matrixD[i][j] = dmp

    for i in range(Ne, Nn):
        for j in range(Ni + Ne, Nn):
            matrixD[i][j] = dmm

    return matrixD



def network(inp, w, d):
    import matplotlib.pyplot as plt
    import numpy as np 

    out = []
    u = [0  for i in range(len(w))]
    # tau = 10 
    # arr = []
    
    for i in range(len(inp)):
        out.append([])
        for j in range(len(w)): 
            for k in range(len(w[0])):
                # if i == 2:
                    # print(inp[i])

                if k < len(inp[0]):
                    delay = d[j][k]
                
                    if i >= delay:
                        is_spike = inp[i - delay][k] 
                        if is_spike:
                            # arr.append(is_spike)
                            u[j] = u[j] + w[j][k]
                else:
                    delay = d[j][k]

                    if i >= delay:
                        is_spike = out[i - delay][k - len(inp[0])] 
                        if is_spike:        
                            u[j] = u[j] + w[j][k]
                            # arr.append(is_spike)
                # print(w[j][k])
            if u[j] > 1:
                out[-1].append(True) 
                u[j] = 0
            else: 
                out[-1].append(False) 
    return out


def draw(data):
    import matplotlib.pyplot as plt
    import numpy as np 

    # plot heatmap
    plt.plot(data)

    # show plot
    plt.show()  



def main():
    Nn, Ni,inp, Wi, wpp, wpm, wmp, wmm, Di, dpp, dpm, dmp, dmm, re, rpp, rpm, rmp, rmm, Ne = getData()
    matrixW = getMatrixW(Nn, Ni, Wi,Ne, rpp, wpp, wpm, wmp, wmm, rpm, rmp, rmm)
    matrixD = getMatrixD(Nn, Ni, Di,Ne, rpp, dpp, dpm, dmp, dmm)
    out = network(inp, matrixW, matrixD)
    print(out[0])
    finalOut = [sum(i) for i in out]
    draw(finalOut)


if __name__ == "__main__":
    main()