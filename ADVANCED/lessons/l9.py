"""Замыкание"""


# Области видимости
def func(a):
    x = 42
    res = x + a
    return res
x = 73
print(func(64)) #106


# Функция как объект высшего порядка
def add_str(a: str, b: str) -> str:
    return a + ' ' + b
print(add_str('Hello', 'world!')) #Hello world!


# Передача функции как объекта в другую функцию
from typing import Callable
def add_one_str(a: str) -> Callable[[str], str]:
    def add_two_str(b: str) -> str:
        return a + ' ' + b
    return add_two_str
print(add_one_str('Hello')('world!')) #Hello world!


# Замыкаем функцию с параметрами
from typing import Callable
def add_one_str(a: str) -> Callable[[str], str]:
    def add_two_str(b: str) -> str:
        return a + ' ' + b
    return add_two_str
hello = add_one_str('Hello')
bye = add_one_str('Good bye')
print(hello('world!')) #Hello world!
print(hello('friend!')) #Hello friend!
print(bye('wonderful world!')) #Good bye wonderful world!
print(f'{type(add_one_str) = }, {add_one_str.__name__ = }, {id(add_one_str) = }')
# type(add_one_str) = <class 'function'>, add_one_str.__name__ = 'add_one_str', id(add_one_str) = 2411832795648
print(f'{type(hello) = }, {hello.__name__ = }, {id(hello) = }')
#type(hello) = <class 'function'>, hello.__name__ = 'add_two_str', id(hello) = 2411832793408
print(f'{type(bye) = }, {bye.__name__ = }, {id(bye) = }')
#type(bye) = <class 'function'>, bye.__name__ = 'add_two_str', id(bye) = 2411832796768


# Замыкаем изменяемые и неизменяемые объекты
from typing import Callable
def add_one_str(a: str) -> Callable[[str], str]:
    names = []
    def add_two_str(b: str) -> str:
        names.append(b)
        return a + ', ' + ', '.join(names)
    return add_two_str
hello = add_one_str('Hello')
bye = add_one_str('Good bye')
print(hello('Alex')) #Hello, Alex
print(hello('Karina')) #Hello, Alex, Karina
print(bye('Alina')) #Good bye, Alina
print(hello('John')) #Hello, Alex, Karina, John
print(bye('Neo')) #Good bye, Alina, Neo


# перепишем код и заменим list на неизменяемый str
from typing import Callable
def add_one_str(a: str) -> Callable[[str], str]:
    text = ''
    def add_two_str(b: str) -> str:
        nonlocal text
        text += ', ' + b
        return a + text
    return add_two_str
hello = add_one_str('Hello')
bye = add_one_str('Good bye')
print(hello('Alex')) #Hello, Alex
print(hello('Karina')) #Hello, Alex, Karina
print(bye('Alina')) #Good bye, Alina
print(hello('John')) #Hello, Alex, Karina, John
print(bye('Neo')) #Good bye, Alina, Neo
print()

# Задание
from typing import Callable
def main(x: int) -> Callable[[int], dict[int, int]]:
    d = {}
    def loc(y: int) -> dict[int, int]:
        for i in range(y):
            d[i] = x ** i
        return d
    return loc
small = main(42)
big = main(73)
print(small(7)) #{0: 1, 1: 42, 2: 1764, 3: 74088, 4: 3111696, 5: 130691232, 6: 5489031744}
print(big(7)) #{0: 1, 1: 73, 2: 5329, 3: 389017, 4: 28398241, 5: 2073071593, 6: 151334226289}
print(small(3)) #{0: 1, 1: 42, 2: 1764, 3: 74088, 4: 3111696, 5: 130691232, 6: 5489031744}


"""Простой декоратор без параметров"""


# Передача функции в качестве аргумента
import time
from typing import Callable
def main(func: Callable):
    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)
        print(f'Результат функции {func.__name__}: {result}')
        print(f'Завершение функции {func.__name__} в {time.time()}')
        return result
    return wrapper
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
print(f'{factorial(1000) = }') #factorial(1000) = 40238...
control = main(factorial)
print(f'{control.__name__ = }') #control.__name__ = 'wrapper'
# Запуск функции factorial в 1691572101.277466
# Результат функции factorial: 40238...
# Завершение функции factorial в 1691572101.2864597
print(f'{control(1000) = }') #control(1000) = 40238...
print()

# Синтаксический сахар Python, @
import time
from typing import Callable
def main(func: Callable):
    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)
        print(f'Результат функции {func.__name__}: {result}')
        print(f'Завершение функции {func.__name__} в {time.time()}')
        return result
    return wrapper
@main
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
print(f'{factorial(1000) = }')
# Запуск функции factorial в 1691572444.6757476
# Результат функции factorial: 40238...
# Завершение функции factorial в 1691572444.6827455
# factorial(1000) = 40238...
print()

"""Множественное декорирование"""
from typing import Callable
def deco_a(func: Callable):
    def wrapper_a(*args, **kwargs):
        print('Старт декоратора A')
        print(f'Запускаю {func.__name__}')
        res = func(*args, **kwargs)
        print(f'Завершение декоратора A')
        return res
    print('Возвращаем декоратор A')
    return wrapper_a
def deco_b(func: Callable):
    def wrapper_b(*args, **kwargs):
        print('Старт декоратора B')
        print(f'Запускаю {func.__name__}')
        res = func(*args, **kwargs)
        print(f'Завершение декоратора B')
        return res
    print('Возвращаем декоратор B')
    return wrapper_b
