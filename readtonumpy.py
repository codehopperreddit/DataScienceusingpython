import numpy as np
import matplotlib.pyplot as plt
 
x=np.array([[3,4,5],[6,9,15]])
np.savetxt('abc.txt',x,fmt='%d')
y=np.loadtxt('abc.txt')
 
plt.plot(x[0],y[1],color='k',linestyle='--', marker='.')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('visualization')

plt.show()

 