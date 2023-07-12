def hello_message():
    print('Программа запущена\n')

def show_menu():
    print(
        'Меню:\n'
        '0 - добавление сотрудника   1 - удаление сотрудника по id  2 - редактирование\n'
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
    
def change_employee(data_base):
    id_change = int(input('Введите id сотрудника для редактирования: '))
    print(data_base[id_change-1])
    print('Пункты, доступные для редактирования:')
    print('id, first_name, last_name, phone_number, position, b_date, salary')
    key_change = input('Выберите пункт для редактирования: ')
    i = id_change - 1
    if key_change == 'id':
        data_base[i]['id'] = int(input('Введите id: '))
    if key_change == 'first_name':
        data_base[i]['first_name'] = input('Введите имя: ')
    if key_change == 'last_name':
        data_base[i]['last_name'] = input('Введите фамилию: ')
    if key_change == 'phone_number':
        data_base[i]['phone_number'] = input('Введите номер телефона: ')
    if key_change == 'position':
        data_base[i]['position'] = input('Введите должность: ')
    if key_change == 'b_date':
        data_base[i]['b_date'] = input('Введите дату рождения: ')
    if key_change == 'salary':
        data_base[i]['salary'] = int(input('Введите заработную плату: '))
    print(f'Внесены следующие изменения:\n')
    print(data_base[id_change - 1])
    return data_base

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