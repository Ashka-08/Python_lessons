# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её 
# и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий 
# размер файлов в ней с учётом всех вложенных файлов и директорий.

import os
import csv
import json
import pickle
import sys


def walk_and_save(dir):
    result = {}
    for dir_path, dirname_name, filename_list in os.walk(dir):
        if dirname_name:
            for dir in dirname_name:
                result[dir] = \
                    {
                        'is' : 'dir',
                        'parent_dir' : dir_path,
                        'size' : sys.getsizeof(dir)
                    }
        if filename_list:
            for file in filename_list:
                result[file] = \
                    {
                        'is' : 'file',
                        'parent_dir' : dir_path,
                        'size' : sys.getsizeof(file)
                    }
    return result

def save_to_json(file: str, data: dict):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_to_csv(file: str, data: dict):
    with open(file, 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f, delimiter=',')
        columns = ['name','is','parent_dir','size']
        csv_writer.writerow(columns)
        for k, values in data.items():
            lst = []
            lst.append(k)
            for v in values.values():
                lst.append(v)
            csv_writer.writerow(lst)
    
def save_to_pickle(file: str, data: dict):
    with open(file, 'wb') as f:
        pickle.dump(data, f)
            

data = walk_and_save('ADVANCED\lessons')
save_to_json('ADVANCED\homeworks\hw8\my_file.json', data)
save_to_csv('ADVANCED\homeworks\hw8\my_file.csv', data)
save_to_pickle('ADVANCED\homeworks\hw8\my_file.pickle', data)
