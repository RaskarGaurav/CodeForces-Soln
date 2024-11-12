t = int(input())
while t>0:
    l = [int(x) for x in input().split()]
    print(sorted(l)[1])
    t-=1