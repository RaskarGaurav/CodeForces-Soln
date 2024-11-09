t = int(input())
while t>0:
	l = [int(x) for x in input().split()]
	k = {i for i in l if i>l[0]}
	print(len(k))
	t -=1