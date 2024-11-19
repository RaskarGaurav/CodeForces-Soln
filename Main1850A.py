t = int(input())
while t>0:
	l = [int(x) for x in input().split()]
	l.remove(min(l))
	if sum(l)>=10:
		print("YES")
	else:
		print("NO")
	t-=1