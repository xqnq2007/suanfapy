# -*- coding:utf-8 -*-
from numpy import *
def loadDataSet(filename):
    dataSet=[]
    labelSet=[]
    s=open(filename)
    s1=open(filename)
    m=len(s.readline().split('\t'))-1 
    dataSet=[[1]+[float(w1) for w1 in w.split('\t')[0:m]] for w in s.readlines()]
    labelSet=[float(w1.split('\t')[m]) for w1 in s1.readlines()]        
    return dataSet,labelSet
def simpleLogRess(dataSet,labelSet):
    dataSet,labelSet=loadDataSet('testSet.txt')
    alpha=0.01
    maxIter=40
    dataMat=mat(dataSet)
    labelMat=mat(labelSet).T
    n,m=shape(mat(dataSet))
    theta=mat(ones())
    for i in range(maxIter):
        

