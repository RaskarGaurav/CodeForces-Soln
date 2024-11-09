t = int(input())
while t>0:
	n = input()
	dic ={}
	l=input().split()
	for i in l:
		dic[i] = dic[i]+1 if i in dic else 1
		if 1 in dic.values() and 2 in dic.values(): break 
	for k in dic:
		if dic[k]==1: print(l.index(k)+1)
	t -=1