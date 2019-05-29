# -*- coding: utf-8 -*-
"""
Use hstack() and vstack() to join Numpy arrays

@author: Sagnik
"""

import numpy as np
a=np.arange(1,7).reshape(2,3)
print("\nFirst array:\n",a)

b=np.arange(7,13).reshape(2,3)
print("\nSecond array:\n",b)  
  
print("\nSingle array Horizontally:\n",np.hstack((a,b)))
print("\nSingle array Vertically:\n",np.vstack((a,b)))