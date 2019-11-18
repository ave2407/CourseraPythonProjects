""" закончите фразу “На лугу пасется...” """
n = int(input())
cow = str(None)
a = n % 10
if a == 0 or a >= 5 or 10 < n < 20:
    cow = "korov"
    print(n, cow)
elif a == 1:
    cow = "korova"
    print(n, cow)
else:
    cow = "korovy"
    print(n, cow)
