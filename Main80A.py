def checkPrime(n):
	i=2
	while i*i<=n:
		if n%i==0: return False
		i+=1
	else:
		return True
		
n,m = map(int,input().split())
for  k in range(n+1,m):
	if checkPrime(k):
		print("NO")
		break
else:
	if checkPrime(m):
		print("YES")
	else:
		print("NO")