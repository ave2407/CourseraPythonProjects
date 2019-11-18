"""Решить в целых числах уравнение: (ax+b) / (cx+d) = 0"""
print("Решу уравнение: '(ax+b) / (cx+d) = 0' в целых числах")
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('d = '))

answer = 'NO'

if a == 0 and b == 0:
    answer = 'INF'
    if c == d == 0:
        answer = 'NO'
else:
    # a != 0, b != 0
    x = - b // a

    if c * x + d == 0:
        answer = 'NO'
    elif a * x + b == 0:
        answer = str(x)

print(answer)
