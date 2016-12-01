# coding:utf-8
import fpGrowth
t1=fpGrowth.treeNode('node1',9,None)
t1.children['t2']=fpGrowth.treeNode('node2',10,None)
t1.children['t3']=fpGrowth.treeNode('node3',11,None)
t1.dsp(1)
