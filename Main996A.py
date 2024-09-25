n=int(input())
ls=[100,20,10,5,1]
cnt=0
for i in ls:
	if(n==0): break
	else: 
	   cnt += n//i
	   n = n%i
print(cnt)