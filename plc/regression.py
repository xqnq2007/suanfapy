# -*- coding:utf-8 -*-
from numpy import * 
import numpy as np
def loadDataSet(filename):
    numfeat=len(open(filename).readline().split('\t'))-1
    dataSet=[]
    label=[]
    for line in open(filename).readlines():
        #print line
        lineArr=[]
        for i in range(numfeat):
            lineArr.append(float(line.split('\t')[i]))
        dataSet.append(lineArr)
        label.append(float(line.split('\t')[numfeat]))
    return dataSet,label
def regression(dataSet,label):    
    X=mat(dataSet)
    Y=mat(label).T   
    xTx=X.T*X   
    if linalg.det(X.T*X)==0.0:
        print '矩阵为奇异'
        return
    #print X
    #print Y
    w=(X.T*X).I*X.T*Y
    
    return w
    #print dataSet
    
#tmp=len(open('ex0.txt').readline().split('\t'))-1
#print tmp
dataSet,label=loadDataSet('ex0.txt')
#print dataSet,label
w=regression(dataSet,label)
#print w
dataMat=mat(dataSet)
lableMat=mat(label)
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111)
#print len(dataMat[:,1].T.A[0])

#print dataMat[:,1].T.A[0]
ax.scatter(dataMat[:,1].T.A[0],lableMat.A[0])

xcopy=dataMat.copy()
yHat=dataMat*w
ax.plot(dataMat[:,1].T.A[0],yHat.T.A[0])
#print dataMat[:,1].T.A[0]
#print lableMat.T.A[0]
plt.show()
    