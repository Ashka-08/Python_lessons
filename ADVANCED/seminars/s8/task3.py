# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import json
import csv

def json_to_csv(file1, file2):
    with (
        open(file1, 'r') as f1,
        open(file2, 'w', encoding='utf-8', newline='') as f2
    ):
        data = json.load(f1)
        columns = ['level', 'pers_id', 'name']
        writer = csv.writer(f2, delimiter=';')
        writer.writerow(columns)
        result = []
        for key, value in data.items():
            for i,j in value.items():
                result.append([key, i, j])
        writer.writerows(result)

file1 = 'ADVANCED\seminars\s8\my_file.json'
file2 = 'ADVANCED\seminars\s8\my_file.csv'
json_to_csv(file1, file2)