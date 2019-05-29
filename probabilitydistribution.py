# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 20:24:04 2005

@author: student
"""

import math as mt
import numpy as np
import matplotlib.pyplot as plt
a=[20,15,26,32,18,28,35,14,26,22,17]

b=len(a)
sum=0
for i in range(0,b):
    sum+=a[i]

mean=sum/b

probdis=[]
c=0

for i in range(0,b):
    variance=((a[i]-mean)**2)/b
    sd=mt.sqrt(variance)
    mx=-((a[i]-mean)**2)/(2*(sd)**2)
    np.exp(mx)
    probdis.append((1/(sd*mt.sqrt(2*np.pi))*mx))
    
  
    

plt.scatter(a,probdis)
plt.show()
x=np.array([2,3,4,5,6,7,9,10])

y=np.array([7,9,8,11,13,20,21,30])
plt.scatter(x,y)

from sklearn.linear_model import LinearRegression
clf=LinearRegression()
x2=x.reshape(-1,1)
clf.fit(x2,y)
m=clf.coef_
c=clf.intercept_
z=m[0]*x+c
plt.plot(x,z,color='r')

print(m)
print(c)
p=clf.predict([12])
print(p)
plt.show()
          