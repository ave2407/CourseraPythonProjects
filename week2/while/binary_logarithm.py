"""По данному натуральному числу N выведите такое наименьшее целое число k,
 что 2ᵏ≥N."""
n = int(input())
i = 1
k = 0
while n / i > 1:
    i *= 2
    k += 1

print(k)
