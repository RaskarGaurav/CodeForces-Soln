t = int(input())
while t>0:
    l = [int(x) for x in input().split()]
    if l[0]+l[1] == l[-1]: print("+")
    else: print("-")
    t -=1