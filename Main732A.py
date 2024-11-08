l =[x for x in input().split()]
k = int(l[0][-1])
r = int(l[-1])

for i in range(1,11):
	n = int(str(k*i)[-1])
	if n==r or n==0:
		print(i)
		break