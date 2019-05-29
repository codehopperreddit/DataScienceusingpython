# -*- coding: utf-8 -*-
"""
Create one Numpy arrary of size 3×4 and perform Slicing operation.

@author: Sagnik
"""

import numpy as np
a=np.arange(1,13).reshape(3,4)
print(a)

print("\nShow only 2nd row:\n",a[1:2])
 
print("\nOnly first column:\n",a[:,:1])

a[:,1:2]=0
print("\nAssigning zero to the second column using slicing:\n",a)