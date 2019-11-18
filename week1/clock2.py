"""выводит кол-во часов, митун, секупд"""

N = int(input())
hours = N // 3600 % 24
minutes = N % 3600 // 60
sec = N % 60
print(hours, end=':')
if minutes < 10:
    print(0, minutes, end=':', sep='')
else:
    print(minutes, end=':')
if sec < 10:
    print(0,  sec, end='', sep='')
else:
    print(sec)

# print()
# res = '{}:{:02d}:{:02d}'.format(hours, minutes, sec)
# res = f'{hours}:{minutes:02d}:{sec:02d}'
# print(res)
