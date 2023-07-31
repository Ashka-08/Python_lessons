# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


# отправлено на проверку
def tuple_maker(data):
    *path, file = data.split('/')
    path = '/'.join(path)
    filename, extension = file.split('.')
    return path, filename, extension


data = 'C:/Users/Professional/Desktop/geekbrain/Python/README.md'
print(tuple_maker(data))


# решение от преподавателя
import os

path = 'D:\WorkShopPy\Dive_into_Python\Work_05\HomeWork_01.py'

full_path, file = os.path.split(path)
name, extension = file.rsplit('.', 1)
print(full_path, name, extension, sep='\n')