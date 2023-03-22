from random import randint as ri
from main import read
from config import *
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from time import sleep
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

base = read(target_file_name)
data = dict()
data[0], data[1] = [], []

arrau_last_litel_table = []
arrau_litel_table = []
arrau_last_table = []
arrau_table = []
Shetsilk = 1

for target in base:
    #if ri(1, 3) in [2, 3]:
    if Shetsilk == 1 or Shetsilk == 2:
        data[1].append(target)
        arrau_last_table.append(target[-1])
        arrau_table.append(target[:-1])
        Shetsilk += 1

    else:
        data[0].append(target)
        arrau_last_litel_table.append(target[-1])
        arrau_litel_table.append(target[:-1])
        Shetsilk = 1
print(len(arrau_last_table))
arr = []

for i in range(0, len(arrau_last_table)-2, 2):
    arr.append([arrau_last_table[i], arrau_last_table[i+1]])
print(len(arr))
arr_test = [[0, 0], [1, 1], [0, 1]]
arr_test2 = [0, 1]
# arry = []
# for sim in arrau_litel_table:
#     for sib in sim:
#         try:
#             if sib == '$':
#                 arry.append(ord(sib))
#             elif sib == '!':
#                 arry.append(ord(sib))
#             else:
#                 arry.append((sib))
#         except:
#             continue
#
# for sim in arrau_table:
#     for sib in sim:
#         try:
#             if sib == '$':
#                 sib = ord(sib)
#                 sim[7] = sib
#             elif sib == '!':
#                 sib = ord(sib)
#                 sim[7] = sib
#             else:
#                 continue
#         except:
#             continue

ed = 0
nuli = 0
clf = tree.DecisionTreeClassifier()
big_table = clf.fit(arr, arrau_last_litel_table)
y = clf.predict(arr)
#litl_table = clf.predict(arrau_litel_table, arrau_last_litel_table)
print(y)
for el in y:
    if el == 1:
        ed += 1
    else:
        nuli += 1
print(ed / nuli)
tree.plot_tree(clf)

print(ed/len(y))

