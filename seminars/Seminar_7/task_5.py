# Напишите функцию triangle(a, b, c), которая принимает на вход три длины 
# отрезков и определяет, можно ли из этих отрезков составить треугольник.
# Входные данные
# Выходные данные
# triangle(1, 1, 2)
# Это не треугольник
# triangle(7, 6, 10)

# квадрат гипотенузы равен сумме квадратов катетов

def Triangle(a, b, c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False
a = int(input('введите а: '))
b = int(input('введите b: '))
c = int(input('введите c: '))
print('Это треугольник' if Triangle(a, b, c) else "Это не треугольник")

# from math import hypot

# def triangle(a, b, c):
#     # if c == (a*a + b*b) * 0.5:
#     if c == int(hypot(a, b)):
#         print('Треугольник получится')
#         return True
#     else:
#         print('Это не треугольник')
#         return False

# a = int(input(' Введите длину катета a: '))
# b = int(input(' Введите длину катета b: '))
# c = int(input(' Введите длину гипотенузы c: '))
# triangle(a, b, c)

# print((lambda a: a[0] + a[1] > a[2] )(sorted(triangle)))