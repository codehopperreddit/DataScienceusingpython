#mean
def mean(a):
    
    b=len(a)
    sum=0
    for i in range (0,b):
        sum+=a[i]
    avg = sum/b

    print(avg)
#median
def median(a):
    a.sort()  
    b=len(a)    
    if b%2==0:
        b-=1    
    b/=2    
    b=int(b)
    print(a[b])
#mode
def mode(a):
    b=len(a)
    l=0
    for i in range (0,b):
        n=a.count(a[i])
        if(n>l):
            l=n 
            num=a[i]
        


    print(num)


#choosing stuff
a=[4,2,9,9,6,4,5]  
mean(a)
median(a)
mode(a)