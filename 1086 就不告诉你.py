Multiplier = []
Multiplier = Multiplier + input().split()
Multiplier = list(map(int,Multiplier))
result = str(Multiplier[0] * Multiplier[1])
result = result[::-1]
result = int(result)
print(result)