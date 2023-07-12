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

def write_base(info):
    file = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_7/phonebook_sem_7/Base.txt'    
    with open (file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def import_scv():
    base = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_7/phonebook_sem_7/Base.txt'
    with open (base, 'r', encoding='utf-8') as base:
        all = base.read()
    file = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_7/phonebook_sem_7/Phonebook.csv'
    with open (file, 'a', encoding='utf-8') as data:
        data.write(all)

def import_txt():
    base = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_7/phonebook_sem_7/Base.txt'
    with open (base, 'r', encoding='utf-8') as base:
        all = base.read()
    file = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_7/phonebook_sem_7/Phonebook.txt'
    with open (file, 'a', encoding='utf-8') as data:
        data.write(all)

def export_txt():
    file = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_7/phonebook_sem_7/export.txt'
    with open (file, 'r', encoding='utf-8') as data:
        all = data.readlines()
    base = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_7/phonebook_sem_7/Base.txt'
    with open (base, 'a', encoding='utf-8') as base:
        base.writelines(all)

def export_csv():
    export_csv = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_7/phonebook_sem_7/export.csv'
    with open (export_csv, 'r', encoding='utf-8') as file:
        data = []
        t = []
        for line in file:      
            if line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t= []
    file = 'C:/Users/Professional/Desktop/geekbrains/Python/homework/homework_7/phonebook_sem_7/Base.txt'    
    with open (file, 'a', encoding='utf-8') as base:
        for i in data:
            temp = ';'.join(i)
            print(temp)
            base.write(f'{temp}\n')