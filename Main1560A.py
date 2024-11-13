t = int(input())
l  = []
for i in range(1,1667):
    if i%3!=0 and i%10!=3:
        l.append(i)
while t>0:
    n =int(input())
    print(l[n-1])
    t-=1