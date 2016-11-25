# coding:utf-8
from numpy import *
#import random as np
def kmeans(dataSet,k):
    n,m=shape(dataSet)
    centroids=initCentroids(dataSet,k,m)
    classCluster=mat(tile([-1.0,0.0],(n,1)))
    print classCluster
    clusterChanged=True
    print centroids
    while(clusterChanged):
        clusterChanged=False
        for i in range(1):
            mindistan=float("inf")
            minIndex=-1
            for j in range(k):
                eculdistance=getEculDistance(dataSet[i],centroids[j])
                print eculdistance
                if eculdistance<mindistan:
                    mindistan=eculdistance
                    minIndex=j
            print mindistan
            print minIndex
            print classCluster[i,0]
            if minIndex!=classCluster[i,0]:
                clusterChanged=True
                classCluster[i,0]=minIndex
                classCluster[i,1]=eculdistance
        print classCluster
        for i in range(k):
            print i
            #print dataSet[nonzero(classCluster[:,0]==minIndex)[0]]
            print dataSet([1])
            #print dataSet(nonzero(classCluster[:,0]==-1)[0].A[0])
            centroids[:,i]=sum(dataSet[nonzero(classCluster[:,0]==i)[0]],0)/float(n)
    return centroids,classCluster
def initCentroids(dataSet,k,m):
    centroids=mat(zeros([k,m]))
    #print centroids
    for i in range(m): 
        #print centroids[:,i]
        x=1
        tmp=min(mat(dataSet)[:,i])+random.random((k,1))*(max(mat(dataSet)[:,i])-min(mat(dataSet)[:,i]))
        #print tmp
        centroids[:,i]=min(mat(dataSet)[:,i])+random.random((k,1))*(max(mat(dataSet)[:,i])-min(mat(dataSet)[:,i]))
    return centroids    
def getEculDistance(lista,listb):
    return sqrt(sum(square(mat(lista)-mat(listb))))
def loadDataSet(filename):
    m=len(open(filename).readline().split('\t'))
    dataSet=[[float(wi) for wi in w.split('\t')] for w in open(filename).readlines()]
    return dataSet
data=loadDataSet('testSet.txt')
centtroids,classCluster=kmeans(data, 3)
#classCluster=mat(tile([-1.0,0.0],(100,1)))


