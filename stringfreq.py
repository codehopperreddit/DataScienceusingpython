s=input().split()
d=dict()
for w in s:
	if w in d.keys():
		d[w]+=1
	else:
		d[w]=1

for w in d.keys():
	print(w ,d[w], sep=' : ').