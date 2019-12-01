"""Определите количество элементов этой последовательности,
 которые равны ее наибольшему элементу."""

now = int(input())
maximum = now
i = 1
while now != 0:
    now = int(input())
    if now > maximum:
        maximum = now
        i = 1
    elif now == maximum:
        i += 1
print(i)
