def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]   
    with open('file', 'r') as file:
        for line in file:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)


def write_txt(filename: str, data: list):
    with open('file', 'w') as file:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            file.write(f'{s[:-1]}\n')

def find_by_name(data: list, last_name: str) -> str:
    for el in data:
        if el.get('Фамилия') == last_name:
            return el.get('Телефон')
    return 'Такой абонент отсутствует'

def find_by_number(data: list, phone_number: str) -> str:
    for el in data:
        if el.get('Телефон') == phone_number:
            return f"{el.get('Фамилия')}, {el.get('Имя')}"
    return 'Такой телефон отсутствует'

def add_user(data: list, user_data: str):
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)

def export_data():
    with open('file_1.txt', 'r') as file:
        data = []
        t = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
            elif ':' in line:
                temp = line.strip().split(':')
                data.append(temp)        
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t= []
    return data

def search_data(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None