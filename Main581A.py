a,b=map(int,input().split())
cnt2 = min(a,b)
cnt1 = int((max(a,b)-cnt2)/2) 
print(cnt2,cnt1)