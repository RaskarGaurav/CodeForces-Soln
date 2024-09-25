str=input()
if(str=="{}"):
    print("0")
else:
    st=set(str[1:-1].split(", "))
    print(len(st))
