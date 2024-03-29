# Напишите программу, которая вычисляет площадь круга и 
# длину окружности по введённому диаметру.
# * Диаметр не превышает 1000 у.е.
# * Точность вычислений должна составлять не менее 42 знаков после запятой.

from decimal import Decimal, getcontext
from math import pi

d = float(input('Введите диаметр круга: '))
getcontext().prec = 42

print('Площадь круга:', Decimal(pi*(d/2**2)))
print('Длина окружности:', Decimal(pi*d))

# print(0.1 + 0.1 + 0.1 - 0.3) #5.551115123125783e-17
# print(round((0.1 + 0.1 + 0.1 - 0.3), 2)) #0.0