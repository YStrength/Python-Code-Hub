num = int(input())
i = 0
while num != 1:
    if num % 2 == 0:
        num /= 2
    else:
        num = (3*num + 1) / 2
    i += 1
print(i)