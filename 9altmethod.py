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

x=np.random.randint(1,100,50)

#plotting function
def plotda(x2,y):
    clf.fit(x2,y)
    m=clf.coef_
    c=clf.intercept_
    z=m[0]*x+c
    plt.plot(x2,z,color='r')
    plt.scatter(x,y,color='b')
    plt.show()


y1=x*np.random.rand(50)
y2=x*np.random.rand(50)
y3=x*np.random.rand(50)
print("Independent data:\n")
print(x)
clf=LinearRegression()
x2=x.reshape(-1,1)
print("Dependent data 1 and the plot:\n")
print(y1)
plotda(x2,y1.reshape(-1,1))
print("Dependent data 2 and the plot:\n")
print(y2)
plotda(x2,y2.reshape(-1,1))
print("Dependent data 3 and the plot:\n")
print(y3)
plotda(x2,y3.reshape(-1,1))


