n=int(input())
l1=[int(x) for x in input().split()]
l2=[int(k) for k in input().split()]
#l1.append(0)
#l2.append(0)
l=l1[1:]+l2[1:]
st1=set(l)
st2={i for i in range(n+1)}
if(st1==st2):
	print("I become the guy.")
else:
	print("Oh, my keyboard!")