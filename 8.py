# -*- coding: utf-8 -*-
"""
Write a program in python to create Linear Regression model for one independent variable
and one dependent variable without importing LinearRegression from sklearn and then
visualize the approximation of data points by line using Matplotlib.

@author: Sagnik
"""
import numpy as np
import matplotlib.pyplot as plt
def line(slope, intercept):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--',color='b')



x=np.array([2,3,5,6])
y=np.array([4.5,7.2,9.2,11.5])
b=(np.sum((y-np.mean(y))*x))/(np.sum((x-np.mean(x))*x))
a=np.mean(y)-(b*(np.mean(x)))
plt.scatter(x,y,marker='o',color='r')
line(a,b)
plt.show()