def deco_c(func: Callable):
    def wrapper_c(*args, **kwargs):
        print('Старт декоратора C')
        print(f'Запускаю {func.__name__}')
        res = func(*args, **kwargs)
        print(f'Завершение декоратора C')
        return res
    print('Возвращаем декоратор C')
    return wrapper_c
@deco_c
@deco_b
@deco_a
def main():
    print('Старт основной функции')
main()
# Возвращаем декоратор A
# Возвращаем декоратор B
# Возвращаем декоратор C
# Старт декоратора C
# Запускаю wrapper_b
# Старт декоратора B
# Запускаю wrapper_a
# Старт декоратора A
# Запускаю main
# Старт основной функции
# Завершение декоратора A
# Завершение декоратора B
# Завершение декоратора C
print()

"""Дополнительные переменные в декораторе"""


from typing import Callable
def cache(func: Callable):
    _cache_dict = {}
    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
        return _cache_dict[args]
    return wrapper
@cache
def factorial(n: int) -> int:
    print(f'Вычисляю факториал для числа {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
print(f'{factorial(10) = }')
# Вычисляю факториал для числа 10
# factorial(10) = 3628800
print(f'{factorial(15) = }')
# Вычисляю факториал для числа 15
# factorial(15) = 1307674368000
print(f'{factorial(10) = }') #factorial(10) = 3628800
print(f'{factorial(20) = }')
# Вычисляю факториал для числа 20
# factorial(20) = 2432902008176640000
print(f'{factorial(10) = }') #factorial(10) = 3628800
print(f'{factorial(20) = }') #factorial(20) = 2432902008176640000
print()

# Задание
import random
from typing import Callable

def cache(func: Callable):
    _cache_dict = {}
    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
        return _cache_dict[args]
    return wrapper

@cache
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)
    
print(f'{rnd(1, 10) = }') #nd(1, 10) = 3
print(f'{rnd(1, 10) = }') #nd(1, 10) = 3
print(f'{rnd(1, 10) = }') #nd(1, 10) = 3
print()

"""Декоратор с параметрами"""
import time
from typing import Callable
def count(num: int = 1):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)
                print(f'Результаты замеров {time_for_count}')
            return result
        return wrapper
    return deco
@count(3)
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
print(f'{factorial(10) = }')
# Результаты замеров [9.199997293762863e-06]
# Результаты замеров [9.199997293762863e-06, 9.900002623908222e-06]
# Результаты замеров [9.199997293762863e-06, 9.900002623908222e-06, 8.000002708286047e-06]
# factorial(10) = 3628800
print()
print(f'{factorial(10) = }')
# Результаты замеров [6.999995093792677e-06]
# Результаты замеров [6.999995093792677e-06, 1.2899996363557875e-05]
# Результаты замеров [6.999995093792677e-06, 1.2899996363557875e-05, 9.700001101009548e-06]
# factorial(10) = 3628800
print()


# Задание
import random
from typing import Callable
def count(num: int = 1):
    def deco(func: Callable):
        counter = []
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                counter.append(result)
            return counter
        return wrapper
    return deco
@count(10)
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)
print(f'{rnd(1, 10) = }')
# rnd(1, 10) = [8, 4, 5, 5, 3, 2, 2, 10, 4, 1]
print(f'{rnd(1, 100) = }')
# rnd(1, 100) = [8, 4, 5, 5, 3, 2, 2, 10, 4, 1, 73, 18, 58, 42, 92, 96, 78, 2, 11, 45]
print(f'{rnd(1, 1000) = }')
# rnd(1, 1000) = [8, 4, 5, 5, 3, 2, 2, 10, 4, 1, 73, 18, 58, 42, 92, 96, 78, 2, 11, 45, 154, 715, 283, 690, 824, 860, 881, 257, 577, 150]
print()


"""Декораторы functools"""


@count(3)
def factorial(n: int) -> int:
    """Returns the factorial of the number n."""
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
print(f'{factorial(10) = }') #factorial(10) = [3628800, 3628800, 3628800]
print(f'{factorial.__name__ = }') #factorial.__name__ = 'wrapper'
help(factorial)
# Help on function wrapper in module __main__:
# wrapper(*args, **kwargs)
print()


# Подгрузим модуль foonctools
import time
from typing import Callable
from functools import wraps
def count(num: int = 1):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)
                print(f'Результаты замеров {time_for_count}')
            return result
        return wrapper
    return deco
    
@count(3)
def factorial(n: int) -> int:
    """Returns the factorial of the number n."""
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
print(f'{factorial(10) = }') #factorial(10) = 3628800]
print(f'{factorial.__name__ = }') #factorial.__name__ = 'factorial'
help(factorial)
# Help on function factorial in module __main__:
# factorial(n: int) -> int
#     Returns the factorial of the number n.


# Декоратор cache
from functools import cache
@cache
def factorial(n: int) -> int:
    print(f'Вычисляю факториал для числа {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
print(f'{factorial(10) = }')
# Вычисляю факториал для числа 10
# factorial(10) = 3628800
print(f'{factorial(15) = }')
#  Вычисляю факториал для числа 15
# factorial(15) = 1307674368000
print(f'{factorial(10) = }') # factorial(10) = 3628800
print(f'{factorial(20) = }') 
# Вычисляю факториал для числа 20
# factorial(20) = 2432902008176640000
print(f'{factorial(10) = }') # factorial(10) = 3628800
print(f'{factorial(20) = }') # factorial(20) = 2432902008176640000
