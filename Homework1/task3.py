"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
print ("Введите целое положительное число n: ")
n = input()
sum = int(n) + int(str(n+n)) + int(str(n+n+n))
print (f"n + nn + nnn = {sum}")