''' стоимость булочки в р и коп'''
A = int(input())
B = int(input())
N = int(input())
rub = B * N // 100
print(A * N + rub)
print(B * N % 100)
