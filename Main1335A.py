t=int(input())
for i in range(t):
	n=int(input())
	if(n!=1): print(n//2 if(n%2!=0) else n//2-1)
	else: print(0)