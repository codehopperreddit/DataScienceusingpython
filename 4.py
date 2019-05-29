# -*- coding: utf-8 -*-
"""
Create one Numpy arrary of size 3×4 and show reshape(), transpose() operations

@author: Sagnik
"""
import numpy as np
a=np.arange(1,13).reshape(3,4)


print(a)

print("\nTranspose of the array:\n",a.transpose())
print("\nReshaping into a 2x6 array:\n",a.reshape(2,6))
