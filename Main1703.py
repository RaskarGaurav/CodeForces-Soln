import re
t = int(input())
while t>0:
	st = input()
	x = re.search(r"yes",st,re.I)
	if x: print("YES")
	else: print("NO")
	t -= 1