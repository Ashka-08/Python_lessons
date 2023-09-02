# import argparse

# parser = argparse.ArgumentParser(description='My first argument parser')
# parser.add_argument('numbers', metavar='N', type=float,
#                 nargs='*', help='press some numbers')
# args = parser.parse_args()
# print(f'В скрипт передано: {args}')

# # Запустим скрипт с несколькими значениями:
# # $ python import_argparse.py 42 3.14 73

# """
# В скрипт передано: Namespace(numbers=[42.0, 3.14, 73.0])
# """

# # ArgumentParser

# parser = argparse.ArgumentParser(prog='average',
#             description='My first argument parser',
#             epilog='Returns the arithmetic mean')
# parser.add_argument('numbers', metavar='N', type=float,
#                 nargs='*', help='press some numbers')
# args = parser.parse_args()
# print('prog, description, epilog')

# # Запустим скрипт с ключом -h:
# # $ python import_argparse.py -h

# """
# usage: average [-h] [N ...]

# My first argument parser

# positional arguments:
#   N           press some numbers

# options:
#   -h, --help  show this help message and exit

# Returns the arithmetic mean
# """


# # Выгружаем результаты

# import argparse

# parser = argparse.ArgumentParser(description='My first argument parser')
# parser.add_argument('numbers', metavar='N', type=float,
#                     nargs='*', help='press some numbers')
# args = parser.parse_args()
# print(f'Получили экземпляр Namespace: {args = }')
# print(f'У Namespace работает точечная нотация: {args.numbers = }')
# print(f'Объекты внутри могут быть любыми: {args.numbers[1] = }')

# # запускаем командой:
# # python import_argparse.py 42 3.14 73

# """ 
# Получили экземпляр Namespace: args = Namespace(numbers=[42.0, 3.14, 73.0])
# У Namespace работает точечная нотация: args.numbers = [42.0, 3.14, 73.0]
# Объекты внутри могут быть любыми: args.numbers[1] = 3.14
# """

# import argparse

# def quadratic_equations(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     if d == 0:
#         return -b / (2 * a)
#     return None

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Solving quadratic equations')
#     parser.add_argument('param', metavar='a b c', type=float, nargs=3,
#                         help='enter a b c separated by a space')
#     args = parser.parse_args()
#     print(quadratic_equations(*args.param))

# # запускаем командой:
# # python import_argparse.py 2 -12 10

# # Вывод: (5.0, 1.0)


# # Необязательные аргументы и значения по умолчанию

# import argparse

# def quadratic_equations(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     if d == 0:
#         return -b / (2 * a)
#     return None

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Solving quadratic equations')
#     parser.add_argument('-a', metavar='a', type=float,
#                         help='enter a for ax^2+bx+c=0', default=1)
#     parser.add_argument('-b', metavar='b', type=float,
#                         help='enter b for ax^2+bx+c=0', default=0)
#     parser.add_argument('-c', metavar='c', type=float,
#                         help='enter c for ax^2+bx+c=0', default=0)
#     args = parser.parse_args()
#     print(quadratic_equations(args.a, args.b, args.c))

# # Теперь при вызове будет ошибка:
# # python import_argparse.py 2 -12 10
# # Вывод:
# # usage: import_argparse.py [-h] [-a a] [-b b] [-c c]
# # import_argparse.py: error: unrecognized arguments: 2 -12 10

# # Команда для вызова:
# # python import_argparse.py -a 2 -b -12

# # Вывод: 
# # (6.0, 0.0)

# Параметр action для аргумента

import argparse

parser = argparse.ArgumentParser(description='Sample')
parser.add_argument('-x', action='store_const', const=42)
parser.add_argument('-y', action='store_true')
parser.add_argument('-z', action='append')
parser.add_argument('-i', action='append_const', const=int, dest='types')
parser.add_argument('-f', action='append_const', const=float, dest='types')
parser.add_argument('-s', action='append_const', const=str, dest='types')
args = parser.parse_args()
print(args)

# Команда для вызова:
# python import_argparse.py -x -y -z 42 -z 73 -i -f -s

# Вывод:
# Namespace(x=42, y=True, z=['42', '73'], types=[<class 'int'>, <class 'float'>, <class 'str'>])

