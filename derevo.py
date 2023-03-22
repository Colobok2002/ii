
from main import read
from config import *
from sklearn import tree


def mas_for_derevo():

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

    return arr,arrau_last_litel_table

def klasifier_metod():

    arr,arrau_last_litel_table = mas_for_derevo()
    ed = 0
    nuli = 0
    clf = tree.DecisionTreeClassifier()
    clf.fit(arr, arrau_last_litel_table)
    y = clf.predict(arr)

    for i in range(len(y)-1):
        el1 = arrau_last_litel_table[i]
        el2 = y[i]
        if el1 == el2:
            ed += 1
        else:
            nuli += 1

    tree.plot_tree(clf)

    print(ed/len(y))

def regresion_metod():

    arr, arrau_last_litel_table = mas_for_derevo()

    clf = tree.DecisionTreeRegressor()
    clf.fit(arr, arrau_last_litel_table)
    y = clf.predict(arr)
    print(y)

if __name__ == '__main__':
    klasifier_metod()
    regresion_metod()