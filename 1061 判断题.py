InputData = input().split()
students = int(InputData[0])
questions = int(InputData[1])
value = input().split()
Answer = input().split()

for i in range(students):
    Sum = 0
    answer = input().split()
    for j in range(questions):
        if answer[j] == Answer[j]:
            Sum += int(value[j])
    print(Sum)