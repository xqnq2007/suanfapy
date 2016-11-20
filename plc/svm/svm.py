# -*- coding:utf-8 -*- 
from numpy import *
import random
def clipa(a,L,H):
    if a<L:
        return L
    if a>H:
        return H
    return a
def selectj(i,n):
    j=random.randint(0,n-1)
    while j==i:
        j=random.randint(0,n-1)
    return j
def loadDataSet():
    dataSet=[]
    label=[]
    numfeat=len(open('testSet.txt').readline().split('\t'))-1
    '''for w in open('testSet.txt').readlines():
        rawlinearr=w.split('\t')
        linearr=[]
        for i in range(numfeat):
            linearr.append(float(rawlinearr[i]))
        dataSet.append(linearr)        
        label.append(float(rawlinearr[numfeat]))'''
    dataSet=[[float(s) for s in w.split('\t')[0:numfeat]] for w in open('testSet.txt').readlines()]
    label=[float(w.split('\t')[numfeat]) for w in open('testSet.txt').readlines()]
    return dataSet,label
        
def simpleSVM(dataSet,label,C):
    dataMat=mat(dataSet)
    labelMat=mat(label).T
    n,m=shape(dataMat)
    alphas=zeros(n)
    iter=0
    b=0    
    print "n:%d m:%d\n" %(n,m) 
    while(iter<40): 
        isalphachaged=0        
        for i in range(n):
            ui=float(mat(alphas*label)*(dataMat*dataMat[i].T))+b  
            Ei=ui-float(label[i]) 
            print "第%d条数据 b: %f\n" % (i,b) 
            print alphas[alphas>0]
            print "ui:%d\n" %(ui) 
            if (label[i]*Ei>0.001 and alphas[i]>0) or (label[i]*Ei<-0.001 and alphas[i]<C):
                j=selectj(i,n)
                cathy=alphas[i]*label[i]+alphas[j]*label[j]
                print "j:%d cathy:%d\n" %(j,cathy) 
                print "label[i]:%d label[j]:%d\n" %(label[i],label[j]) 
                if label[i]!=label[j]:
                    L=max(0,alphas[j]-alphas[i])
                    H=min(C,C+alphas[j]-alphas[i])                   
                else:
                    L=max(0,alphas[j]+alphas[i]-C)
                    H=min(C,alphas[j]+alphas[i]) 
                if L==H:
                    print "L==H"
                    continue
                print "L:%.2f H:%.2f\n" %(L,H) 
                alphajold=alphas[j].copy()
                alphaiold=alphas[i].copy()
                kii=dataMat[i]*dataMat[i].T
                #print "i:%d kii:%d" %(i,kii) 
                kjj=dataMat[j]*dataMat[j].T
                kij=dataMat[i]*dataMat[j].T                
                eta=kii+kjj-2*kij
                print "kii:%d kjj:%d kij:%d eta:%d\n" %(kii,kjj,kij,eta) 
                if eta<=0:
                    print "eta<=0"
                    continue
                uj=float(mat(alphas*label)*(dataMat*dataMat[j].T))+b                 
                Ej=uj-float(label[j]) 
                print "uj:%d Ei:%d Ej:%d\n" %(uj,Ei,Ej) 
                alphas[j]=alphajold+float(label[j]*(Ei-Ej))/(kii+kjj-2*kij)
                alphas[j]=clip(alphas[j],L,H)
                print "alphas[j]:%.2f\n" %(alphas[j]) 
                if alphas[j]-alphajold<0.0001:
                    print "alphaj not moving"
                    continue
                alphas[i]=alphaiold-float(label[j]*label[i])*(alphas[j]-alphajold)
                b1=b-label[i]*kii*(alphas[i]-alphaiold)-label[j]*kij*(alphas[j]-alphajold)-Ei
                b2=b-label[i]*kij*(alphas[i]-alphaiold)-label[j]*kjj*(alphas[j]-alphajold)-Ej
                print "alphas[i]:%.2f b1:%.2f b2:%.2f\n" %(alphas[i],b1,b2) 
                if alphas[i]>0 and alphas[i]<C:
                    b=b1
                elif alphas[j]>0 and alphas[j]<C:
                    b=b2
                else: b=float(b1+b2)/2
                print "b:%.2f\n" %(b) 
                isalphachaged+=1
                print "iter:%d alphachaged:%d" % (iter,isalphachaged)
                
        if isalphachaged==0:
            iter+=1            
        else:
            iter=0
        print "iter:%d" % iter
    w=mat(alphas*label)*dataMat
    return w,b,alphas
