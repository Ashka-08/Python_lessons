# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

import json
import os.path


class Person:

    def __init__(self, firstname, lastname, sex, age):
        self.firstname = firstname
        self.lastname = lastname
        self.sex = sex
        self.age = age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f'{self.firstname} {self.lastname} {self.sex}'

    def get_age(self):
        return self.__age


class Employee(Person):

    def __init__(self, firstname, lastname, sex, age, pers_id):
        if len(pers_id) != 6:
            raise ValueError('Некорректный id!')
        super().__init__(firstname, lastname, sex, age)
        self.pers_id = pers_id
        self.lvl_id = int(pers_id) % 7
        self.json_data = {self.firstname: [lastname, sex, age, self.lvl_id, pers_id]}
        self.save_in_files()

    def __str__(self):
        return f'{self.firstname}: уровень: {self.lvl_id}, ID: {self.pers_id}'

    def save_in_files(self):
        try:
            if not os.path.isfile('ADVANCED\seminars\s13\json_file.json') \
                or os.path.getsize('ADVANCED\seminars\s13\json_file.json') == 0:
                with open('ADVANCED\seminars\s13\json_file.json', 'w', encoding='utf-8') as f:
                    f.write('{}')
            with open('ADVANCED\seminars\s13\json_file.json', 'r', encoding='utf-8') as f_read:
                data = json.load(f_read)
                data.update(self.json_data)
            with open('ADVANCED\seminars\s13\json_file.json', 'w', encoding='utf-8') as f_write:
                json.dump(data, f_write, ensure_ascii=False, indent=2)
        except:
            return 'Ошибка записи!'

def user_create():
    user_list = []
    with open('ADVANCED\seminars\s13\json_file.json', 'r', encoding='utf-8') as f_read:
        data = json.load(f_read)
    for firstname, values in data.items():
        lastname, sex, age, lvl_id, pers_id = values
        user_list.append(Employee(firstname, lastname, sex, age, pers_id))
    return user_list


e1 = Employee('Вася', 'Иванов', 'М', 30, '123456')
e2 = Employee('Петя', 'Петров', 'М', 25, '654321')
e3 = Employee('Глафира', 'Вениаминовна', 'Ж', 41, '333555')

print(e1)
print(e2)
print(e3)

print(*user_create())