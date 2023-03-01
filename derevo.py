from random import randint as ri
from main import read
from config import *
from sklearn import tree
from time import sleep

base = read(target_file_name)
data = dict()
data[0],data[1] = [],[]

arrau_last_litel_table = []
arrau_litel_table = []
arrau_last_table = []
arrau_table = []

for target in base:
    if ri(1,3) in [2,3]:
        data[1].append(target)
        arrau_last_table.append(target[-1])
        arrau_table.append(target[:-1])

    else:
        data[0].append(target)
        arrau_last_litel_table.append(target[-1])
        arrau_litel_table.append(target[:-1])


clf = tree.DecisionTreeClassifier()
big_table = clf.fit(arrau_table, arrau_last_table)
litl_table = clf.predict(arrau_litel_table,arrau_last_litel_table)
tree.plot_tree(clf)

