# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json


def transform_file_to_json(filename):
    with (
        open(filename, 'r', encoding='utf-8') as f1,
        open(f'ADVANCED\seminars\s8\{filename}.json', 'w', encoding='utf-8') as f2
        ):
        data = f1.readlines()
        dict_to_save = {}
        for line in data:
            key, value = line.strip().split(' ')
            if key.title() in dict_to_save.keys():
                dict_to_save[key.title()].append(value)
            else:
                dict_to_save[key.title()] = [value]
        json.dump(dict_to_save, f2, ensure_ascii=False, indent=2)


filename = 's7_task3.txt'
transform_file_to_json(filename)