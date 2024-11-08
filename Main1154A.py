l=[int(x) for x in input().split()]
n = max(l)
l.remove(n)
print(n-l[0],n-l[1],n-l[2])