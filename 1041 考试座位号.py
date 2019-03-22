class ticket(object):
    def __init__(self,AdmissionNum, TestNum, ExamNum):
        self.AdmissionNum = AdmissionNum
        self.TestNum = TestNum
        self.ExamNum = ExamNum
    def print(self):
        print('%s'%(self.AdmissionNum),end=' ')
        print('%s'%(self.ExamNum))

n = int(input())
person = []
for i in range(n):
    Box = input().split()
    person.append(ticket(Box[0],Box[1],Box[2]))
m = int(input())
a = input().split()
for j in a:
    for k in range(n):
        if j == person[k].TestNum:
            person[k].print()