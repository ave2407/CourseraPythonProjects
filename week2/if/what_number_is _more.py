''' Программа должна вывести число
"1", если первое число больше второго, число
"2", если второе больше первого или число
"0", если они равны.'''
a = int(input())
b = int(input())
if a > b:
    print(1)
elif b > a:
    print(2)
else:
    print(0)
