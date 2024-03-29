# Напишите функцию группового переименования файлов. Она должна:
# * принимать параметр желаемое конечное имя файлов. 
#       При переименовании в конце имени добавляется порядковый номер.
# * принимать параметр количество цифр в порядковом номере.
# * принимать параметр расширение исходного файла. 
#       Переименование должно работать только для этих файлов внутри каталога.
# * принимать параметр расширение конечного файла.
# * принимать диапазон сохраняемого оригинального имени. 
#       Например для диапазона [3,6] берутся буквы с 3 по 6 из исходного имени файла. 
#       К ним прибавляется желаемое конечное имя, если оно передано. 
#       Далее счётчик файлов и расширение. 
# Соберите из созданных на уроке и в рамках домашнего задания функций 
# пакет для работы с файлами.

import os


def rename_group_files(new_name= '', 
                        count_digits= 2, 
                        extention= 'jpg', 
                        new_extention= 'jpg', 
                        span_names= (0,0)):
    """
    Функция группового переименования файлов.
    :param: new_name желаемое конечное имя файлов,
    :param: count_digits количество цифр в порядковом номере,
    :param: extention расширение исходного файла,
    :param: new_extention расширение конечного файла,
    :param: span_names диапазон сохраняемого оригинального имени
    """
    count = 0
    for file in os.listdir():
        c_name, c_extention = file.split('.')
        if extention == c_extention:
            res = ''
            if new_name:
                res += f'{new_name}_'
            if span_names:
                res += f'{c_name[span_names[0]:span_names[1]]}_'
            res += f'{count:0>{count_digits}}.{new_extention}' 
            os.rename(file, res)
            count += 1


if __name__ == '__main__':
    rename_group_files(new_name='image', count_digits=3, span_names=(1,4))