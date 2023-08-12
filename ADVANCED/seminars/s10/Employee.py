# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# * шестизначный идентификационный номер
# * уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

from Person import Person

class Employee(Person):

    def __init__(self, firstname, lastname, sex, age, pers_id):
        if len(pers_id) != 6:
            raise ValueError('Некорректный id!')
        super().__init__(firstname, lastname, sex, age)
        self.pers_id = pers_id
        self.lvl_id = int(pers_id) % 7

    def __str__(self):
        return f'{self.firstname}: уровень: {self.lvl_id}, ID: {self.pers_id}'


e1 = Employee('Вася', 'Иванов', 'М', 30, '123456')
print(e1)