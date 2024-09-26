n=int(input())
dic={"Tetrahedron":4,
     "Cube":6,
     "Octahedron":8,
     "Dodecahedron":12,
     "Icosahedron":20}
cnt=0
for i in range(n):
	str=input()
	cnt+=dic.get(str,0)
print(cnt)