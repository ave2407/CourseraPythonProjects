"""сколько чисел совпадает"""
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print(3)
elif a == c or a == b or c == b:
    print(2)
elif a != b != c:
    print(0)
