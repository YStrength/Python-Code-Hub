length,symbol = input().split()
length = int(length)
if length % 2 != 0:
    row = length // 2 + 1
else:
    row = length // 2
for i in range(row):
    if i == 0 or i == row-1:
        print(symbol * length)
    else:
        print("%s%s%s"%(symbol, ' '*(length-2), symbol))

# a = input().split()
# a[0] = int(a[0])
# if a[0]%2!=0:
#     k = a[0]//2+1
# else:
#     k = a[0]//2
# for i in range(a[0]-1):
#     print(a[1],end="")
# print(a[1])
# for i in range(k-2):
#     print("%s%s%s"%(a[1]," "*(a[0]-2),a[1]))
# for i in range(a[0]):
#     print(a[1],end="")