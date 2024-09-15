n=int(input())
luv="I love "
het="I hate "
tht="that "
str=""
for i in range(n):
	if(i%2==0):
		str=str+het+tht
	else:
		str=str+luv+tht

k=str.rfind("that")
str=str[:k]
print(str+"it")