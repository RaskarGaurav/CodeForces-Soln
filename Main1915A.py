t = int(input())
while t>0:
	l=[x for x in input().split()]
	if l[0]==l[1]:
		print(l[2])
	elif l[0]==l[2]:
		print(l[1])
	else:
		print(l[0])
	t -=1