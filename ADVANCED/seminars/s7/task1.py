# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.


from random import randint, uniform

def input_nums(count, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        for i in range(count):
            f.write(f'{randint(-1000, 1000)}|{uniform(-1000, 1000)}\n')

input_nums(5, 's7_task1.txt')