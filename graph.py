import numpy as np
import matplotlib.pyplot as plt
from main import read
from config import *

base = read(target_file_name)
data = dict()




for row in base:
    try:
        data['Local Sales'].append(row[2])
    except:
        data['Local Sales'] = [row[2]]
    try:
        data['Buyer'].append(row[-1])
    except:
        data['Buyer'] = [row[-1]]


shag = max(data['Local Sales']) // 9

data_sort = {}

k = 0

for i in range(0,9):
    if i == 0:
        data_sort[i] = {'min': i*shag, 'max' : shag*(i+1),'kolvo' : 0 ,'kolvo_nb' : 0  ,'name':f"{i*shag} - {shag*(i+1)}"}
    else:
        data_sort[i] = { 'min': i * shag + 1, 'max': shag * (i + 1), 'kolvo' : 0 ,'kolvo_nb' : 0  ,'name':f"{i*shag + 1} - {shag*(i+1)}"}

    k = i

data_sort[k+1] = { 'min': data_sort[k]['max']+1, 'max': max(data['Local Sales']),'kolvo' : 0 ,'kolvo_nb' : 0  ,'name':f"{data_sort[k]['max']+1} - {max(data['Local Sales'])}"}

for row in base:
    for j in data_sort:
        if row[2] >= data_sort[j]['min'] and row[2] <= data_sort[j]['max']:
            if row[-1] == 0:
                data_sort[j]['kolvo_nb'] += 1
            else:
                data_sort[j]['kolvo'] += 1
            continue



for i in data_sort:
    print(data_sort[i])

name_base = []
kolvo = []
kolvo_nb = []

for i in data_sort:
    name_base.append(data_sort[i]['name'])
    kolvo.append(data_sort[i]['kolvo'])
    kolvo_nb.append(data_sort[i]['kolvo_nb'])


species = (name_base)
sex_counts = {
    'Buyer': kolvo,
    'Buyer_no': kolvo_nb,
}
width = 0.6  # the width of the bars: can also be len(x) sequence


fig, ax = plt.subplots()
bottom = np.zeros(10)

for sex, sex_count in sex_counts.items():
    p = ax.bar(species, sex_count, width, label=sex, bottom=bottom)
    bottom += sex_count

    ax.bar_label(p, label_type='center')

ax.set_title('Number of penguins by sex')
ax.legend()

plt.show()