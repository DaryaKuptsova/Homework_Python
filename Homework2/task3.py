"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Введите число N:"))
degree = 0
while degree <= N:
    number = 2 ** degree
    print(f"2 в степени {degree} = {number}.")
    degree += 1
"""
N = int(input("Введите число N:"))
degree = 0
while 2**degree <= N:
    number = 2 ** degree
    print(f"2 в степени {degree} = {number}.")
    degree += 1
