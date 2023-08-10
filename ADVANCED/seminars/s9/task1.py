# Создайте функцию-замыкание, которая запрашивает два целых числа:
# * от 1 до 100 для загадывания,
# * от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток. 

from random import randint

def main():
    upper_limit, find_try = int(input('Пределе? ')), int(input('Попыток? '))

    def guess_num():
        """
        Угадайка
        :param lower_limit: нижняя граница,
        :param upper_limit: верхняя граница,
        :param find_try: количество попыток
        """
        nonlocal upper_limit
        nonlocal find_try
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

a = main()
a()

# main()()