# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def tuple_maker(data):
    *path, file = data.split('/')
    path = '/'.join(path)
    filename, extension = file.split('.')
    return path, filename, extension


data = 'C:/Users/Professional/Desktop/geekbrain/Python/README.md'
print(tuple_maker(data))