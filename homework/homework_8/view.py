def hello_message():
    print('Программа запущена\n')

def show_menu():
    print(
        'Меню:\n'
        '1 - добавление сотрудника   2 - удаление сотрудника по id\n'
        '3 - поиск по фамилии        4 - поиск по должности         5 - поиск по зарплате\n'
        '6 - импорт в json           7 - импорт в csv \n'
        '8 - экспорт из json         9 - экспорт из csv \n'
        '10 - просмотр всего списка  0 - выход\n'
        )
    return int(input('Выберите номер пункта: '))

def input_person(data_base):
    print('Добавление сотрудника:')
    new_employee = {}
    new_employee['id'] = len(data_base)+1
    new_employee['first_name'] = input('Введите Имя: ')
    new_employee['last_name'] = input('Введите Фамилию: ')
    new_employee['phone_number'] = input('Введите номер телефона: ')
    new_employee['pozition'] = input('Введите должность: ')
    new_employee['b_date'] = input('Введите дату рождения: ')
    new_employee['salary'] = float(input('Введите заработную плату: '))
    print(f'\nВведены данные:\n{new_employee}\n')
    return(new_employee)
    
def input_last_name():
    return input('Введите фамилию сотрудника для поиска: ')

def input_id_to_del():
    return int(input('Введите id сотрудника для удаления: '))    

def input_id_change():
    return int(input('Введите id сотрудника для удаления: '))

def input_key_change():
    return input('Выберите ключ для редактирования: ')

def input_position():
    return input('Введите должность сотрудников для поиска: ')

def input_min_salary():
    return int(input('Выберите min размер зарплаты: '))

def input_max_salary():
    return int(input('Выберите max размер зарплаты: '))

def success_message():
    print("\nВыполнено успешно\n")

def error_message():
    print("\nОшибка\n")

def save_message():
    return int(input('Сохранить изменения?   0 - нет   1 - да: '))

def print_data(data_base):
    for i in data_base:
        print(i)