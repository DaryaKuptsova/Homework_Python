"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""
a = int(input("Введите число A: "))
b = int(input("Введите степень числа A: "))

def degree(a, b):
    if b > 0:
        return degree(a, b - 1) * a
    elif b < 0:
        return degree(a, b + 1) / a
    else:
        return 1

print(degree(a, b))
