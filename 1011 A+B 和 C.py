n = int(input())
abc = []
flag = []
i = 0
while i < n:
    abc = (input().split())
    ABC = list(map(int, abc))
    if (ABC[0] + ABC[1]) > ABC[2]:
        flag.append(0)
    else:
        flag.append(1)
    i += 1
    j = 1
for i in flag:
    if i == 0:
        print("Case #%d: true"%j)
    else:
        print("Case #%d: false"%j)
    j += 1