# Обмен значения переменных
a = 1
b = 1
a, b = b, a


# Распаковка коллекции
# a, b, c = input("Три символа: ")
# print(f'{a=} {b=} {c=}')

a, b, c = ("один", "два", "три",)
print(f'{a=} {b=} {c=}')


# Распаковка с упаковкой “лишнего” 
data = ["один", "два", "три", "четыре", "пять", "шесть", "семь"]
a, b, c, *d = data
print(f'{a=} {b=} {c=} {d=}') #a='один' b='два' c='три' d=['четыре', 'пять', 'шесть', 'семь']
a, b, *c, d = data
print(f'{a=} {b=} {c=} {d=}') #a='один' b='два' c=['три', 'четыре', 'пять', 'шесть'] d='семь'
a, *b, c, d = data
print(f'{a=} {b=} {c=} {d=}') #a='один' b=['два', 'три', 'четыре', 'пять'] c='шесть' d='семь'
*a, b, c, d = data
print(f'{a=} {b=} {c=} {d=}') #a=['один', 'два', 'три', 'четыре'] b='пять' c='шесть' d='семь'

# Подчеркивание как мусорка
link = 'https://docs.python.org/3/faq/programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another'
prefix, *_, suffix = link.split('/')

# Распаковка со звездочкой
data = [2, 4, 6, 8, 10, ]
for item in data:
    print(item, end='\t') #2       4       6       8       10
print()
print(*data, sep='\t') #2       4       6       8       10


# Множественное присваивание и сравнение
a = b = c = 0
a += 42
print(f'{a=} {b=} {c=}') #a=42 b=0 c=0

a, b, c = 1, 2, 3
print(f'{a=} {b=} {c=}')


a = b = c = 42
# if a == b and b == c:
if a == b == c:
    print('Полное совпадение')
if a < b < c:
    print('b больше a и меньше c')


# Итераторы
data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter) #<list_iterator object at 0x000001ED5B43FF70>

data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter) #2 4 6 8
print(*list_iter) #пустота

# работа функции iter с двумя параметрами — 
# например чтение бинарного файла блоками фиксированного размера
# import functools
# f = open('mydata.bin', 'rb')
# for block in iter(functools.partial(f.read, 16), b''):
#     print(block)
# f.close()

data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
# print(next(list_iter)) # StopIteration

data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))



data = {"один": 1, "два": 2, "три": 3}
x = iter(data.items()) 
print(x) #<dict_itemiterator object at 0x00000222702B4270>
y = next(x)
print(y) #('один', 1)
z = next(iter(y)) #итератор по кортежу
print(z) #один


# генераторы
a = range(0, 10, 2)
print(f'{a=}, {type(a)=}, {a.__sizeof__()=}, {len(a)}')
# a=range(0, 10, 2), type(a)=<class 'range'>, a.__sizeof__()=48, 5


b = range(-1_000_000, 1_000_000, 2)
print(f'{b=}, {type(b)=}, {b.__sizeof__()=}, {len(b)}')
# b=range(-1000000, 1000000, 2), type(b)=<class 'range'>, b.__sizeof__()=48, 1000000


# генераторные выражения
my_gen = (chr(i) for i in range(97, 103))
print(my_gen) # <generator object <genexpr> at 0x000001ED58DD7D60>
for char in my_gen:
    print(char)

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
res = list(mult)
print(f'{len(res)=}\n{res}')


# List comprehensions
my_listcomp = [chr(i) for i in range(97, 103)]
print(my_listcomp) # ['a', 'b', 'c', 'd', 'e', 'f']
for char in my_listcomp:
    print(char)


data = [2, 5, 1, 42, 65, 76, 24, 77]
res = []
for item in data:
    if item % 2 == 0:
        res.append(item)
print(f'{res = }')

# Аналогичное решение, но с использованием синтаксического сахара listcomp:

data = [2, 5, 1, 42, 65, 76, 24, 77]
res = [item for item in data if item % 2 == 0]
print(f'{res = }')


# если нужен список, то лучше listcomp
x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = [i + j for i in x if i % 2 != 0 for j in y if j != 1]
print(f'{len(res)=}\n{res}')


# а если все элементы сразу не нужны, то генераторное выражение
x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
for item in mult:
    print(f'{item = }')


# Set comprehensions
my_setcomp = {chr(i) for i in range(97, 123)}
print(my_setcomp) # {'f', 'g', 'b', 'j', 'e',... }
for char in my_setcomp:
    print(char)

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = {i + j for i in x if i % 2 != 0 for j in y if j != 1}
print(f'{len(res)=}\n{res}')


# Dict comprehensions
my_dictcomp = {i: chr(i) for i in range(97, 123)}
print(my_dictcomp) # {97: 'a', 98: 'b', 99: 'c',... }
for number, char in my_dictcomp.items():
    print(f'dict[{number}] = {char}')


# задание
data = {2, 4, 4, 6, 8, 10, 12}
res1 = {None: item for item in data if item > 4}
res2 = (item for item in data if item > 4)
res3 = [[item] for item in data if item > 4]
print(res1, res2, res3)
# {None: 12} <generator object <genexpr> at 0x000001BA3DCC82B0> [[6], [8], [10], [12]]


# Создание функции генератора
# сначала создадим обычную функцию, которая вернёт список чисел.
def factorial(n):
    number = 1
    result = []
    for i in range(1, n + 1):
        number *= i
        result.append(number)
    return result


for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')


# превратим функцию в генератор
def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
    yield number


for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')

# Функции iter и next для генераторов
my_iter = iter(factorial(4))
print(my_iter)
print(next(my_iter))
# print(next(my_iter)) # StopIteration


# задание
def gen(a: int, b: int) -> str:
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield str(i)
for item in gen(10, 1):
    print(f'{item = }')
"""
item = '1'
item = '2'
item = '3'
item = '4'
item = '5'
item = '6'
item = '7'
item = '8'
item = '9'
item = '10'"""

def zipper(iterable1, iterable2):
    for i in range(min(len(iterable1), len(iterable2))):
        yield iterable1[i]
        yield iterable2[i]

print(*zipper([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'])) #1 a 2 b 3 c 4 d 5 e


# Данная Python программа выводит числа от 1 до 15, возведенные в куб,
# используя yield и, следовательно, генератор. Функция будет бесконечно генерировать
# последовательность чисел в третьей степени, начиная с 1

def nextCube():
    acc = 1
 
    # Бесконечный цикл
    while True:
        yield acc**3                
        acc += 1 # После повторного обращения
                # исполнение продолжится отсюда
 
# Ниже мы запрашиваем у генератора и выводим ровно 15 чисел
count = 1
for num in nextCube():
    if count > 15:
        break   
    print(num)
    count += 1