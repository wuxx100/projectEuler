# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

a=0

for i in range(0,10):
	x=np.linspace(1,11,11)
	#print(x)
	y=x**10-x**9+x**8-x**7+x**6-x**5+x**4-x**3+x**2-x+1
	#y=x**3
	#print(y)

	cof=np.polyfit(x[0:i+1],y[0:i+1],i)

	p=np.poly1d(cof)

	print(p(i+2))

	a=a+p(i+2)

print(a)





