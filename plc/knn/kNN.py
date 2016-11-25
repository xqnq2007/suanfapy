# -*- coding:utf-8 -*-
from numpy import *
def getdistance(a,b):
    return sqrt(sum((a-b)**2))
def loadDataSet(filename):
    f1=open(filename)
    label=[]
    m=len(open(filename).readline().split('\t'))-1
    dataSet=[[float(x) for x in w.split('\t')[0:m]]for w in f1.readlines()]
    for s in open('datingTestSet.txt').readlines():
        label.append(s.strip('\n').split('\t')[3])
    #label=[w1.split('\t')[m].replace('\n','') for w1 in open(filename).readlines()]
    #print label[0:5]
    return dataSet,label
def kNN(dataSet,label,tdata,k):
    dataMat=mat(dataSet)
    labelMat=mat(label)
    n,m=shape(dataMat)
    #print 'n:%d \n' % (n)
    d=[]
    for i in range(n):
        d.append((i,getdistance(dataMat[i].A[0],tdata)))
    d=sorted(d,key=lambda x:x[1])   
    #print d
    classCount={}
    
    for i in range(k):
        tmplabel=label[d[i][0]]
        print tmplabel
        if tmplabel not in classCount.keys():
            classCount[tmplabel]=0
        classCount[tmplabel]=classCount[tmplabel]+1
    #print classCount
    classCount=sorted(classCount.iteritems(),key=lambda d:d[1],reverse=True)
    #print classCount
    return classCount[0][0]
    #print 'len(d):%d \n' % (len(d))
dataSet,label=loadDataSet('datingTestSet.txt')
#print label
n=shape(dataSet)[0]
trainSet=dataSet[0:int(0.9*n)]
testSet=dataSet[int(0.9*n):]
error=0
for i in range(int(0.1*n)):
    hlabel=kNN(trainSet,label,testSet[i],5)
    if hlabel!=label[900+i]:
        error+=1
print error/(0.1*n)

