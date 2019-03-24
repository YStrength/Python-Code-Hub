InputNum =input().split()
n = int(InputNum.pop(0))
Box = set([])
for i in range(n):
    for j in range(n):
        if i != j:
           Box.add(InputNum[i] + InputNum[j])
Box = list(map(int,Box))
print(sum(Box))