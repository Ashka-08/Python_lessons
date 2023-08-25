# Создайте функцию, которая запрашивает числовые данные от пользователя 
# до тех пор, пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения

def get_num():
    while True:
        try:
            num = float(input('Введите число: '))
            if num - int(num) == 0:
                num = int(num)
            break
        except ValueError:
            print('Ошибка ввода!')
    return num


print(get_num())