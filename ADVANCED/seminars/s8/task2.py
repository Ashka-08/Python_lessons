# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.



import json

def bd_maker(filename):
    while True:
        str_inp = input('Введите имя, айди, уровень доступа: ')
        if str_inp:
            name, pers_id, level = str_inp.split()
            level = int(level)
            if not 0 < level < 8:
                print('Ошибка')
                continue
            with open(filename, 'r') as f:
                try:
                    data = json.load(f)
                except:
                    data = {}
            if str(level) not in data and pers_id not in data:
                data[level] = {pers_id : name}
            elif pers_id in data:
                print('Этот id уже добавлен в базу')
                continue
            elif str(level) in data:
                data[str(level)][pers_id] = name
            else:
                print('Ошибка добавления')
                continue
            with open(filename, 'w', encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            return data 


filename = 'ADVANCED\seminars\s8\my_file.json'
bd_maker(filename)
