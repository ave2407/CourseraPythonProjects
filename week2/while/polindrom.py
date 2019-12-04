"""Назовем число палиндромом, если оно не меняется при перестановке его цифр
 в обратном порядке. Напишите программу, которая по заданному числу K
 выводит количество натуральных палиндромов, не превосходящих K."""

k = int(input())

count_poli = 0

current_number = 1
while current_number <= k:
    # Check if this number is poli
    number = current_number
    reverse = 0
    while number > 0:
        last_digit = number % 10
        reverse = 10 * reverse + last_digit
        number //= 10

    if current_number == reverse:
        count_poli += 1

    current_number += 1

print(count_poli)
