import math as mt

x=[1,2,3]
y=[2,4,6]
xl=len(x)
yl=len(y)
sum=0
for i in range(0,xl):
	sum+=x[i]
mx=sum/xl
sum=0
for i in range(0,yl):
	sum+=y[i]
my=sum/yl

a=[t-mx for t in x]
b=[t-my for t in y]
ab=[0.0]*len(x)
ab=[0]


ab=[a[i]*b[i] for i in range (len(x))]
a2=[t*2 for t in a]
corr=sum(ab)/mt.sqrt(sum(a2)*sum(b2))
