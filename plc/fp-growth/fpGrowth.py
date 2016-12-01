class treeNode:    
    def __init__(self,name,num,parent):
        self.name=name
        self.count=num
        self.nodeLink=None
        self.parent=parent
        self.children={}
    def inc(self,num):
        self.count+=num
    def dsp(self,ind=1):
        for child in self.children.values():
            print ' '*ind ,child.name,' ', child.count
            child.dsp(2)
def mineTree(myFPTree,myHeadTable,minSub,prefix,releteRules):
    frequentSet=sorted(myHeadTable.items(),key=lambda x:x[0])
    for condBase in frequentSet:
        newprefix=prefix.copy()
        newprefix.add(conBase)
        relateRules.append(newprefix)
        condPatBase=getPatBase(myFPTree,myHeadTable)
        #node1=treeNode('Null',1,None)
        myTree,myHead=createTree(condPatBase,minSub)
        if myHead!=None:
           mineTree(myTree,myHead,minSub,newprefix,releteRules)
def getPatBase(myFPTree,myHeadTable):
    patBase={}
    for item in myHeadTable:
        tmpPath=asendTree(myHeadTable)
def createTree(dataSet,minSub,root):
    headTable={}
    for trans in dataSet:
        for data in trans:
            headTable[data]=headTable.find(data,0)+dataSet[trans]
    if len(headTable)==0:
        return None,None    
    headTable[data]=[headTable[data],None] 
    for w in headTable.keys():
        if headTable[w][0]<minSub:
            delete(headTable[data])    
    freqset=set(headTable.keys())
    headTable=sorted(headTable.items(),key=lambda x:x[0])
    node1=treeNode('Null',1,None)
    for trans in dataSet:
        localD={}
        for data in trans:
            if data in freqset:
                localD[data]=headTable[data][0]
        localD=sorted(localD.items(),key=lambda x:x[0])
        updataTree(node1,localD,headTable)
def updateTree(root,localD,headTable):
    if localD[0].key() in root.children:
        root.children[localD[0].key()].inc(localD[0])
    else:
        root.children[localD[0].key()]=treeNode(localD[0].key(),1,root)
    if len(localD>1):
        updateTree(root.children[localD[0].key()], localD[1:], headTable)
    else:
        updateHeadTable(root.children[localD[0].key()],headTable)
def updateHeadTable(node,headTable):
    if headTable[node.name][1]!=None:
        tmpNode=headTable[node.name][1]
        while(tmpNode.nodeLink!=None):
            tmpNode=tmpNode.nodeLink
        tmpNode.nodeLink=node

        