# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# * загрузка данных (функция из задания 4)
# * вход в систему - требует указать имя и id пользователя. 
#     Для проверки наличия пользователя в множестве используйте магический метод 
#     проверки на равенство пользователей. Если такого пользователя нет, 
#     вызывайте исключение доступа. А если пользователь есть, 
#     получите его уровень из множества пользователей.
# * добавление пользователя. Если уровень пользователя меньше, 
# чем ваш уровень, вызывайте исключение уровня доступа.

import json
import os.path

from task6 import UserLevelError, UserPermissionError

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


    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.pers_id == other.pers_id
        return NotImplemented



def user_create():
    user_list = []
    with open('ADVANCED\seminars\s13\json_file.json', 'r', encoding='utf-8') as f_read:
        data = json.load(f_read)
    for firstname, values in data.items():
        lastname, sex, age, lvl_id, pers_id = values
        user_list.append(Employee(firstname, lastname, sex, age, pers_id))
    return user_list


class Login():
    def user_login(self, user_name, user_id):
        try:
            with open('ADVANCED\seminars\s13\json_file.json', 'r', encoding='utf-8') as f_read:
                data = json.load(f_read)
            for firstname, values in data.items():
                lastname, sex, age, lvl_id, pers_id = values
                curr_user = Employee(firstname, lastname, sex, age, pers_id)
                if firstname == user_name and pers_id == user_id:
                    user_from_base = Employee(firstname, lastname, sex, age, pers_id)
                    return curr_user.lvl_id
        except:
            raise UserPermissionError(user_id)

    def user_creator(self, data, creator_lvl):
        new_user = Employee(*data)
        print(data)
        print(new_user)
        if new_user.lvl_id >= creator_lvl:
            return new_user
        else:
            raise UserLevelError(creator_lvl)



e1 = Employee('Вася', 'Иванов', 'М', 30, '123456')
e2 = Employee('Петя', 'Петров', 'М', 25, '654321')
e3 = Employee('Глафира', 'Вениаминовна', 'Ж', 41, '999999')
e4 = ('Антон', 'Анатольевич', 'М', 24, '123456')


us1 = Login()
print(us1.user_creator(e4, us1.user_login('Глафира', '999999')))
# print(e1)
# print(e2)
# print(e3)