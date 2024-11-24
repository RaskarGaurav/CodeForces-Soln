t = int(input())
while t>0:
	d,r,n = map(int,input().split())
	q = n//d
	k = d*q+r
	if k>n:
	    k =d*(q-1)+r
	print(k)
	t-=1