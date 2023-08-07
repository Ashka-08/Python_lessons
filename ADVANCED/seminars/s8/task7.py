# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

import csv
import pickle

def csv_to_bin_str(file1):
    with open(file1, 'r') as f1:
        csv_file = csv.reader(f1, delimiter=';')
        next(csv_file)
        new_dict = {}
        for level, pers_id, name in csv_file:
            pers_id = pers_id.rjust(10,'0')
            name = name.title()
            hash_id = hash(name + pers_id)
            new_dict[hash_id] = {pers_id: [name, level]}
        print(pickle.dumps(new_dict))


file1 = 'ADVANCED\seminars\s8\my_file2.csv'
csv_to_bin_str(file1)