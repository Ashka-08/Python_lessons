# Напишите программу, которая принимает на вход вещественное число и показывает 
# сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = input('Введите число: ')
s = 0
for i in n:
    if i.isdigit():
        s += int(i)
print(f"Сумма цифр числа {n} равна:", s)

# 2 способ
# n = input('Введите число: ')
# s = 0
# for i in n:
#     if i != '.':
#         s += int(i)
# print(f"Сумма цифр числа {n} равна:", s)