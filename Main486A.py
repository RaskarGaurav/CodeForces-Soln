n = int(input())
odd = (n**2)//4 if (n%2==0) else (n//2 + 1)**2
even = (n//2)*(n//2 +1) 
print(even-odd)