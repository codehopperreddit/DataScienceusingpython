#program to consider an empty list, add six number then pop 3 numbers display the list value
x=[] 


x = [int(x) for x in input().split()] 
x.append(1)
x.append(2)
x.append(3)
x.append(4) 
x.append(5) 
x.append(6) 
del x[0]
del x[0]
del x[0]
print(x)



x.pop()
print(x)
