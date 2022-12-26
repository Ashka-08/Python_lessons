# add_to_database, export_csv, exoprt_json
import json
import csv

def read_database():
    file = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_8/database.json'
    with open(file, 'r', encoding='utf-8') as base:
        data_base = json.load(base)
    return(data_base) 

def add_to_data_base(new_employee, data_base):
    data_base.append(new_employee)
    return(data_base)

def export_json(data_base):
    file = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_8/export.json'
    with open(file, 'r', encoding='utf-8') as export_file:
        employees = json.load(export_file)
        print('В базу экспортированы данные с заменой id на последующие: ')
        n = len(data_base) + 1
        for employee in employees:
            employee['id'] = n
            n += 1
            print(employee)
            data_base.append(employee)
        print('')
    return(data_base)
        
def save_database(data_base):
    file = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_8/database.json'
    with open(file, 'w', encoding='utf-8') as base:
        json.dump(data_base, base, indent=3)

def import_json(data_base):
    file = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_8/import.json'
    with open(file, 'w', encoding='utf-8') as base:
        json.dump(data_base, base, indent=3)
        
def export_csv(data_base):
    file = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_8/export.csv'
    with open(file, 'r', encoding='utf-8') as export_file:
        data = csv.reader(export_file)
        n = len(data_base) + 1
        print('В базу экспортированы данные с заменой id на последующие: ')
        for row in data:
            employee = {}
            employee["id"] = n
            employee["first_name"] = row[1]            
            employee["last_name"] = row[2]
            employee["phone_number"] = row[3]            
            employee["position"] = row[4]
            employee["b_date"] = row[5]
            employee["salary"] = int(row[6])
            print(employee)
            data_base.append(employee)
            n += 1
    return data_base
        
def import_csv(data_base):
    file = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_8/import.csv'
    with open(file, 'w', encoding='utf-8') as base:
        data = csv.writer(base, delimiter=',', lineterminator='\r')
        data.writerow(["id", "first_name", "last_name", "phone_number", "position", "b_date", "salary"])
        for i in data_base:
            data.writerow(i.values())         

def search_employee(last_name, data_base):
    data = []
    for i in data_base:
        if i['last_name'] == last_name:
            data.append(i)
    return data

def search_position(position, data_base):
    data = []
    for i in data_base:
        if i['position'] == position:
            data.append(i)
    return data

def search_salary(min, max, data_base):
    for i in data_base:
        if min <= i['salary'] <= max:
            print(f"id = {i['id']} {i['first_name']} {i['last_name']}, ЗП = {i['salary']}")

def del_employee(data_base, id_to_del):
    i = id_to_del - 1
    print(f"Удаляемый id {data_base[i]['id']} {data_base[i]['last_name']}")
    data_base.pop(i)
    
def id_count(data_base):
    n = 1
    for i in data_base:
        i['id'] = n
        n += 1
    return data_base