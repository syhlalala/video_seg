import sklearn
import numpy as np
from sklearn import svm
from sklearn import tree
from sklearn import neighbors
import random
import math
import logging
import os
import warnings
from sklearn.feature_selection import *
from sklearn import cross_validation
from sklearn.cross_validation import KFold
from sklearn import metrics

#n=3600
#testn=726
#trainn=n

warnings.filterwarnings("ignore", category=Warning) 
method = raw_input("please enter classifier - 0 for svm, 1 for DT, 2 for KNN: ")
#choose = raw_input("please enter data: 0 for all, 1 for content only, 2 for link only: ")
ignore = raw_input("please enter ignore features: ")
name = raw_input("please enter file name: ")
ignorelist = ignore.split(' ')
print ignorelist

fin = open("../data/" + name+".txt", "r")
res=[]
data=[]
lines = fin.readlines()
count = [[0 for i in range(2)]for j in range(0,101)]
for line in lines:
    #line = fin.readline()
    #print(line)
    tmp = line.split(" ")
    #print j
    result = int(tmp[0])
    res = res + [result]
    tmp_data = tmp[1]
    lis = tmp_data.split(",")
    dataline = []
    #print(line)
    for k in range(len(lis)):
        stk = str(k+1)
        if (stk in ignorelist):
            continue
        st = lis[k]
        d = float(st)
        dataline.append(d)
        #count[int(st)][result] = count[int(st)][result]+1
    data.append(dataline)
    #print(dataline)
fin.close()
arrtotdata = np.array(data)
arrtotres = np.array(res)
n=len(res)

#print(count)

if (method == '0'):
    clf = svm.LinearSVC()
if (method == '1'):
    clf = tree.DecisionTreeClassifier()
if (method == '2'):
    clf = neighbors.KNeighborsClassifier(n_neighbors=50)
#print(arrtotdata)
#print(arrtest)
clf = clf.fit(arrtotdata, arrtotres)
#output = clf.predict(arrtest)
#print(output)

scores = cross_validation.cross_val_score(clf, arrtotdata, arrtotres, cv=10, score_func=metrics.precision_score)
print "%0.3f(%0.3f)" % (scores.mean(), scores.std())
scores = cross_validation.cross_val_score(clf, arrtotdata, arrtotres, cv=10, score_func=metrics.recall_score)
print "%0.3f(%0.3f)" % (scores.mean(), scores.std())
scores = cross_validation.cross_val_score(clf, arrtotdata, arrtotres, cv=10, score_func=metrics.f1_score)
print "%0.3f(%0.3f)" % (scores.mean(), scores.std())
#selector = SelectKBest(f_classif, k=1)
#selector.fit(arrtotdata,arrtotres)
#print(selector.get_support())

