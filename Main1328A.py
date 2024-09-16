t = int(input()) 
while t > 0:
    a, b = map(int, input().split()) 
    k = (a // b)
    if(a%b!=0):
        k+=1
    result= k * b - a  
    print(result)
    t -= 1