"""Последовательность Фибоначчи определяется так:
F[0] = 0, F[1] = 1, ..., F[n] = F[n-1] + F[n-2].

По данному числу n определите n-е число Фибоначчи F[n].
"""
n = int(input())
idx = 1
prev = 0
curr = 1
a = curr
while idx <= n:
    curr += prev
    prev = a
    a = curr
    idx += 1
print(prev)
