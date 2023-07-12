# Загадать число от 0 до 1000. LOWER_LIMIT, UPPER_LIMIT
# Программе необходимо угадать это число за 10 попыток. 
# Программа должна спрашивать «больше» или «меньше» после каждой попытки. 

from random import randint 

TRY = 10
count = 1
lower_limit = 0
upper_limit = 1000
print(f'Привет, я бот! Загадайте число от {lower_limit} до {upper_limit} не включительно, ' 
        f'я попробую угадать его за {TRY} попыток')

while count < TRY:
    count += 1
    num = randint(lower_limit, upper_limit)
    print(f'Загаданное число {num}?')

    answer = int(input('Введите: 0 - если меньше, 1 - если больше, 2 - если угадал: '))
    if answer == 2:
        print(f'Отлично! Угадано за {count} попыток(ки) (=^.^=)')
        break
    elif answer == 1:
        print(f'Больше?! Осталось {TRY-count} попыток(ки)')
        lower_limit = num
        continue
    elif answer == 0:
        print(f'Меньше?! Осталось {TRY-count} попыток(ки)')
        upper_limit = num
        continue
    else:
        print('Какая-то ошибка ввода, попробуем еще раз')
        continue

print('Игра закончилась!')