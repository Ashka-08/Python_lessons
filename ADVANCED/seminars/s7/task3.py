# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, 
# возвращайтесь в его начало.

from itertools import cycle

with (
    open('s7_task1.txt', 'r', encoding='utf-8') as examples,
    open('s7_task2.txt', 'r', encoding='utf-8') as names,
    open('s7_task3.txt', 'w', encoding='utf-8') as res
    ):

    names_size = len(list(1 for _ in names))
    nums_size = len(list(1 for _ in examples))
    count = max(names_size, nums_size)

    names_str = cycle(names.readlines())
    examples_str = cycle(examples.readlines())

    for _ in range(count):
        num1, num2 = next(examples_str).split('|')
        prod = float(num1) * float(num2)
        if prod < 0:
            res.write(f'{next(names_str).strip().lower()} {abs(prod)}\n')
        else:
            res.write(f'{next(names_str).strip().upper()} {round(prod)}\n')