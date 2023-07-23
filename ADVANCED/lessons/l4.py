a = 42
print(type(a), id(a))
print(type(id))

def my_func():
    pass


def quadratic_equations(a: int | float, b: int | float, c: int | float) -> tuple[float, float] | float | None:
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 *a)
    elif d == 0:
        return -b / (2 * a)
    else:
        return None


print(quadratic_equations(2, -3, -9))

# Пример с неизменяемыми переменными.
def no_mutable(a: int) -> int:
    a += 1
    print(f'In func {a = }') 
    # Для демонстрации работы, но не для привычки принтить из функции
    return a


a = 42
print(f'In main {a = }')
z = no_mutable(a)
print(f'{a = }\t{z = }')

# Пример с изменяемыми объектами.
def mutable(data: list[int]) -> list[int]:
    for i, item in enumerate(data):
        data[i] = item + 1
    print(f'In func {data = }') 
    # Для демонстрации работы, но не для привычки принтить из функции
    return data

    
my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = mutable(my_list)
print(f'{my_list = }\t{new_list = }')


# Неявный return
def quadratic_equations(a, b, c):
    10
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    # return None # можно не писать


# Значения по умолчанию
def quadratic_equations(a, b=0, c=0):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)


print(quadratic_equations(2, -9))


# Изменяемый объект как значение по умолчанию
def from_one_to_n(n, data=None):
    if data is None:
        data = []
    for i in range(1, n + 1):
        data.append(i)
    return data


# Позиционные и ключевые параметры
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only) # Принтим для примера, а не для привычки


# combined_example(1, 2, 3) # TypeError
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3) # TypeError


# Если несколько ключевых параметров, порядок аргументов может отличаться
def triangulation(*, x, y, z):
    pass


triangulation(y=5, z=2, x=11)

# Параметр *args - любое число позиционных аргументов (в кортеж)
def mean(*args):
    return sum(args) / len(args)


print(mean(*[1, 2, 3]))
print(mean(1, 2, 3))


# Параметр **kwargs,- любое число ключевых параметров и возвращает словарь
def school_print(**kwargs):
    for key, value in kwargs.items():
        print(f'По предмету "{key}" получена оценка {value}')


school_print(химия=5, физика=4, математика=5, физра=5)


# Области видимости: global и nonlocal
def func(y: int) -> int:
    global x
    x += 100
    print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
    return y + 1


x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')

def main(a):
    x = 1
    def func(y):
        nonlocal x
        x += 100
        print(f'In func {x = }') # Для демонстрации работы
        return y + 1
    return x + func(a)
x = 42
print(f'In main {x = }')
z = main(x)
print(f'{x = }\t{z = }')

# Доступ к константам
LIMIT = 1_000
def func(x, y):
    result = x ** y % LIMIT
    return result


print(func(42, 73))


# lambda parameters: action
my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
s_key = sorted(my_dict.items()) 
#словарь сортируется по ключам, т.е. по алфавиту.
s_value = sorted(my_dict.items(), key=lambda x: x[1])
# сортировка по второму (индексация начинается с нуля) элементу, т.е. по значению
print(f'{s_key = }\n{s_value = }')


# Документирование кода функций в переменную __doc__.
def max_before_hundred(*args):
    """Return the maximum number not exceeding 100."""
    m = float('-inf')
    for item in args:
        if m < item < 100:
            m = item
    return m


print(max_before_hundred(-42, 73, 256, 0))


def max_before_hundred(*args):
    """Return the maximum number not exceeding 100.

    :param args: tuple of int or float numbers
    :return: int or float number from the tuple args
    """
    pass


# map(function, iterable)
texts = ["Привет", "ЗДОРОВА", "привеТствую"]
res = map(lambda x: x.lower(), texts)
print(*res)
# лямбда для вызова метода lower у каждого из переданных объектов


# filter(function, iterable)
numbers = [42, -73, 1024]
res = tuple(filter(lambda x: x > 0, numbers))
print(res)
# Лямбда фильтрует элементы больше нуля. 
# Функция tuple преобразует итератор к кортежу с положительными числами.


# zip(*iterables, strict=False)
names = ["Иван", "Николай", "Пётр"]
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13, 0.99]
for name, salary, award in zip(names, salaries, awards):
    print(f'{name} заработал {salary:.2f} денег и премию {salary* award:.2f}')


# max(iterable, *[, key, default]) или max(arg1, arg2, *args[, key])
lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр", 109_000)]
print(max(lst_1, default='empty'))
print(max(*lst_2))
print(max(lst_3, key=lambda x: x[1]))


# min(iterable, *[, key, default]) или min(arg1, arg2, *args[, key])
lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр", 109_000)]
print(min(lst_1, default='empty'))
print(min(*lst_2))
print(min(lst_3, key=lambda x: x[1]))


# sum(iterable, /, start=0)
my_list = [42, 256, 73]
print(sum(my_list))
print(sum(my_list, start=1024))


# all(iterable)
numbers = [42, -73, 1024]
if all(map(lambda x: x > 0, numbers)):
    print('Все элементы положительные')
else:
    print('В последовательности есть отрицательные и/или нулевые элементы')


# any(iterable)
numbers = [42, -73, 1024]
if any(map(lambda x: x > 0, numbers)):
    print('Хотя бы один элемент положительный')
else:
    print('Все элементы не больше нуля')


# chr(integer) возвращает строковой символ из таблицы Юникод по его номеру
print(chr(97))
print(chr(1105))
print(chr(128519))


# ord(char) возвращает его код символа таблице Юникод.
print(ord('a'))
print(ord('а'))
print(ord('😉'))


# locals() возвращает словарь переменных из локальной области видимости на момент вызова
SIZE = 10
def func(a, b, c):
    x = a + b
    print(locals())
    z = x + c
    return z
func(1, 2, 3)


# globals() возвращает словарь переменных из глобальной области видимости
# словарь globals позволяет изменить значение переменной

SIZE = 10
def func(a, b, c):
    x = a + b
    print(globals())
    z = x + c
    return z
print(globals())
print(func(1, 2, 3))


# vars() аналог locals(). Или вернет атрибут __dict__ переданного объекта или ошибку, если нет такого атрибута
print(vars(int))


# Задание
data = [25, -42, 146, 73, -100, 12]
print(list(map(str, data))) # ['25', '-42', '146', '73', '-100', '12']
print(max(data, key=lambda x: -x)) # -100
print(*filter(lambda x: not x[0].startswith('__'), globals().items()))
# ('data', [25, -42, 146, 73, -100, 12])
