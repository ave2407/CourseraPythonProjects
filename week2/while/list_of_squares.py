# n = int(input())
# # i = 1
#
# while True:
#     square = i ** 2
#     if square <= n:
#         print(square)
#     else:
#         break
#     i += 1
"""По данному числу N распечатайте все целые степени двойки,
 не превосходящие N,
 в порядке возрастания.Операцией возведения в степень пользоваться нельзя!"""

n = int(input())
i = 1

while i <= n:
    print(i)
    i *= 2
