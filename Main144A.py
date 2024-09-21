n=int(input())
ls=[int(x) for x in input().split()]
mx=ls.index(max(ls))
ls.reverse()
mn=n-1-ls.index(min(ls))

a = (mx+n-mn-1) if(mx<mn) else (mx+n-mn-2)
print(a)