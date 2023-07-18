print('Создание списков')

list_1 = list() # функция возвращает пустой список.
print(list_1) #[]
list_2 = list((3.14, True, "Hello world!"))
list_3 = [] # синтаксический сахар, работает быстрее
print(list_3) #[]
list_4 = [3.14, True, "Hello world!"]


print('Доступ к элементам списка')

my_list = [2, 4, 6, 8, 10, 12]
print(my_list[0]) #2
# print(my_list[6]) # IndexError: list index out of range

print(my_list[-1]) # 12, т.к. последний элемент имеет индекс - 1
# print(my_list[-10]) # IndexError: list index out of range
print()

print('метод append(item)')

a = 42
b = 'Hello world!'
c = [1, 3, 5, 7]
my_list = [None] 
print(my_list) #[None], None - это объект

my_list.append(a)
print(my_list)
my_list.append(b)

print(my_list)
my_list.append(c)
print(my_list)
print()

print('Метод extend(items)')

a = 42
b = 'Hello world!'
c = [1, 3, 5, 7]
my_list = [None]
# my_list.extend(a) # TypeError: 'int' object is not iterable
print(my_list)
my_list.extend(b)
print(my_list)
my_list.extend(c)
print(my_list)
my_list.extend(my_list)
print(my_list)
print()

print('Метод pop(index)')

my_list = [2, 4, 6, 8, 10, 12, 7, 9]
spam = my_list.pop()
print(spam, my_list)
eggs = my_list.pop(1)
print(eggs, my_list)
# err = my_list.pop(10) # IndexError: pop index out of range
print()

print('Метод count(item)')

spam = my_list.count(2)
print(spam)
eggs = my_list.count(3)
print(eggs)
print()

print('Метод index(item, start_index, stop_index)')

my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
spam = my_list.index(2)
print(spam)
eggs = my_list.index(2, spam + 1, 90)
print(eggs)
# err = my_list.index(3) # ValueError: 3 is not in list
print()

print('Метод insert(i, item)')

my_list.insert(2, 555)
print(my_list)
my_list.insert(-2, 13)
print(my_list)
# my_list.insert(42, 73) # my_list.append(73)
print(my_list)
print()

print('Метод remove(item)')

my_list.remove(6)
print(my_list)
# my_list.remove(3) # ValueError: list.remove(x): x not in list
print(my_list)

print('Функция sorted(massive)')

sort_list = sorted(my_list)
print(my_list, sort_list, sep='\n')
rev_list = sorted(my_list, reverse=True)
print(my_list, rev_list, sep='\n')
print()

print('Метод sort()')

my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
print()

print('Функция reversed()')

res = reversed(my_list)
print(type(res), res)
rev_list = list(reversed(my_list))
print(rev_list)

for item in reversed(my_list):
    print(item)
print()

print('Метод reverse()')

my_list.reverse()
print(my_list)
print()

print('синтаксический сахар [::-1]')

new_list = my_list[::-1]
print(my_list, new_list, sep='\n')

print('Срезы')

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
print(my_list[2:7:2])
print(my_list[:7:2])
print(my_list[2::2])
print(my_list[2:7:])
print(my_list[8:3:-1])
print(my_list[3::])
print(my_list[:7:])

print('Копии')

new_list = my_list.copy()
print(my_list, new_list, sep='\n')
my_list[2] = 555
print(my_list, new_list, sep='\n')
print()

print('Строки')

text = 'Hello world!'
print(text[6])
print(text[3:7])

print(text.count('l'))
print(text.index('l'))
print(text.find('l'))
print(text.find('z'))
print()

print('Форматирование')

