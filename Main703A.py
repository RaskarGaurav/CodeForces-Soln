t = int(input())
dic = {1:0,2:0}
while t>0:
	l = [int(x) for x in input().split()]
	if l[0]>l[1]:
		dic[1]+=1
	elif l[0]<l[1]:
		dic[2]+=1
	t-=1
if dic[1]>dic[2]:
	print("Mishka")
elif dic[1]<dic[2]:
	print("Chris")
else:
	print("Friendship is magic!^^")