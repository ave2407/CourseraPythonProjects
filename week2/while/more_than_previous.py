"""Определите, сколько элементов этой последовательности
больше предыдущего элемента."""
a = int(input())
i = 0
j = a
while a != 0:
    a = int(input())
    if a > j:
        i += 1
    j = a
print(i)