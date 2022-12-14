# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# отправлено на проверку
a = int(input('Введите число: '))
b = ''
while a > 0:
    b = str(a % 2) + b
    a = a // 2
print(b)

# еще одно решение
import random
a = random.randint(0, 100)
b = a
# print(a)
# print(bin(a)) это вывод через двоичную систему
c = ""
while b > 0:
    c = str(b % 2) + c
b = b // 2
print(f"{a} -> {c}")

# еще одно решение
n = int(input("Введите число:\n"))
print(f'{n} -> {bin(n)}')