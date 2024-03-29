# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141.    10^(-1) ≤ d ≤10^(-10)

# v1 ответ 3.142
from math import pi
n =  int(input("Введите число для точности числа Пи: "))
print(f'Число Пи с заданной точностью {n} равно {round(pi, n)}')

# v2 ответ 3.142
import math
num = input('Введите степень округления в формате 0.01: ')
num = num[2:len(num)]
print(f'Число Пи с заданной точностью равно {round(math.pi,len(num))}')

# v3, ответ рандомный с точностью 0.001
import random
b = 1e-1
c = 1e-10
d = random.randint(1,9)
a = round(random.uniform(b,c) + d, 3) 
#random.uniform() используется для генерации числа с плавающей запятой в пределах 
# заданного промежутка
print(a)

# v4 ответ 3.142
p = 3.141592654 
# число пи с точностью 1e-10 или 10^(-10)
print(format(p, '.3f'))
# округляет по правилам математики, так же как и round(p, 3)

# v5 ответ 3.141 float
x = str(p)
y = x[:5]
j = float(y)
print(j)

print(float(str(pi)[:5]))

# v6
m = int(input('введите число нужной точности 1#= '))
pi_target = 0
for i in range(1, 1000000):
    pi_target += 4 * ((-1) ** (i + 1)) / (2 * i - 1)
    # матем.формула для рассчета числа пи
print(str(pi_target)[:m + 2])