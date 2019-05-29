# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:59:49 2019

@author: admin
"""

import numpy as np
import matplotlib.pyplot as plt

s=np.random.normal(0.0,2.0,4000)
plt.hist(s,30)
plt.show()