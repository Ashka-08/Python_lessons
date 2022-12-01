# Напишите программу, которая принимает на вход число N и выдаёт 
# последовательность из N членов.
# Пример:
# - Для N = 5: 1, -3, 9, -27, 81

number = int(input('Введите число: '))
for i in range(number):
    print(((-3) ** i), end=", ")

# number = int(input('Введите число: '))
# for i in range(number-1):
#     print(((-3) ** i), end=", ")
# print((-3) ** (number-1))
