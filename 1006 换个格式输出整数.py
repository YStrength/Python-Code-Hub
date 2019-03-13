def PrintStr(length,integer , switch=0):
    if length == 3:
        if switch == 0:
            for a in range(integer):
                print(a+1,end='')
        elif switch == 1:
            for a in range(integer):
                print("S",end='')
        else:
            for a in range(integer):
                print("B",end='')
    elif length == 2:
        if switch == 0:
            for a in range(integer):
                print(a+1,end='')
        else:
            for a in range(integer):
                print("S",end='')
    else:
        for a in range(integer):
            print(a + 1, end='')
integer = int(input())
L = len(str(integer))
box = []
for i in range(L):
    box.append(integer % 10)
    integer /= 10
    integer = int(integer)
box = box[::-1]
k = L - 1
j = 0
while k >= 0 and j<= L:
    PrintStr(L, box[j], k)
    j += 1
    k -= 1