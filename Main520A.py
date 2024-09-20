input()
str=input()
str=str.lower()
st=set(str)
st1={chr(x) for x in range(97,123)}
print("YES" if(st==st1) else "NO")