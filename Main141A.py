str=input()
str1=input()
str2=input()
str=str+str1
l=[x for x in str]
l1=[i for i in str2]
l.sort()
l1.sort()
print('YES' if(l==l1) else 'NO')