# ✔ Создайте функцию для сортировки файлов по директориям: 
# видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, 
# которые не подошли для сортировки.

import os


def replace_files():
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


replace_files()


# с семинара, сортирует по папкам по расширениям
# def replace_files():
#     for file in os.listdir():
#         extention = file.split('.')[-1]
#         if not os.path.exists(extention):
#             os.mkdir(extention)
#         os. replace(file, os.path.join(os.getcwd(), extention, file))