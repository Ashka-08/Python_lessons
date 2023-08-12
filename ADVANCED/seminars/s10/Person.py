# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, 
# full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, 
# но есть возможность получить текущий возраст

class Person:

    def __init__(self, firstname, lastname, sex, age):
        self.firstname = firstname
        self.lastname = lastname
        self.sex = sex
        self.__age = age

    def birthday(self):
        self.__age += 1
        return f'С Днем рождения, {self.firstname}. Возраст увеличен на 1 год'

    def full_name(self):
        return f'{self.firstname} {self.lastname} {self.sex}'

    def get_age(self):
        return self.__age


p1 = Person('Вася', 'Иванов', 'М', 30)

print(p1.get_age())
print(p1.birthday())
print(p1.get_age())
print(p1.full_name())
print(p1._Person__age)
# print(p1.__age)