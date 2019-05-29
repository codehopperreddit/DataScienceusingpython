#a={}
#sname=[]
#sid=[]
#sad=[]

#for i in range(1):
    #name=input("Enter the name:")
    #ssid=int(input("Enter the Id"))
   # ad=input("Enter address")
  #  sname.append(name)
 #   sid.append(ssid)
#    sad.append(sad)

#a.update(sname)
#a.update(sid)
#a.update(sad)
a=[]
student=[]
num=int(input("Enter number of students"))

for i in range(0,num):
    name=input("Enter the name:")
    ssid=int(input("Enter the Id"))
    sad=input("Enter address")
    sage=int(input("Enter Age:"))
    student.append(name)
    student.append(ssid)
    student.append(sad)
    student.append(sage)
    a.append(student)
    student=[]

print("name----ID----address----age----")
sss=[]
temp=tuple(a)
print(temp)
for i in range(0,num):
    #print(set(a[i]))
    print(a[i])
    #sss.append(set(a[i]))
    #print(sss)


    
