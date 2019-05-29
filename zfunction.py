import math as mt

a=[20,15,26,32,18,28,35,14,26,22,17]

b=len(a)
sum=0
for i in range(0,b):
    sum+=a[i]

mean=sum/b

for i in range(0,b):
    variance=((a[i]-mean)**2)/b
    sd=mt.sqrt(variance)
    z=(a[i]-mean)/sd
    print("\nZ-score of ",a[i],"is",'%.2f'%z)
