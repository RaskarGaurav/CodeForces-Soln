t=int(input())
for i in range(t):
	str=input()
	cnt=0
	print()
	for x in str:
		cnt= cnt+1 if(x!='0') else cnt
	print(cnt)
	for y in range(len(str)):
		if(str[y]!='0'):
			print(str[y]+'0'*(len(str)-y-1),end=" ")