name = 'Alex'
age = 12
text = 'Меня зовут %s и мне %d лет' % (name, age) # оператор %
"""
'%s' - Строка
'%c'- строка из одного символа или число - код символа
'%d', '%i', '%u' - Десятичное число
'%o' - Число в восьмеричной системе счисления.
'%x', '%X' - Число в шестнадцатеричной системе счисления (буквы в нижнем или 
в верхнем регистре).
'%f', '%F'- Число с плавающей точкой (обычный формат)
'%%' - Знак '%'.
'%e', '%E' - Число с плавающей точкой с экспонентой
'%g', '%G' - Вещественное число (обычный формат), если порядок числа будет 
больше -5 и меньше заданной точности (по умолчанию 6), иначе экспоненциальный вид 
(нижний/верхний регистр). Точность также равна количеству видимых значимых цифр.
"""
text = 'Меня зовут {} и мне {} лет'.format(name, age) #метод format()
text = f'Меня зовут {name} и мне {age} лет' #f-строка
text = 'Меня зовут' + name + ' и мне ' + age + ' лет' # конкатенация с +
print(text)
# конкатенация с *
print('name * 3 =', name * 3)

# модуль Template
from string import Template
from random import randint
template_string = Template('Лучший язык программирования - $lang!')
prepared_string = template_string.substitute(lang='Python')
print(prepared_string) # Лучший язык программирования - Python!
template_string = Template('Хочу зарабатывать $zp$$!')
prepared_string = template_string.substitute(zp=randint(10, 100)**randint(10, 100))
print(prepared_string) # Хочу зарабатывать 504857282956046106624$!
print()

print('Уточнение формата')

pi = 3.1415
print(f'Число Пи с точностью два знака: {pi:.2f}') #Число Пи с точностью два знака: 3.14

data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
for item in data:
  print(f'{item:>10}')
"""
      3254
4364314532
  43465474
      2342
    462256
      1747"""    
num = 2 * pi * data[1] 
print(f'{num = :_}') # num = 27_420_988_204.556
print()

print('Метод split')

link = 'https://habr.com/ru/users/dzhoker1/posts/'
urls = link.split('/')
print(urls)

a, b, c = input('Введите 3 числа через пробел: ').split()
print(c, b, a)

a, b, c, *_ = input('Введите не менее трёх чисел через пробел: ').split()
print()

print('Метод join')

data = ['https:', '', 'habr.com', 'ru', 'users', 'dzhoker1', 'posts']
url = '/'.join(data)
print(url)
print()

print('Методы upper, lower, title, capitalize')

text = 'однажды в СТУДЁНУЮ зИмнЮЮ ПоРУ'
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print()

print('Методы startswith и endswith')

text = 'Однажды в студёную зимнюю пору'
print(text.startswith('Однажды'))
print(text.endswith('зимнюю', 0, -5))
print()

text = 'Привет, мир!'
print(text.find(' ')) # 7
print(text.title()) # Привет, Мир!
print(text.split()) # ['Привет,', 'мир!']
print(f'{text = :>25}') #text =              Привет, мир!
print()

print('Кортежи')

a = ()
b1 = 1,
b2 = (1,)
c1 = 1, 2, 3,
c2 = (1, 2, 3)
d = tuple(range(3))
print(a, b1, b2, c1, c2, d, sep='\n')
"""
()96*5
(1,)
(1,)
(1, 2, 3)
(1, 2, 3)
(0, 1, 2)"""

my_tuple = (2, 4, 6, 2, 8, 10, 12, 14, 16, 18)
print(my_tuple[2:6:2])
print(my_tuple[-3])
print(my_tuple.count(2))
print(f'{my_tuple = }')
print(my_tuple.index(2, 2))
print(type('text',))
print()

print('Словари')

a = {'one': 42, 'two': 3.14, 'ten': 'Hello world!'}
b = dict(one=42, two=3.14, ten='Hello world!')
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world!')])
print(a == b == c) # True

print('Добавление нового ключа')

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
my_dict['ten'] = 10
print(my_dict)

print('Доступ к значению словаря')

TEN = 'ten'
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict['two'])
print(my_dict[TEN])

print('метод get')

print(my_dict.get('two'))
print(my_dict.get('five'))
print(my_dict.get('five', 5))
print(my_dict.get('ten', 5))

print('методы словарей')
spam = my_dict.setdefault('five')
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.setdefault('six', 6)
print(f'{eggs = }\t{my_dict=}')
new_spam = my_dict.setdefault('two')
print(f'{new_spam=}\t{my_dict=}')
new_eggs = my_dict.setdefault('one', 1_000)
print(f'{new_eggs=}\t{my_dict=}')

