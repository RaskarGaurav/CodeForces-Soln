t = int(input())
while t>0:
	a,b=input().split()
	print(b[0]+a[1:3],a[0]+b[1:3])
	t-=1