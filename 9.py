# -*- coding: utf-8 -*-
"""
Create a Linear Regression model for one independent variable and 3 dependent variables
(consider suitable random data or any suitable dataset) by importing LinearRegression from
sklearn.

@author: Sagnik
"""


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x=np.array([[0,0,1,2,2],[0,0,0,1,2],[0,0,0,0,1]])
y=np.array([0,0,1,1,1])

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
"""
outlook=np.array([0,0,1,2,2])
temp=np.array([0,0,0,1,2])
humid=np.array([0,0,0,0,1])
windy=np.array([0,1,0,0,0])
play=np.array([0,0,1,1,1])
"""








0
