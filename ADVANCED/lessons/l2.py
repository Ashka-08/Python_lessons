a = 42
print(type(a), id(a))
print(isinstance(a, int))

a = 'hello world'
print(type(a), id(a))

a = 42.0 * 3.14 / 2.72
print(type(a), id(a))

a = True
print(type(a), id(a))
print(isinstance(a, int))

a = 3.14
print(isinstance(a, (int, float, complex)))

num = 2 + 2 * 2
digit = 36 / 6
print(num, ',', digit)
print(num == digit)
print(num is digit)

txt = 'Hello world!'
print(txt, id(txt))
txt = txt.replace(' ', '_')
print(txt, id(txt))

x = 42
y = 'text'
z = 3.1415
print(hash(x), hash(y), hash(z))
my_list = [x, y, z]
print(hash(my_list)) # получим ошибку, т.к. list изменяемый

# Напишите небольшую программу, которая запрашивает у пользователя любой текст
# и выводит о нём следующую информацию:
# ✔ тип объекта,
# ✔ адрес объекта в оперативной памяти,
# ✔ хеш объекта

something = input('Введите что-либо: ')
print(type(something))
print(id(something))
print(hash(something))

# Аннотация типов
a: int | float = 42
b: float = float(input('Введи число: '))
a = a / b

def my_func(data: list[int, float]) -> float:
    res = sum(data) / len(data)
    return res

print(my_func([2, 5.5, 15, 8.0, 13.74]))

print("Hello world!".__doc__)

print("Hello world!".upper())
print("Hello world!".count('l'))

txt = 'hi'
print(dir(txt))

help(str)
help()

x = int("42")
y = int(3.1415)
z = int("hello", base=30)
print(x, y, z, sep='\n')

import sys
STEP = 2 ** 16
num = 1
for _ in range(30):
    print(sys.getsizeof(num), num)
    num *= STEP

num = 7_901_123_456_789
print(num)

num = 2 ** 16 - 1
b = bin(num)
o = oct(num)
h = hex(num)
print(b, o, h)

print(0.1 + 0.2)
pi = 3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375
print(pi)

text = 'Привет.' 'Как ты, друг?' 'Рад тебя видеть.'
print(text)

empty_str = ''
en_str = 'Text'
ru_str = 'Текст'
unicode_str = '😀😍😉🙃'
print(empty_str.__sizeof__())
print(en_str.__sizeof__())
print(ru_str.__sizeof__())
print(unicode_str.__sizeof__())

# Напишите небольшую программу, которая запрашивает у пользователя текст. Если
# текст можно привести к целому числу, выведите его двоичное, восьмиричное и
# шестнадцатиричное представление. А если преобразование к целому невозможно,
# сообщите написан ли текст в ASCII или нет

t = input('Введите текст: ')
if t.isdigit():
    num = int(t)
    b = bin(num)
    o = oct(num)
    h = hex(num)
    print(b, o, h, sep='\n')
elif t.isascii():
    print('все символы в строке ASCII')

import math
print(math.pi, math.e, math.inf, math.nan, math.tau, sep='\n')
print(dir(math))
print(help(math.gcd))

import decimal
pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
decimal.getcontext().prec = 120
science = 2 * pi * decimal.Decimal(23.452346) ** 2
print(science)

import fractions
f1 = fractions.Fraction(1, 3)
print(f1)
f2 = fractions.Fraction(3, 5)
print(f2)
print(f1 * f2)

a = complex(2, 3)
b = complex('2+3j')
print(a, b, a == b, sep='\n')

d = 3.1432
print(round(d, 2))
