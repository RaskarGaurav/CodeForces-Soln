import math
t = int(input())
while t>0:
	l = [int(x) for x in input().split()]
	print(math.ceil(abs(l[0]-l[1])/10))
	t -= 1