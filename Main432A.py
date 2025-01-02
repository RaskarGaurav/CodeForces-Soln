n,k = map(int,input().split())
l =[x for x in input().split() if int(x)+k <=5]
print(len(l)//3)
