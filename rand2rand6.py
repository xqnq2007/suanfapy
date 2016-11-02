# -*- coding:utf-8 -*-
import random
def unbalancedcoin():
    rk=random.randint(0,100)
    if rk<30:
        return 0
    else:
        return 1
def balancedcoin():
    while(True):
        a=unbalancedcoin()
        if a!=unbalancedcoin():
            return a+1
def rand6():
    rand16=8*balancedcoin()+4*balancedcoin()+2*balancedcoin()+balancedcoin()-14
    while(rand16>12):
        rand16=8*balancedcoin()+4*balancedcoin()+2*balancedcoin()+balancedcoin()-14
    return rand16%6+1
a=[]
b=[0,0,0,0,0,0]
b2=[0,0]
for i in range(10000):
    tmp=rand6()
    a.append(tmp)
    b[tmp-1]+=1
for i in range(0,6):
    print b[i]
   
'''for i in range(10000):
    tmp=balancedcoin()
    a.append(tmp)
    b2[tmp-1]+=1
for i in range(0,2):
    print b2[i]'''
    
    
    