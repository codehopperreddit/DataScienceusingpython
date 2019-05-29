# -*- coding: utf-8 -*-
"""
Write a program in Python to find mean, median and mode without importing additional
#module.

@author: Sagnik
"""

#mean
def mean(a):
    
    b=len(a)
    sum=0
    for i in range (0,b):
        sum+=a[i]
    avg = sum/b

    print("Mean:",avg)
#median
def median(a):
    a.sort()  
    b=len(a)    
    if b%2==0:
        b-=1    
    b/=2    
    b=int(b)
    print("Median:",a[b])
#mode
def mode(a):
    b=len(a)
    l=0
    for i in range (0,b):
        n=a.count(a[i])
        if(n>l):
            l=n 
            num=a[i]
        


    print("Mode:",num)


#taking user input
a=[]
n = int(input("Enter number of elements : ")) 
  
print("\nEnter the numbers:\n")
for i in range(0, n): 
    t= int(input()) 
  
    a.append(t) 
      
print(a) 

mean(a)
median(a)
mode(a)