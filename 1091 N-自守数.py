import math
column = int(input())
num_list = []
num_list += input().split()
for num_temp in num_list:
    num_temp_len = len(num_temp)
    num_temp = int(num_temp)
    for j in range(1,10):
        result = j * math.pow(num_temp,2)
        result = str(int(result))
        result_rear = ''
        for k in range(-num_temp_len,0):
            result_rear = result_rear + result[k]
        # print(result_rear)
        if str(num_temp) == result_rear:
            print(j,result)
            break
        elif j == 9:
            print('No')