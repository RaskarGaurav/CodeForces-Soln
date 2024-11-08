t = int(input())
while t>0:
	n = input()
	l = {int(x) for x in input().split()}
	for i in range(min(l),max(l)):
		if i not in l:
			print("NO")
			break
	else:
		print("YES")
	t -= 1 