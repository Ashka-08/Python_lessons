# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа 
# в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.


from random import randint

def value_control(func):
    upper_limit, find_try = int(input('Пределе? ')), int(input('Попыток? '))
    
    def wrapper(upper_limit, find_try):
        if not 0 < upper_limit < 100:
            upper_limit = randint(1, 100)
        if not 0 < find_try < 10:
            find_try = randint(1, 10)
        func(upper_limit, find_try)
    
    return wrapper


@value_control
def guess_num(upper_limit, find_try):
    lower_limit = 1
    num = randint(lower_limit, upper_limit)
    print(f'Угадай число от {lower_limit} до {upper_limit} за {find_try} попыток')

    while find_try > 0:
        answer = int(input('Введите число: '))
        find_try -= 1
        if answer == num:
            print(f'Верно!')
            break
        elif answer < num:
            print(f'Больше! Осталось {find_try} попыток(ки)')
            continue
        else:
            print(f'Меньше! Осталось {find_try} попыток(ки)')
            continue
            
    print(f'Загаданное число {num}')
    return guess_num

guess_num(10, 5)