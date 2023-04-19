import csv
from config import *
from random import random


def read(target_file_name):
    d = {}
    i = 0
    base = []

    with open(target_file_name, 'r', newline='') as csvfile:

        spamreader = csv.reader(csvfile)

        isFirstRow = True

        for row in spamreader:
            if isFirstRow:
                isFirstRow = False
                continue

            kesh = []

            for simvol in row:
                try:
                    kesh.append(int(simvol))
                except:
                    if d.get(simvol) == None:
                        d[simvol] = i
                        kesh.append(i)
                        i += 1

                    else:
                        kesh.append(d[simvol])
                # finally:
                # print("!!!!!!!!", kesh)
            if len(kesh) > 1:
                base.append(kesh)
    # print(d)
    # print(base)
    index0 = 0
    index2 = 0
    first_mas = []
    second_mas = []
    for el in base:
        index0 += el[0]
        first_mas.append(el[0])
        index2 += el[2]
        second_mas.append(el[2])
    k = index2 / index0
    print(k)
    #print(first_mas)
    #print(second_mas)
    koef_mas = []
    for index in range(len(second_mas)):
        if first_mas[index] == 0 and second_mas[index] == 0:
            koef = 0
            koef_mas.append(koef)
        else:
            koef = second_mas[index] / first_mas[index]
            koef_mas.append(koef)
    print(koef_mas)
    x_mas = []
    x_mas.append(base[0])
    x_mas.append(base[5])
    x_mas.append(base[10])
    x_mas.append(base[8])
    x_mas.append(base[9])
    x_mas.append(base[4])
    x_mas.append(base[7])
    print(x_mas)
    return base



def create_train_tet(base):
    train = []
    test = []

    for s in base:
        if random() < 0.6666:
            train.append(s)
        else:
            test.append(s)

    return train, test


def save(save_file_name, base):
    with open(save_file_name, 'w') as file:
        for row in base:
            print(row)
            file.write(str(row))
            file.write('\n')


def train_tree_classifier(x, y):
    from sklearn.model_selection import train_test_split
    from sklearn.datasets import load_iris
    from sklearn.tree import DecisionTreeClassifier
    from sklearn import tree

    X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)

    clf = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)
    clf.fit(X_train, y_train)

    predicted_Y_test = clf.predict(X_test)

    ed = 0
    nuli = 0

    for i in range(len(predicted_Y_test)):
        el1 = y_test[i]
        el2 = predicted_Y_test[i]
        if el1 == el2:
            ed += 1
        else:
            nuli += 1

    tree.plot_tree(clf)

    print(ed / len(predicted_Y_test))


def random_forest_classifier(x, y, X_test, y_test):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn import tree

    clf = RandomForestClassifier(max_depth=2, random_state=0)
    clf.fit(x, y)

    predicted_Y_test = clf.predict(X_test)

    ed = 0
    nuli = 0

    for i in range(len(predicted_Y_test)):
        el1 = y_test[i]
        el2 = predicted_Y_test[i]
        if el1 == el2:
            ed += 1
        else:
            nuli += 1

    tree.plot_tree(clf.estimators_[0])

    print(ed / len(predicted_Y_test))


def Neural_network_model(x, y, X_test, y_test):
    from sklearn.neural_network import MLPClassifier
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                        hidden_layer_sizes=(5, 2), random_state=1)
    clf.fit(x, y)
    MLPClassifier(alpha=1e-05, hidden_layer_sizes=(5, 2), random_state=1,
                  solver='lbfgs')
    predicted_Y_test = clf.predict(X_test)

    ed = 0
    nuli = 0

    for i in range(len(predicted_Y_test)):
        el1 = y_test[i]
        el2 = predicted_Y_test[i]
        if el1 == el2:
            ed += 1
        else:
            nuli += 1

    # tree.plot_tree(clf.estimators_[0])

    print(ed / len(predicted_Y_test))


def gaussian_naive_bayes(x, y):
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import GaussianNB

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=0)
    gnb = GaussianNB()
    y_pred = gnb.fit(X_train, y_train).predict(X_test)
    ed = 0
    nuli = 0

    for i in range(len(y_pred)):
        el1 = y_test[i]
        el2 = y_pred[i]
        if el1 == el2:
            ed += 1
        else:
            nuli += 1
    print(ed / len(y_pred))


def gradient_boosting_classifier(x, y, X_test, y_test):
    from sklearn.ensemble import GradientBoostingClassifier
    X_train = x
    y_train = y

    clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,
                                     max_depth=1, random_state=0).fit(X_train, y_train)
    print(clf.score(X_test, y_test))
    # y_pred = clf.fit(X_train, y_train)

    # ed = 0
    # nuli = 0

    # for i in range(len(y_pred)):
    #     el1 = y_test[i]
    #     el2 = y_pred[i]
    #     if el1 == el2:
    #         ed += 1
    #     else:
    #         nuli += 1
    # print(ed/len(y_pred))


if __name__ == '__main__':
    # save(save_file_name,read(target_file_name))
    trasform_file = read("MarketData.csv")
    train, test = create_train_tet(trasform_file)
    trainX = [s[:-1] for s in train]
    trainY = [s[-1] for s in train]
    testX = [s[:-1] for s in test]
    testY = [s[-1] for s in test]
    #train_tree_classifier(trainX, trainY)
    #random_forest_classifier(trainX, trainY, testX, testY)
    #Neural_network_model(trainX, trainY, testX, testY)
    #gaussian_naive_bayes(trainX, trainY)
    #gradient_boosting_classifier(trainX, trainY, testX, testY)