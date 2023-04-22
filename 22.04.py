from random import random
import math


# f_end = 0.5
# f_start = 0
# f_step = 0.01
# f = int((f_end - f_start) / f_step) + 1 
f = 0.1
a_start = 0
a_end = 0.1
a_step = 0.0001
a = int((a_end - a_start) // a_step)


# fStartInt = int(f_start / f_step)
# fEndInt = int(f_end / f_step)
# for i in range(fStartInt, fEndInt):
#     print(i * f_step)

w = 0.2 
tau = 10 

u = 0
out = []


for j in range(a):
    # print(j)
    out.append([])
    s = [[random() < f + a_start * math.sin(jj / 100) for jj in range(10)] for ii in range(10000)]
    # print(s[0])
    # print(sum(s[0]))

    for i in range(len(s)):
        new_u = u * (1 - 1/tau) + w * sum(s[i])
        if new_u > 1:
            new_u = True
        else:
            new_u = False

        out[j].append(new_u)   

    # f_start += f_step
    a_start += a_step
# print(out) 
# print(len(out)) 

res = []

for elem in out:
    # print(sum(elem))
    res.append(sum(elem))

def draw(data):
    import matplotlib.pyplot as plt
    import numpy as np 

    # convert Boolean values to integers
    data = np.array(data, dtype=int)

    # plot heatmap
    plt.plot(data)

    # show plot
    plt.show()   

draw(res)