def selectJrand(i,m):
    j=i #we want to select any J not equal to i
    while (j==i):
        j = int(random.uniform(0,m))
    return j
def clipAlpha(aj,H,L):
    if aj > H: 
        aj = H
    if L > aj:
        aj = L
    return aj
def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    dataMatrix = mat(dataMatIn); labelMat = mat(classLabels).transpose()
    b = 0; m,n = shape(dataMatrix)
    alphas = mat(zeros((m,1)))
    iter = 0
    while (iter < maxIter):
        alphaPairsChanged = 0
        for i in range(m):
            fXi = float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[i,:].T)) + b
            Ei = fXi - float(labelMat[i])#if checks if an example violates KKT conditions
            if ((labelMat[i]*Ei < -toler) and (alphas[i] < C)) or ((labelMat[i]*Ei > toler) and (alphas[i] > 0)):
                j = selectJrand(i,m)
                fXj = float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[j,:].T)) + b
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy(); alphaJold = alphas[j].copy();
                if (labelMat[i] != labelMat[j]):
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L==H: print "L==H"; continue
                eta = 2.0 * dataMatrix[i,:]*dataMatrix[j,:].T - dataMatrix[i,:]*dataMatrix[i,:].T - dataMatrix[j,:]*dataMatrix[j,:].T
                if eta >= 0: print "eta>=0"; continue
                alphas[j] -= labelMat[j]*(Ei - Ej)/eta
                alphas[j] = clipAlpha(alphas[j],H,L)
                if (abs(alphas[j] - alphaJold) < 0.00001): print "j not moving enough"; continue
                alphas[i] += labelMat[j]*labelMat[i]*(alphaJold - alphas[j])#update i by the same amount as j
                                                                        #the update is in the oppostie direction
                b1 = b - Ei- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[i,:].T - labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[i,:]*dataMatrix[j,:].T
                b2 = b - Ej- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[j,:].T - labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[j,:]*dataMatrix[j,:].T
                if (0 < alphas[i]) and (C > alphas[i]): b = b1
                elif (0 < alphas[j]) and (C > alphas[j]): b = b2
                else: b = (b1 + b2)/2.0
                alphaPairsChanged += 1
                print "iter: %d i:%d, pairs changed %d" % (iter,i,alphaPairsChanged)
        if (alphaPairsChanged == 0): iter += 1
        else: iter = 0
        print "iteration number: %d" % iter
    return b,alphas
def loadDataSet1():
    dataMat = []; labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat
dataSet,label=loadDataSet()

w,b,alphas=simpleSVM(dataSet,label,0.6)
'''dataMat=mat(dataSet)
tmp=dataMat[0]*dataMat[0].T
print tmp'''
#b,alphas=smoSimple(dataSet,label,0.6,0.001,40)
#u= multiply(alphas,mat(label).T).T*(mat(dataSet)*mat(dataSet).T)+b

#print alphas[alphas>0]
import numpy as np
import matplotlib.pyplot as mp
fig=mp.figure()
ax=fig.add_subplot(111)
ax.scatter(mat(dataSet)[:,0].T.A[0],mat(dataSet)[:,1].T.A[0])
#ax.plot(mat(dataSet)[:,0].T.A[0],u.A[0])
#mp.show()
for i in range(100):
    if alphas[i]>0:        
        theta = np.arange(0, 2 * np.pi + 0.1,2 * np.pi / 1000)
        x = np.cos(theta)
        y = np.sin(theta)
        mp.plot(dataSet[i][0]+0.2*x,dataSet[i][1]+0.2*y , color='red')

mp.show()




