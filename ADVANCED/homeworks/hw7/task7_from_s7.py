# ✔ Создайте функцию для сортировки файлов по директориям: 
# видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, 
# которые не подошли для сортировки.

import os


def replace_files():
    """
    Функция сортировки файлов по директориям: 
    видео, изображения, текст, музыка
    по их расширениям.
    """
    diction = {
            'video' : ['avi', 'wav', 'mov'],
            'text' : ['txt', 'doc', 'xml', 'json'],
            'image' : ['jpeg', 'jpg', 'png'],
            'music' : ['mp3']
        }
    for file in os.listdir():
        extention = file.split('.')[-1]
        print(extention)
        for k, v in diction.items():
            if not os.path.exists(k):
                os.mkdir(k)
            if extention in v:
                os.replace(file, os.path.join(os.getcwd(), k, file))

if __name__ == '__main__':
    replace_files()