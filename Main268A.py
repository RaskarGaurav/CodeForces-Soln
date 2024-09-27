n=int(input())
ls1=[]
ls2=[]
for i in range(n):
	ls=[int(x) for x in input().split()]
	ls1.append(ls[0])
	ls2.append(ls[1])
cnt=0
for i in ls1:
	for j in ls2:
	    if(i==j): cnt+=1 
print(cnt)