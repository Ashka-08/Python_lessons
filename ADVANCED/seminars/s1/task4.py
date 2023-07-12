# Решите квадратное уравнение 5x2-10x-400=0 последовательно
# сохраняя переменные a, b, c, d, x1 и x2.
# *Попробуйте решить уравнения с другими значениями a, b, c.

print('Решаем квадратное уравнение вида ax^2+bx+c=0')
a = int(input('Введите a: '))
print('a = ', a)
b = int(input('Введите b: '))
print('b = ', b)
c = int(input('Введите c: '))
print('c = ', c)

print(f'Решаем квадратное уравнение {a}x^2+{b}x+{c}=0')
# print('Решаем квадратное уравнение {}x^2+{}x+{}=0'.format(a, b, c))
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
    if discriminant < 0:
        print('нет решения')
    elif discriminant == 0:
        x1 = -b / (2 * a)
        print(f'у уравнения только 1 корень х1 = {x1}')
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print(f'1 корень х1 = {x1}')
        print(f'2 корень х2 = {x2}')