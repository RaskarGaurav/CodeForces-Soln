dic={}
l=[x for x in input().split()]
for i in l:
	if(i in dic):
		dic[i] = dic[i]+1
	else:
		dic[i] = 1
if(len(dic)==2 and max(dic.values())==2):
    print(max(dic.values()))
else:
    print(max(dic.values())-1)