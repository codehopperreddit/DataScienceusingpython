# -*- coding: utf-8 -*-
"""
Consider two Numpy arrarys of size 2×3 and show matrix addition, subtraction and matrix
multiplication.

@author: Sagnik
"""

import numpy as np
a=np.arange(1,7).reshape(2,3)
print("\nFirst array:\n",a)

b=np.arange(7,13).reshape(2,3)
print("\nSecond array:\n",b)

print("\nMatrix Addition:\n",a+b)
print("\nMatrix Subtraction:\n",a-b)
print("\nMatrix Multiplication:\n",a.dot(b.transpose()))