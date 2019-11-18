"""выяснить является ли число симметричным"""
n = int(input())
s = str(n)
z = '0' * (4 - len(s))
filled = z + s

if filled[0] == filled[3] and filled[1] == filled[2]:
    print(1)  # симметричное
else:
    print(0)  # не симметричное
