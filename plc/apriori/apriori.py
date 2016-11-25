# -*- coding:utf-8 -*-
def generateBigRules(L,minconf,supportData):
    bigRules=[]
    print L
    for i in range(1,len(L)-1):
        for freqSet in L[i]:
            print freqSet
            H=[[w] for w in freqSet]
            print H
            if len(freqSet)>1:
                generateRules(freqSet,H,supportData,bigRules,minconf)
            else:
                calfConf(freqSet,H,supportData,bigRules,minconf)
    return bigRules
def generateRules(freqSet,H,supportData,bigRules,minconf):
    m=len(H[0])
    if len(freqSet)>m+1:
        h1=aprioriGen(H,m)
        generateRules(freqSet,h1,supportData,bigRules,minconf)
    calfConf(freqSet,H,supportData,bigRules,minconf)
def calfConf(freqSet,H,supportData,bigRules,minconf):
    print freqSet
    print H
    for w in H:
        print w
        tmpconf=float(supportData[str(freqSet)])/supportData[str(list(set(freqSet)-set(w)))]
        print tmpconf
        if (tmpconf)>minconf:
            print str(list(set(freqSet)-set(w)))+'-->'+str(w)+str(tmpconf)
            bigRules.append(str(list(set(freqSet)-set(w)))+'-->'+str(w)+str(tmpconf))
def aprioriGen(L,k):
    s=[]
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):            
            L[i].sort()
            L[j].sort()
            L1=L[i][:k-2]
            L2=L[j][:k-2]            
            if L1==L2:
                s.append(list(set(L[i])|set(L[j])))
    return s
def getSupportData(DataSet,L):
    supportData={}
    dataNum=len(DataSet)
    #print dataNum
    for w in L:
        #print w
        sw=str(w)
        #supportData[sw]=0        
        for d in DataSet: 
            #print w,d           
            if set(w).issubset(set(d)):
                #print 'dddd'
                supportData[sw]=supportData.get(sw,0)+1
        #print supportData[sw]
    for x in supportData.keys():
        #print supportData[x]           
        supportData[x]=supportData[x]/float(dataNum)
    return supportData
def createC1(dataSet):
    c1=[]
    for w in dataSet:
        for wi in w:
            if wi not in c1:
                c1.append(wi)
    return c1
def createL1(c1,dataSet,minSupport):
    L1=[] 
    supportData1={}
    for w in c1:
        for d in dataSet:
            if w in d:
                supportData1[str([w])]=supportData1.get(str([w]),0)+1
        supportData1[str([w])]=supportData1[str([w])]/float(len(dataSet))
        if supportData1[str([w])]<minSupport:            
            del(supportData1[str([w])])
        else:
            L1.append([w])
    return L1,supportData1
def apriori(dataSet,minSupport):
    c1=createC1(dataSet)
    L1,supportData=createL1(c1, dataSet, minSupport)
    k=2    
    L=[L1]
    #print L
    while(len(L[0])>0):
        Lk=aprioriGen(L[0],k)
        #print Lk
        L.insert(0,Lk)
        #print Lk
        #print getSupportData(dataSet, Lk)
        #print L
        supportData=dict(supportData.items()+getSupportData(dataSet, Lk).items())        
        k+=1
    return L,supportData
def loadDataSet():
    return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]
data=loadDataSet()
L,supportData=apriori(data,0.7)
print L,supportData
print generateBigRules(L, 0.7, supportData)