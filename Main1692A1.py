t = int(input())
while t>0:
	l = [int(x) for x in input().split()]
	print((l[0]<l[1])+(l[0]<l[2])+(l[0]<l[3]))
	t -=1