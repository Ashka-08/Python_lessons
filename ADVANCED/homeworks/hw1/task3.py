# Программа загадывает число от 0 до 1000. 
# Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код: 
# from random import randint 
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint 

num = randint(0, 1000)
print('Число от 0 до 1000 сгенерировано. Попробуйте угадать за 10 попыток это число')
TRY = 10
count = 1

while count < TRY:
    count += 1
    answer = int(input('Введите число: '))
    if answer == num:
        print(f'Верно! Угадано за {count} попыток(ки)')
        break
    elif answer < num:
        print(f'Больше! Осталось {TRY-count} попыток(ки)')
        continue
    else:
        print(f'Меньше! Осталось {TRY-count} попыток(ки)')
        continue
    
print(f'Загаданное число {num}')