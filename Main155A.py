n = int(input())
l = [int(x) for x in input().split()]
cnt = 0
max = l[0]
min = l[0]
for i in l:
	if i>max:
		max = i
		cnt+=1
	elif i<min:
		min = i
		cnt+=1
print(cnt)
