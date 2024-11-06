n,k = map(int,input().split())
rem = 240-k
t = 0
for i in range(1,n+1):
	t = t+ 5*i
	if t>rem:
	    print(i-1)
	    break
else:
    print(i)
