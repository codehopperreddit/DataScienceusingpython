# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 20:24:05 2005

@author: student
"""
import numpy as np
import matplotlib.pyplot as plt
x=np.random.rand(20)*10

y=x + np.random.rand(20)*2
x=np.array(x)
y=np.array(y)
a=(np.sum((y-y.mean()*x)) )/(np.sum(x-x.mean()*x) )
b=y.mean()-a*(x.mean())
print(a)
print(b)
plt.scatter(x,y)
plt.plot(x,a*x+b,color='r', marker='o')
plt.show