# task4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42 (в примере 3)
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

# task5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи

# task6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import os
from string import ascii_letters
from random import sample, randint, randbytes

def makefile(extention, smallest=6, largest=30, min_bytes=256, max_bytes=4096, count=3):
    names = set()
    while len(names) < count:
        names.add(''.join(sample(ascii_letters, randint(smallest, largest))))
    
    for name in names:
        with open(f'{name}.{extention}', 'wb') as file:
            temp = randbytes(randint(min_bytes, max_bytes))
            file.write(temp)
            print(len(temp))


def makefiles(**extentions):
    for extention, count in extentions.items():
        makefile(extention, count)


def makefile_to_path(path, extention):
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    makefile(extention)


# makefile('mp3') 

# temp = {'mp3':1, 'xml':1, 'json':1}
# makefiles(**temp)

# makefiles(mp3=1, xml=1, json=1)
makefiles(jpg=1)

# makefile_to_path('s7_test_dir', 'txt')