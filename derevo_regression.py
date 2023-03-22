from main import read
from config import *
from sklearn import tree

base = read(target_file_name)
data = dict()
data[0], data[1] = [], []

arrau_last_litel_table = []
arrau_litel_table = []
arrau_last_table = []
arrau_table = []
Shetsilk = 1

for target in base:

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

arr = []

for i in range(0, len(arrau_last_table)-2, 2):
    arr.append([arrau_last_table[i], arrau_last_table[i+1]])

ed = 0
nuli = 0
clf = tree.DecisionTreeRegressor()
big_table = clf.fit(arr, arrau_last_litel_table)
y = clf.predict(arr)

print(y)
tree.plot_tree(clf)