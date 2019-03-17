integer = input()
k = []
for i in range(10):
    k.append(0)
for i in range(10):
    for a in integer:
        if a == str(i):
            k[i] += 1
for b in range(10):
    if k[b] == 0:
        continue
    else:
        print("{}:{}".format(b,k[b]))