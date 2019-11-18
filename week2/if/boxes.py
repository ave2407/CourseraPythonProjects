"""выяснить может ли одна коробка поместитьься в другую"""
# стороны первой коробки
a0 = int(input())
b0 = int(input())
c0 = int(input())
# стороны второй коробки
a1 = int(input())
b1 = int(input())
c1 = int(input())

# Find two minimum dimensions of the first box
max_0 = max(a0, c0, b0)
min_0 = min(a0, c0, b0)
if min_0 <= b0 <= max_0:
    mid_0 = b0
elif min_0 <= c0 <= max_0:
    mid_0 = c0
else:
    mid_0 = a0

# Find two minimum dimensions of the second box
max_1 = max(a1, c1, b1)
min_1 = min(a1, c1, b1)
if min_1 <= b1 <= max_1:
    mid_1 = b1
elif min_1 <= c1 <= max_1:
    mid_1 = c1
else:
    mid_1 = a1

if min_0 == min_1 \
        and mid_0 == mid_1 \
        and max_0 == max_1:
    print("Boxes are equal")

elif min_0 <= min_1 \
        and mid_0 <= mid_1 \
        and max_0 <= max_1:
    print("The first box is smaller than the second one")

elif min_0 >= min_1 \
        and mid_0 >= mid_1 \
        and max_0 >= max_1:
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")
