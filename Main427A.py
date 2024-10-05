input()
ls=[int(x) for x in input().split()]
pol=0
unt=0
for i in ls:
    if i>=0:
        pol+=i
    else:
        if pol<1:
            unt+=1
        else:
            pol-=1
print(unt)
