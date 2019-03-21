ZM = {'0':'1', '1':'0', '2':'X', '3':'9', '4':'8', '5':'7', '6':'6', '7':'5', '8':'4', '9':'3', '10':'2'}
count = 0
def WeightAdd (ID,weight=[7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]):
    ID = map(int,ID)
    i = 0
    Sum = 0
    for a in ID:
        Sum += a * weight[i]
        i += 1
    return Sum

n = int(input())
N = n
while n > 0:
    ID = input()
    if ID[:17].isdigit() == False:
        print(ID)
        n -= 1
        continue
    else:
        Sum = WeightAdd(ID[:17])
        Check = Sum % 11
        check = str(ID[-1])
        if check != ZM[str(Check)]:
            print(ID)
        else:
            count += 1
        n -= 1
if count == N:
    print("All passed")