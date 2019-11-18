hour1 = int(input())
min1 = int(input())
sec1 = int(input())
hour2 = int(input())
min2 = int(input())
sec2 = int(input())
res = (hour1 - hour2) * 3600 + (min1 - min2) * 60 + sec1 - sec2
if res < 0:
    print(-res)
else:
    print(res)
