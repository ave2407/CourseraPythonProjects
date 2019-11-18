"""....."""
brick_height = int(input('brick_height = '))
brick_width = int(input('brick_width = '))
brick_depth = int(input('brick_depth = '))
hole_height = int(input('hole_height = '))
hole_width = int(input('hole_width = '))

# Find two minimum dimensions of the hole
hole_min_0 = min(hole_width, hole_height)
hole_min_1 = max(hole_width, hole_height)

# Find two minimum dimensions of the brick
brick_max = max(brick_depth, brick_width, brick_height)
if brick_height == brick_max:
    x = brick_width
    y = brick_depth
elif brick_width == brick_max:
    x = brick_height
    y = brick_depth
else:
    x = brick_width
    y = brick_height
brick_min_0 = min(x, y)
brick_min_1 = max(x, y)

# Check if the brick can be passed into the hole
if brick_min_0 <= hole_min_0 and brick_min_1 <= hole_min_1:
    print("YES")
else:
    print("NO")


# brick_params = sorted([brick_width, brick_height, brick_depth])  # 2, 3, 4
# hole_params = sorted([hole_height, hole_width])  # 3, 2
#
# if brick_params[0] <= hole_params[0] and brick_params[1] <= hole_params[1]:
#     print('YES')
# else:
#     print('NO')
