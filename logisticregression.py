# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 21:45:08 2005

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,1,2,3,4])
y=np.array([1,3,5.5,8,9.2])
yp=(1/(1+np.exp(-x)))
a=(np.sum((y-y.mean()*x)) )/(np.sum(x-x.mean()*x) )
b=y.mean()-a*(x.mean())
plt.scatter(x,y)
plt.plot(x,yp,color='r', marker='o')
plt.show