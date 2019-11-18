"""Даны две различные клетки шахматной доски,
может ли король попасть с первой клетки на вторую одним ходом."""
x1 = int(input('x1 = '))  # номер строки1
y1 = int(input('y1 = '))  # номер столбца1

x2 = int(input('x2 = '))  # номер строки2
y2 = int(input('y2 = '))  # номер столбца2
#
# if (y1 + 1 == y2
#         or y1 - 1 == y2
#         or y1 == y2
#         or x1 + 1 == x2
#         or x1 - 1 == x2):
#     print("YES")
# else:
#     print("NO")

if x1 == x2 and y1 == y2:
    print("NO")
elif -1 <= x1 - x2 <= 1 and -1 <= y1 - y2 <= 1:
    print("YES")
else:
    print("NO")


"""
  0 1 2  Y
0 y x x
1 x o x
2 x x x
X 

"""