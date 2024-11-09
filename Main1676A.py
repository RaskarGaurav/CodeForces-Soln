t = int(input())
while t>0:
	l = [int(x) for x in input()]
	if l[0]+l[1]+l[2]==l[-1]+l[-2]+l[-3]:
		print("YES")
	else:
		print("NO")
	t -=1