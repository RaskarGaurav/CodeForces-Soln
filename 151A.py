n, k, l, c, d, p, nl, np = map(int,input().split())
cnt= min((k*l)/(n*nl),(c*d)/n,p/(n*np))
print(int(cnt))