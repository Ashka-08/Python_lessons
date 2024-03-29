# Напишите программу, которая решает квадратные уравнения даже если 
# дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.
# для примера x^2-6x+13=0

print('Решаем квадратное уравнение вида ax^2+bx+c=0')
a = int(input('Введите a: '))
print('a = ', a)
b = int(input('Введите b: '))
print('b = ', b)
c = int(input('Введите c: '))
print('c = ', c)

print(f'Решаем квадратное уравнение {a}x^2+{b}x+{c}=0')

if a == 0:
    if b == 0:
        if c == 0:
            print("бесконечное число корней")
        else: 
            print("ошибка записи")
    else:
        print(f'линейное уравнение {b}x+{c}=0')
        print(f'у уравнения только 1 корень х1 = {-c / b}')
else:
    discriminant = b ** 2 - 4 * a * c
    if discriminant == 0:
        x1 = -b / (2 * a)
        print(f'у уравнения только 1 корень х1 = {x1}')
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print(f'1 корень х1 = {x1}')
        print(f'2 корень х2 = {x2}')

