# Задание 5
# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# * декораторами для сохранения параметров,
# * декоратором контроля значений и
# * декоратором для многократного запуска.
# Выберите верный порядок декораторов.

# Задание 6
# Доработайте прошлую задачу добавив декоратор wraps в
# каждый из декораторов.


import json
from random import randint
from functools import wraps

def json_saver(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open(f'ADVANCED\seminars\s9\{func.__name__}.json', 'a', encoding='utf-8') as file:
            temp_dict = {'args' : args}
            temp_dict.update(kwargs)
            result = func(*args, **kwargs)
            temp_dict['result'] = result
            json.dump(temp_dict, file, ensure_ascii=False, indent=2)
        return result
    return wrapper


def call_count(num):
    def decorator(func):
        result = []
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result.append(func(*args, **kwargs))
            return result
        
        return wrapper
    
    return decorator


def value_control(func):
    upper_limit, find_try = int(input('Пределе? ')), int(input('Попыток? '))
    @wraps(func)
    def wrapper(upper_limit, find_try):
        if not 0 < upper_limit < 100:
            upper_limit = randint(1, 100)
        if not 0 < find_try < 10:
            find_try = randint(1, 10)
        func(upper_limit, find_try)
    
    return wrapper

@call_count(3)
@value_control
@json_saver
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


guess_num(50, 3)