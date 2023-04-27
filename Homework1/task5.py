"""
ДОПОЛНИТЕЛЬНЫЕ:
Задача 2: Найдите сумму цифр трехзначного числа.

Пример:

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""

print("Введите трехзначное число: ")
num = int(input())
firstN = num % 10
secondN = num % 100 // 10
thirdN = num // 100
amount = firstN + secondN + thirdN
print(f"Сумма цифр трехзначного числа = {amount}.")