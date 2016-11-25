# -*- coding:utf-8 -*-
from numpy import *
def majorityType(dataSet):
    classCount={}
    for i in range(len(dataSet)):
        classCount[dataSet[i][-1]]=classCount.get(dataSet[i][-1],0)+1
    classCount=sorted(classCount.iteritems(),key=lambda x:x[1],reverse=True)
    #print classCount
    return classCount[0][0]
def getSplitIndex(dataSet,label):
    splitIndex=-1
    minShanonValue=100000
    priShnonValue=getShanonValue(dataSet)
    for i in range(len(label)):
        tmpValue=0.0   
        featSet= zip(*dataSet)[i]  
        featValues=set(featSet)
        for f in featValues:
            tmpNum=featSet.count(f)
            tmpDataSet=[w for w in dataSet if w[i]==f]
            tmpValue+=(float(tmpNum)/len(dataSet))*getShanonValue(tmpDataSet)
        #print tmpValue
        if tmpValue<minShanonValue:
            minShanonValue=tmpValue
            splitIndex=i
    return splitIndex
def getShanonValue(dataSet):
    labelSet=zip(*dataSet)[-1]
    w=set(labelSet)
    tmpValue=0.0
    for wi in w:
        wiNum=labelSet.count(wi)
        tmpP=(float(wiNum))/len(dataSet)
        tmpValue-=tmpP*math.log(tmpP)
    return tmpValue
def createDataSet():
    dataSet=[[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    label=['no surfacing','flippers']
    return dataSet,label
def createTree(dataSet,label):
    #print "第i次递归：\n"
    if zip(*dataSet)[-1].count(dataSet[0][-1])==len(dataSet):
        #print dataSet[0][-1]        
        return dataSet[0][-1]
    if len(label)==0:
        return majorityType(dataSet)
    splitIndex=getSplitIndex(dataSet,label)    
    splitLabel=label[splitIndex]
    #print "splitIndex：%d splitLabel:%s \n" % (splitIndex,splitLabel)
    myTree={splitLabel:{}}   
    
    featValues=set(zip(*dataSet)[splitIndex])
    #print "featValues：\n"
    #print featValues
    del(label[splitIndex])
    sublabel=label[:]
    #print "sublabel：\n"
    #print sublabel
    for f in featValues:
        #print f
        subDataSet=[w[:splitIndex]+w[splitIndex+1:]for w in dataSet if w[splitIndex]==f]
        #print subDataSet
        myTree[splitLabel][f]=createTree(subDataSet,sublabel)
    return myTree
data,label=createDataSet()
print createTree(data,label)
#print getSplitIndex(data, label)
#print [w for w in data if w[-1]=='no']
#print getShanonValue(data)
#print zip(*data)[-1].count('no')
#print majorityType(data)
#print [w for w in data if w[-1]=='no']
#splitIndex=0
#print [[w[:splitIndex]+w[splitIndex+1:]]for w in data]
