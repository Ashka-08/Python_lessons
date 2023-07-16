# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# Отправлено на проверку
num = list(map(float, input("Введите числа через пробел: ").split()))
max_min = []
for i in range(len(num)):
    if num[i]%1 != 0:
        max_min.append(num[i]%1)
result = max(max_min) - min(max_min)
print(f'Разница между максимальной и минимальной дробной части = {result:.2f}')

# еще одно решение
import random
a = []
l = 5
for i in range(l):
    k = round(random.uniform(1.0, 10.5), 2) 
# random.uniform() используется для генерации числа с плавающей запятой 
# в пределах заданного промежутка
    a.append(k)
print(f"Original list: {a}")
b = []
for i in range(l):
    k = a[i] - (a[i] // 1)
    b.append(round(k, 2))
if min(b) == 0:
    b.remove(0)
print(f"The difference max - min = {max(b) - min(b)}")

# Функция min() возвращает минимальное значение элемента из итерируемого объекта или наименьшее из двух или более переданных позиционных аргументов.
# min(iterable, *[, key, default])
# min(arg1, arg2, *args[, key])
# Параметры:
# iterable - итерируемый объект,
# key - функция сортировки (смотри list.sort()),
# default - значение по умолчанию, если итерируемый объект окажется пустым,
# arg1...argN - позиционный аргумент,
# *args - список позиционных аргументов.