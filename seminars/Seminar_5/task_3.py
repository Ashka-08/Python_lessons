# Найти НОД двух чисел (наибольший общий делитель)

import random
a = random.randint(33, 99)
b = random.randint(33, 99)
c = [a, b]
print(c)
while max(a, b) % min(a, b) != 0:
    if a > b:
        a = a % b
    elif a < b:
        b = b % a
print(min(a, b))

# a = int(input('Введите а: '))
# b = int(input('Введите в: '))
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a

# print(a)