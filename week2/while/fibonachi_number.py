"""Дано натуральное число A.
Определите, каким по счету числом Фибоначчи оно является,
то есть выведите такое число n, что F[n]=A."""
n = int(input())
idx = 2
prev = 1
curr = 1
a = curr
while curr < n:
    curr += prev
    prev = a
    a = curr
    idx += 1
if curr == n:
    print(idx)
else:
    print(-1)
