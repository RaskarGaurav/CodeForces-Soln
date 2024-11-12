t = int(input())
while t>0:
	n = int(input())
	if 1900<= n:
		print("Division 1")
	elif 1600<=n<=1899:
		print("Division 2")
	elif 1400<=n<=1599:
		print("Division 3")
	else:
		print("Division 4")
	t -= 1