print(my_dict.keys())
for key in my_dict.keys():
    print(key)
for key in my_dict: 
#отработает также, т.к. По умолчанию словарь возвращает ключи для итерации в цикле.
    print(key)

print(my_dict.values())
for value in my_dict.values():
    print(value)

print(my_dict.items())
for tuple_data in my_dict.items():
    print(tuple_data)
for key, value in my_dict.items():
    print(f'{key = } value before 100 - {100 - value}')

spam = my_dict.popitem()
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.popitem()
print(f'{eggs = }\t{my_dict=}')

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
my_dict.update(dict(six=6))
print(my_dict) 
# {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10, 'six': 6}
my_dict.update(dict([('five', 5), ('two', 42)]))
print(my_dict)
# {'one': 1, 'two': 42, 'three': 3, 'four': 4, 'ten': 10, 'six': 6, 'five': 5}

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6)
print(new_dict) 
#{'one': 1, 'two': 42, 'three': 3, 'four': 4, 'ten': 10, 'five': 5, 'six': 6}

# Задание
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.items()) 
# dict_items([('one', 1), ('two', 2), ('three', 3), ('four', 4), ('ten', 10)])
print(my_dict.keys())
# dict_keys(['one', 'two', 'three', 'four', 'ten'])
print(my_dict.setdefault('ten', 555)) # 10
print(my_dict.values()) #dict_values([1, 2, 3, 4, 10])
print(my_dict.pop('one')) # 1
my_dict['one'] = my_dict['four']
print(my_dict) #{'two': 2, 'three': 3, 'four': 4, 'ten': 10, 'one': 4}

print('Множества')

my_set = {1, 2, 3, 4, 2, 5, 6, 7}
print(my_set)
my_f_set = frozenset((1, 2, 3, 4, 2, 5, 6, 7,))
print(my_f_set)

my_set = {3, 4, 2, 5, 6, 1, 7}
print(my_set) #{1, 2, 3, 4, 5, 6, 7}
my_set.add(9) 
print(my_set) #{1, 2, 3, 4, 5, 6, 7, 9}
my_set.add(7)
print(my_set) #{1, 2, 3, 4, 5, 6, 7, 9}
# my_set.add(9, 10) # TypeError: set.add() takes exactly one argument (2 given)
my_set.add((9, 10))
print(my_set) #{(9, 10), 1, 2, 3, 4, 5, 6, 7, 9}

my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.remove(5)
print(my_set)

my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.discard(5)
print(my_set)
my_set.discard(10)

my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.intersection(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')

my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set & other_set
print(f'{my_set = }\n{other_set = }\n{new_set = }')

my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.union(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')
new_set_2 = my_set | other_set
print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')

my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.difference(other_set)
36
print(f'{my_set = }\n{other_set = }\n{new_set = }')
new_set_2 = my_set - other_set
print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')

# Задание
my_set = frozenset({3, 4, 1, 2, 5, 6, 1, 7, 2, 7})
print(my_set) #frozenset({1, 2, 3, 4, 5, 6, 7})
print(len(my_set)) #7
print(my_set - {1, 2, 3}) #frozenset({4, 5, 6, 7})
print(my_set.union({2, 4, 6, 8})) #frozenset({1, 2, 3, 4, 5, 6, 7, 8})
print(my_set & {2, 4, 6, 8}) #frozenset({2, 4, 6})
# print(my_set.discard(10)) #AttributeError: 'frozenset' object has no attribute 'discard'

print('Классы bytes и bytearray')

text_en = 'Hello world!'
res = text_en.encode('utf-8')
print(res, type(res)) # b'Hello world!' <class 'bytes'>
text_ru = 'Привет, мир!'
res = text_ru.encode('utf-8')
print(res, type(res))
"""
b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82, \xd0\xbc\xd0\xb8\xd1\x80!' 
<class 'bytes'>"""

x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8')
y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')
print(f'{x = }\n{y = }')
