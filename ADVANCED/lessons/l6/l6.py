# про импорт
import sys

print(sys)
print(sys.builtin_module_names)
print(*sys.path, sep='\n')


import random

print(random.randint(1, 6))


# из модуля импорт
from sys import builtin_module_names, path

print(builtin_module_names)
print(*path, sep='\n')


# из модуля импорт с псевдонимом
import random as rnd
from sys import builtin_module_names as bmn, path as p

print(bmn)
print(*p, sep='\n')
print(rnd.randint(1, 6))
# print(path) # NameError: name 'path' is not defined
# print(sys.path) # NameError: name 'sys' is not defined


# из модуля импорт всего из переменной __all__
from super_module import *

SIZE = 49.5
print(f'{SIZE = }\n{result = }')
# print(f'{z = }') # NameError: name 'z' is not defined
print(f'{_secret = }') 
print(f'{func(100, 200) = }')
# print(f'{randint(10, 20) = }') # NameError: name 'randint' is not defined

def func(a: int, b: int) -> int:
    return a + b

print(f'{func(100, 200) = }')


# импорт собственного модуля в этой же директории
import base_math

x = base_math.mul # Плохой приём передача имени в другую переменную
y = base_math._START_MULT # Очень плохой приём, обращение к защищённой или приватной переменной
z = base_math.sub(73, 42)
print(x(2, 3))
print(y)
print(z)


# импорт пакета 
import mathematical
print(mathematical.__all__)
# x = mathematical.base_math.div(12, 5) AttributeError: module 'mathematical' has no attribute 'base_math'


# импорт модулей из пакета
from mathematical import base_math as bm
from mathematical.advanced_math import exp

x = bm.div(12, 5)
z = exp(2, 3)


# модуль рандом
import random as rnd

START = -100
STOP = 1_000
STEP = 10
data = [2, 4, 6, 8, 42, 73]

print(rnd.random()) #0.808786757561689
rnd.seed(42)
state = rnd.getstate()
print(rnd.random()) #0.6394267984578837
rnd.setstate(state)
print(rnd.random()) #0.6394267984578837
print(rnd.randint(START, STOP)) #-49
print(rnd.uniform(START, STOP)) #715.7055497358161
print(rnd.choice(data)) # 4
print(rnd.randrange(START, STOP, STEP)) #180
print(data) #[2, 4, 6, 8, 42, 73]
rnd.shuffle(data) 
print(data) #[8, 73, 6, 42, 2, 4]
print(rnd.sample(data, 2)) #[8, 4]
print(rnd.sample(data, 2, counts=[1, 1, 1, 1, 1, 100])) #[4, 4]