# try и except

from random import randint


# def get(text: str = None) -> int:
#     data = input(text)
#     try:
#         num = int(data)
#     except ValueError as e:
#         print(f'Ваш ввод привёл к ошибке ValueError: {e}')
#         num = 1
#         print(f'Будем считать результатом ввода число {num}')
#     return num

# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     print(f'100 / {number} = {100 / number}')

"""
Введите целый делитель: сорок два
Ваш ввод привёл к ошибке ValueError: invalid literal for int() with base 10: 'сорок два'
Будем считать результатом ввода число 1
100 / 1 = 100.0"""


# Цикл while для обработки ошибок ввода

# def get(text: str = None) -> int:
#     while True:
#         try:
#             num = int(input(text))
#             break
#         except ValueError as e:
#             print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
#                 f'Попробуйте снова')
#     return num

# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     print(f'100 / {number} = {100 / number}')


# Код ниже имитирует получение данных из источника

# def get_data():
#     """Получает данные из внешнего источника. Имитируем это через рандом"""
#     if result := randint(0,3):
#         return result
#     else:
#         raise ConnectionError

# MAX_COUNT = 5
# count = 0
# while count < MAX_COUNT:
#     count += 1
#     try:
#         data = get_data()
#         break
#     except ConnectionError as e:
#         print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')

# print(data)

"""
Попытка 1 из 5 завершилась ошибкой
2"""

# Несколько except для одного try

# def hundred_div_num(text: str = None) -> tuple[int, float]:
#     while True:
#         try:
#             num = int(input(text))
#             div = 100 / num
#             break
#         except ValueError as e:
#             print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
#                 f'Попробуйте снова')
#         except ZeroDivisionError as e:
#             div = float('inf')
#             break
#     return num, div

# if __name__ == '__main__':
#     n, d = hundred_div_num('Введите целый делитель: ')
#     print(f'Результат операции: "100 / {n} = {d}"')


# Команда else

# MAX_COUNT = 5
# result = None
# for count in range(1, MAX_COUNT + 1):
#     try:
#         num = int(input('Введите целое число: '))
#         print('Успешно получили целое число')
#     except ValueError as e:
#         print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')
#     else:
#         result = 100 / num
#         break
# print(f'{result = }')


# Вложенные блоки обработки исключений

# MAX_COUNT = 5
# result = None
# for count in range(1, MAX_COUNT + 1):
#     try:
#         num = int(input('Введите целое число: '))
#         print('Успешно получили целое число')
#     except ValueError as e:
#         print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')
#     else:
#         try:
#             result = 100 / num
#         except ZeroDivisionError as e:
#             result = float('inf')
#         break
# print(f'{result = }')


# Команда finally

# def get(text: str = None) -> int:
#     num = None
#     try:
#         num = int(input(text))
#     except ValueError as e:
#         print(f'Ваш ввод привёл к ошибке ValueError: {e}')
#     finally:
#         return num if isinstance(num, int) else 1

# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     try:
#         print(f'100 / {number} = {100 / number}')
#     except ZeroDivisionError as e:
#         print(f'На ноль делить нельзя. Получим {e}')


# Блок finally без except

# file = open('text.txt', 'r', encoding='utf-8')
# try:
#     data = file.read().split()
#     print(data[len(data)])
# finally:
#     print('Закрываю файл')
#     file.close()

"""
🔥 Важно! Для ситуации выше правильным будет использовать менеджер
контекста для гарантированного закрытия файла"""


# Задание

# d = {'42': 73}
# try:
#     key, value = input('Ключ и значение: ').split()
#     if d[key] == value:
#         r = 'Совпадение'
# except ValueError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# else:
#     print(r)
# finally:
#     print(d)

# """
# Ключ и значение: 42 13
# {'42': 73}
# Traceback (most recent call last):
#   File "c:\Users\Professional\Desktop\geekbrains\Python\ADVANCED\lessons\l13.py", line 171, in <module>
#     print(r)
#           ^
# NameError: name 'r' is not defined


# Ключ и значение: 42 73 3
# too many values to unpack (expected 2)
# {'42': 73}


# Ключ и значение: 73 42
# '73'
# {'42': 73}


# Ключ и значение: 42 73
# {'42': 73}
# Traceback (most recent call last):
#   File "c:\Users\Professional\Desktop\geekbrains\Python\ADVANCED\lessons\l13.py", line 171, in <module>
#     print(r)
#           ^
# NameError: name 'r' is not defined
# """


# Ключевое слово raise

# def add_key(dct, key, value):
#     if key in dct:
#         raise KeyError(f'Перезаписывание существующего ключа запрещено. {dct[key] = }')
#     dct[key] = value
#     return dct

# data = {'one': 1, 'two': 2}
# print(add_key(data, 'three', 3))
# print(add_key(data, 'three', 3))


# Поднимаем исключения в классах

# class User:
#     def __init__(self, name, age):
#         if 6 < len(name) < 30:
#             self.name = name
#         else:
#             raise ValueError(f'Длина имени должна быть между 6 и 30 символами. {len(name) = }')
#         if not isinstance(age, (int, float)):
#             raise TypeError(f'Возраст должен быть числом. Используйте int или float. {type(age) = }')
#         elif age < 0:
#             raise ValueError(f'Возраст должен быть положительным. {age = }')
#         else:
#             self.age = age

# user = User('Яков', '-12')

# Задание

def func(a, b, c):
    if a < b < c:
        raise ValueError('Не перемешано!')
    elif sum((a, b, c)) == 42:
        raise NameError('Это имя занято!')
    elif max(a, b, c, key=len) < 5:
        raise MemoryError('Слишком глуп!')
    else:
        raise RuntimeError('Что-то не так!!!')

# func(11, 7, 3)
# """
# file "c:\Users\Professional\Desktop\geekbrains\Python\ADVANCED\lessons\l13.py", line 213, in func    
#     elif max(a, b, c, key=len) < 5:
#          ^^^^^^^^^^^^^^^^^^^^^
# TypeError: object of type 'int' has no len()"""

# func(3, 2, 3) # RuntimeError: Что-то не так!!!
# func(73, -40, 9) # NameError: Это имя занято!
# func(10, 20, 30) # ValueError: Не перемешано!

# Создание собственных исключений

from error0 import UserNameError, UserAgeError

class User:
    MIN_LEN = 6
    MAX_LEN = 30
    
    def __init__(self, name, age):
        if self.MIN_LEN < len(name) < self.MAX_LEN:
            self.name = name
        else:
            raise UserNameError
        if not isinstance(age, (int, float)) or age < 0:
            raise UserAgeError
        else:
            self.age = age

user = User('Яков', '-12')


# сделаем чуть более информативно

class User:
    def __init__(self, name, age):
        if 6 < len(name) < 30:
            self.name = name
        else:
            raise UserNameError(name)
        if not isinstance(age, (int, float)) or age < 0:
            raise UserAgeError(age)
        else:
            self.age = age
            
user = User('Яков', '-12')

# Методы __init__ и __str__ в классах своих исключений

from error1 import UserNameError, UserAgeError

class User:
    MIN_LEN = 6
    MAX_LEN = 30
    
    def __init__(self, name, age):
        if self.MIN_LEN < len(name) < self.MAX_LEN:
            self.name = name
        else:
            raise UserNameError(name, self.MIN_LEN, self.MAX_LEN)
        if not isinstance(age, (int, float)) or age < 0:
            raise UserAgeError
        else:
            self.age = age

user = User('Яков', '-12')