s = input()
ans = ""
i=0
while i<len(s):
	if s[i] == ".":
		ans+="0"
		i+=1
	elif s[i] == "-":
		if s[i+1]==".":
			ans+="1"
			i+=2
		else:
			ans+="2"
			i+=2
print(ans)