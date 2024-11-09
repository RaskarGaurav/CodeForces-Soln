input()
l = [int(x) for x in input().split()]
turn = True
s = 0
d = 0
while l:
	tup = (l[0],l[-1])
	k = max(tup)
	l.remove(k)
	if turn:
		s +=k
		turn = False
	elif not turn:
		d +=k
		turn = True
print(s,d)		