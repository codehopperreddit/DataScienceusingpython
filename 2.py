"""
Write a program in Python to find odd and even numbers between 1 and 20.

@author: Sagnik

"""

even=[]
odd=[]
for i in range(1,20):
	if i%2==0:
		even.append(i)
	else:
		odd.append(i)

print("Odd Numbers:",odd)
print("Even Numbers:",even)