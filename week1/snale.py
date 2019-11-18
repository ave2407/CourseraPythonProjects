""" Улитка ползет по вертикальному шесту.
 На какой день улитка доползет до вершины шеста?"""
import math

height = int(input())
speed_up = int(input())
speed_down = int(input())

days = math.ceil((height - speed_up) / (speed_up - speed_down)) + 1
print(days)
