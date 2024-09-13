str1 = input()
str2 = input()
n1 = int(str1,2)
n2 = int(str2,2)

ans = n1^n2
str3 = bin(ans)[2:].zfill(len(str1))
print(str3)