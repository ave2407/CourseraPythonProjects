"""Определите значение второго по величине элемента
в этой последовательности, то есть элемента,
который будет наибольшим, если из последовательности
удалить одно вхождение наибольшего элемента."""
# Первое" становится "вторым", если "новое" больше "первого"

now = int(input())
maximum = now
maximum2 = None
while now != 0:
    now = int(input())
    if now >= maximum:
        maximum2 = maximum
        maximum = now
    elif maximum2 is None or maximum2 < now < maximum:
        maximum2 = now
print(maximum2)
