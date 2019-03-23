import math
Box = input().split()
Box = list(map(float,Box))
A = Box[0] * Box[2] * math.cos(Box[1]+Box[3])
if A >= -0.005 and A < 0:
    A = 0.00
B = Box[0] * Box[2] * math.sin(Box[1]+Box[3])
if B > -0.005 and B < 0:
    B = 0.00
print("{:.2f}{:+.2f}i".format(A,B))