InputData = list(map(int,input().split()))
M = InputData[0]
N = InputData[1]
Min = InputData[2]
Max = InputData[3]
Alt = InputData[4]
for i in range(M):
    row = input().split()
    for j in range(N):
        if int(row[j]) >= Min and int(row[j]) <= Max:
            if Alt < 10:
                row[j] = '00' + str(Alt)
            elif Alt >= 10 and Alt < 100:
                row[j] = '0' + str(Alt)
            else: row[j] = str(Alt)
        else:
            if int(row[j]) < 10:
                 row[j] = '00' + row[j]
            elif int(row[j]) >= 10 and int(row[j]) < 100:
                row[j] = '0' + row[j]
    print(' '.join(row))