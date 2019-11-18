"""Определите, можно ли таким образом отломить от шоколадки часть
 состоящую ровно из k долек."""
m = int(input())
n = int(input())
k = int(input())
if n <= k <= m * n \
    and k % m == 0 \
        or m <= k <= m * n \
        and k % n == 0:
    print("YES")
else:
    print("NO")
