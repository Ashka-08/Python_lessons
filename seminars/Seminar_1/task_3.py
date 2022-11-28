# Task 
# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них

# a = int(input('Введите 1 число: '))
# b = int(input('Введите 2 число: '))
# c = int(input('Введите 3 число: '))
# d = int(input('Введите 3 число: '))
# e = int(input('Введите 5 число: '))

# list = [a, b, c, d, e]
# max = a
# for i in list:
#     if max < i:
#         max = i
# print(max)

lst = []
for i in range(5):
    x = int(input(f'Введите число {i}: '))
    lst.append(x)
print(lst)
max = 0
for i in lst:
    if max < i:
        max = i
print(f'Максимальное число номер {i} = {max}')