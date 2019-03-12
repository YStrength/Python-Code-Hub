pinyin ={0:'ling', 1:'yi', 2:'er', 3:'san', 4:'si',
         5:'wu', 6:'liu', 7:'qi', 8:'ba', 9:'jiu', 10:'shi'}
Num = input()
Sum = 0
for i in Num:
    Sum += int(i)
n = len(str(Sum))
box = []
for j in range(n):
    temp = Sum % 10
    box.append(temp)
    Sum /= 10
    Sum = int(Sum)
box = box[::-1]
k = 1
for a in box:
    print(pinyin[a],end='')
    if k!= n:
        print(' ',end='')
        k += 1