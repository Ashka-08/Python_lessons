def print_hello():
    print(
        'Меню справочника:\n'
        '1 - добавление записи \n'
        '2 - импорт в csv \n'
        '3 - импорт в txt\n'
        '4 - экспорт из txt\n'
        '5 - выход из приложения'
        )
    return int(input('Выберите номер пункта: '))

def print_add(info):
    print(f'Введены данные:\n{info[0]};{info[1]};{info[2]};{info[3]}')
    print('\nЗапись данных в базе создана\n')

def success():
    print("\nВыполнено успешно\n")