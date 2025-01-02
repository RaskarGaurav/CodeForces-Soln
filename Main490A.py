n = int(input())
l = [int(x) for x in input().split()]
dic={1:0,2:0,3:0}
for i in l:
	dic[i] = dic[i]+1
k = min(dic.values())
lst = []
i =0
l1=[]
while len(lst)!=k*3:
	if len(l1)==3: l1=[]
	if l[i] not in l1 and i+1 not in lst:
		l1.append(l[i])
		lst.append(i+1)
	i+=1
	if i==n:
		i=0
print(k)
for i in range(0,len(lst),3):
	print(lst[i],lst[i+1],lst[i+2])