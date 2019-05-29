# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:02:07 2019

@author: admin
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,3*np.pi,500)
y=2**x
#plt.subplot(4,2,4)
#plt.plot(x,y)
#plt.show()
y1=np.sin(x)
y2=np.cos(x)
y3=(x-2)**2
plt.subplot(421)
plt.plot(x,y1,color='k',linestyle='--')
plt.subplot(4,2,2)
plt.plot(x,y2,color='r',linestyle='-')
plt.subplot(4,2,8)
plt.plot(x,y3)
plt.show()
