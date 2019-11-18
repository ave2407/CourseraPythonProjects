"""определить цвет клетки на шахматной доске"""
x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
if (x + y) % 2 == 0 \
        and (x1 + y1) % 2 == 0 \
        or (x + y) % 2 == 1 \
        and (x1 + y1) % 2 == 1:
    print("YES")
else:
    print("NO")
