import csv
from config import *


def read(target_file_name):

    with open(target_file_name, 'r', newline='') as csvfile:

        base = []

        spamreader = csv.reader(csvfile)

        for row in spamreader:

            kesh = []

            for simvol in row:
                try:
                    if simvol.isdigit():
                        kesh.append(int(simvol))
                    else:
                        if simvol == "":
                            kesh.append('$')
                        elif simvol == 'Private':
                            kesh.append(ord('p'))

                        elif simvol == '#N/A':
                            kesh.append('!')
                        else:
                            kesh.append(ord(simvol))
                except:
                    continue

            if len(kesh) > 1:
                base.append(kesh)
    return base


def save(save_file_name,base):

    with open(save_file_name, 'w') as file:

        for row in base:
            print(row)
            file.write(str(row))
            file.write('\n')

if __name__ == '__main__':

    save(save_file_name,read(target_file_name))