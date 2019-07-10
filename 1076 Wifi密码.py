N = int(input())
i = 0
answer = []
while i < N:
    answer = answer + input().split()
    i += 1
len_answer = len(answer)
wifi = []
for j in range(len_answer):
    str_temp = str(answer[j])
    if str_temp[0] == 'A' and str_temp[-1] == 'T':
        wifi.append(1)
    elif str_temp[0] == 'B' and str_temp[-1] == 'T':
        wifi.append(2)
    elif str_temp[0] == 'C' and str_temp[-1] == 'T':
        wifi.append(3)
    elif str_temp[0] == 'D' and str_temp[-1] == 'T':
        wifi.append(4)
for k in range(N):
    print(wifi[k],end='')