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
#method = raw_input("please enter classifier - 0 for svm, 1 for DT, 2 for KNN: ")
#choose = raw_input("please enter data: 0 for all, 1 for content only, 2 for link only: ")
#ignore = raw_input("please enter ignore features: ")
name = raw_input("please enter file name: ")
filename="databackup/"+name + "test.txt"
fintest = open(filename,"r")
testdata = []
testres = []
#print(pred)
lines = fintest.readlines()
for line in lines:
    #line = fintest.readline()
    #print line
    tmp = line.split(" ")
    #print j
    result = int(tmp[0])
    testres = testres + [result]
    tmp_data = tmp[1]
    lis = tmp_data.split(",")
    dataline = []
    for k in range(len(lis)):
        st = lis[k]
        d = float(st)
        dataline.append(d)
    testdata.append(dataline)   
    #print(dataline)
fintest.close()
arrtest=np.array(testdata)
#print arrtest.shape

fin = open("databackup/" + name+".txt", "r")
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

testnum = len(testres)

for kk in range(14):
    print(kk)
    selector = SelectKBest(f_classif, k=kk)
    selector.fit(arrtotdata,arrtotres)
    print(selector.get_support())
