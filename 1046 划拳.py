n = int(input())
Box = []
A = 0
B = 0
for i in range(n):
    Box = input().split()
    Box = list(map(int,Box))
    if Box[0] + Box [2] == Box[1] and Box[0] + Box [2] != Box[3]:
        B += 1
    elif Box[0] + Box[2] != Box[1] and Box[0] + Box[2] == Box[3]:
        A += 1
print("%d %d"%(A,B))