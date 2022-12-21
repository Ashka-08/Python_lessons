# add_to_database, export_csv, exoprt_json
import json
import csv

def read_database():
    file = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_8/database.json'
    with open(file, 'r', encoding='utf-8') as base:
        data_base = json.load(base)
    return(data_base)

def exoprt_json():
    file = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_8/export.json'
    with open(file, 'r', encoding='utf-8') as export_file:
        employees = json.load(export_file)
        print('Извлечены следующие данные: ')
        for employee in employees:
            print(employee)
    return employees
        
def add_to_database(data_base, new_data):
    file = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_8/database.json'
    data_base.append(new_data)
    with open(file, 'w', encoding='utf-8') as base:
        json.dump(data_base, base, indent=3)

# def id_count(data):
#     file = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_8/database.json'
#     with open(file, 'r', encoding='utf-8') as export_file:
#         employees = json.load(export_file)
        
def export_csv() -> list:
    employee = []
    with open('database.csv', 'r', encoding='utf-8') as base:
        csv_reader = csv.reader(base)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["position"] = row[3]
            temp["phone_number"] = row[4]
            temp["salary"] = float(row[5])
            employee.append(temp)
    return employee
        
        