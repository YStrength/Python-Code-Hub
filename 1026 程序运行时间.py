n = input().split()
T = (int(n[1]) - int(n[0])) / 100
hh = int(T // 3600)
mm = int((T - hh * 3600) // 60)
ss =T - hh * 3600 - mm * 60
# if ss - round(ss) > 0:
#     ss += 1
ss = round(ss)
HH = str(hh)
MM = str(mm)
SS = str(ss)
if hh < 10:
    HH = '0' + HH
if mm < 10:
    MM = '0' + MM
if ss < 10:
    SS = '0' + SS
print("%s:%s:%s"%(HH,MM,SS))