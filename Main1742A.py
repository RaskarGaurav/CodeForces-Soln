t = int(input())
while t>0:
	l = [int(x) for x in input().split()]
	n = max(l)
	l.remove(n)
	if sum(l)==n:
		print("YES")
	else:
		print("NO")
	t-=1