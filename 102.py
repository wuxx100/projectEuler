# -*- coding:utf-8 -*-
import numpy as np


def cross(a,b):
	return a[0]*b[1]-a[1]*b[0]

i=0
with open('102.txt','r') as f:
    for line in f:
        result=map(float,line.split(','))
        a=cross(np.subtract([0,0],result[0:2]),np.subtract(result[4:6],result[0:2]))
        b=cross(np.subtract([0,0],result[2:4]),np.subtract(result[0:2],result[2:4]))
        c=cross(np.subtract([0,0],result[4:6]),np.subtract(result[2:4],result[4:6]))
    	if ((a>=0 and b>=0 and c>=0) or (a<=0 and b<=0 and c<=0)):
    		print("yes")
    		print(result[0:6])
    		i=i+1
print(i)
    	




#A=[-340,495]
#B=[-153,-910]
#C=[835,-947]
#D=[0,0]





#result=[]
#with open('a.txt','r') as f:
#    for line in f:
#        result.append(map(float,line.split(',')))
#    print(result)