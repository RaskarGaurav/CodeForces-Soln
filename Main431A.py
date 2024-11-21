l = [int(x) for x in input().split()]
l1 = [int(x) for x in input()]
sm =0
for i in l1:
	sm += l[i-1]
print(sm)

