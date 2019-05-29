#a=[[1,2,3],[4,5,6],[7,8,9]]	
r, c=int(input().split)
for i in range(0,r):
	x=
r=len(a)
c=len(a[0])
sumr=0
sumc=0	
for i in range(0,r):
	sumr=0
	sumc=0
	for j in range(0,c):
		sumr+=a[i][j]
		sumc+=a[j][i]
		print(sumr, sumc, sep=', ')
		print('%.2f '%(sumr/3), '%.2f'%(sumc/3), sep=', ')
		
		

		

