# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import pickle
import csv

def pickle_to_csv(file1, file2):
    with (
        open(file1, 'rb') as f1,
        open(file2, 'w', encoding='utf-8', newline='') as f2
    ):
        data: dict = pickle.load(f1)
        head = data.keys()
        writer = csv.writer(f2, delimiter=';')
        writer.writerow(head)
        for key, values in data.items():
            a, b = tuple(*values.values())
            writer.writerow([*(values.keys()), a, b])


file1 = 'ADVANCED\seminars\s8\my_file2.pickle'
file2 = 'ADVANCED\seminars\s8\my_file2.csv'
pickle_to_csv(file1, file2)