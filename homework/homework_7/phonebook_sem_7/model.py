def add_record(info):
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = input('Введите номер: ')
    info.append(phone_number)
    note = input('Введите описание: ')
    info.append(note)
    return info

def import_scv():
    file = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_7/phonebook_sem_7/Phonebook.csv'
    with open (file, 'a') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def import_txt():
    file = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_7/phonebook_sem_7/Phonebook.txt'
    with open (file, 'a') as data:
        data.write(f'Фамилия: {info[0]}\nИмя: {info[1]}\nНомер телефона: {info[2]}\nОписание: {info[3]}\n\n')