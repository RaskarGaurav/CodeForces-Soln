t = int(input())
while t>0:
	s = input()
	s1= s[0]
	for i in range(len(s)):
		if i%2!=0:
			s1 += s[i]
	print(s1)
	t-=1