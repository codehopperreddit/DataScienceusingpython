import numpy as np
import matplotlib.pyplot as plt
x=[t for t in range(20)]
y=[(t-2)**2 for t in x]
print(x)
print(y)

plt.plot(x,y,color='k',linestyle='--', marker='.')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('visualization')

plt.show()