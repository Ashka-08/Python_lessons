from random import randint 

def guess_num(lower_limit, upper_limit, find_try):
    """
    Угадайка
    :param lower_limit: нижняя граница,
    :param upper_limit: верхняя граница,
    :param find_try: количество попыток
    """
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


if __name__ == '__main__':
    guess_num(1, 10 , 3)