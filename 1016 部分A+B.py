Box =[]
Box =(input().split())
A = Box[0]
DA = Box[1]
B = Box[2]
DB = Box[3]
PA = ''
for i in A:
    if i == DA:
        PA += DA
if PA == '':
    PA = '0'
PB = ''
for j in B:
    if j == DB:
        PB += DB
if PB == '':
    PB = '0'
print(int(PA)+int(PB))