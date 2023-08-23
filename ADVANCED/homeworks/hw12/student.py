# Создайте класс студента.
# * Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# * Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# * Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых. 

import csv


class CheckName:
    """Класс дескриптор для проверки ФИО при создании экземпляра класса Student"""

    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        """Метод проверки ФИО"""
        if not all(i.isalpha() for i in value):
            raise TypeError('Ошибка, должны быть только буквы')
        if not value.istitle():
            raise ValueError('Ошибка, ФИО должны быть с заглавной буквы')
        

class Student:
    first_name = CheckName()
    last_name = CheckName()
    patronymic = CheckName()

    def __init__(self, first_name, last_name, patronymic, filename):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.filename = filename
        self.__journal = self.__load_lessons()
        self.__tests = self.__load_lessons()

    def __load_lessons(self):
        """Метод загрузки словаря из файла csv с уроками в качестве ключей"""
        res = {}
        with open(self.filename, 'r', encoding='UTF-8') as f:
            csv_reader = csv.reader(f, delimiter='\n')
            for line in csv_reader:
                res[line[0]] = []
        return res
    
    @property
    def journal(self):
        return self.__journal

    @property
    def tests(self):
        return self.__tests

    @journal.setter
    def journal(self, value):
        raise AttributeError('Нельзя изменить журнал оценок')
    
    @tests.setter
    def tests(self, value):
        raise AttributeError('Нельзя изменить журнал тестирования')
    
    def add_marks(self, lesson, marks):
        """Метод добавления оценки к уроку"""
        if lesson not in self.__journal.keys():
            raise ValueError('Ошибка! Нет такого урока')
        if not all(str(i).isdigit() for i in marks):
            raise ValueError('Ошибка! Оценки должны быть числом')
        for item in marks:
            if item < 2 or item > 5:
                raise ValueError('Ошибка! Оценка должна быть от 2 до 5')
            self.__journal[lesson].append(item)
    
    def add_test_balls(self, lesson, balls):
        """Метод добавления результатов тестов к уроку"""
        if lesson not in self.__tests.keys():
            raise ValueError('Ошибка! Нет такого урока')
        if not all(str(i).isdigit() for i in balls):
            raise ValueError('Ошибка! Баллы должны быть числом')
        for item in balls:
            if item < 0 or item > 100:
                raise ValueError('Ошибка! Баллы должны быть от 0 до 100')
            self.__tests[lesson].append(item)

    def get_gpa(self):
        """Метод получения средней оценки по всем урокам"""
        summ = 0
        count = 0
        for v in self.__journal.values():
            summ += sum(i for i in v)
            count += len(v)
        return round(summ / count, 2)
    
    def get_av_tests_balls(self, lesson):
        """Метод получения среднего балла по результатам тестирования по уроку"""
        if lesson not in self.__tests.keys():
            raise ValueError('Ошибка! Нет такого урока')
        if len(self.__tests[lesson]) != 0:
            res = sum(self.__tests[lesson][i] for i in range(len(self.__tests[lesson])))
            res /= len(self.__tests[lesson])
            return res
        return -1

    def __repr__(self):
        return f'Student("{self.first_name} {self.last_name} {self.patronymic}")'


print(s1 := Student('Марванова', 'Любовь', 'Дмитриевна', 'ADVANCED\homeworks\hw12\lessons.csv'))
print(s1.journal)
s1.add_marks('Математика', [4,3,4,5,5,4,3])
s1.add_marks('Физика', [4,3,4,5,5,4,3])
s1.add_test_balls('Математика', [40,30,40,50,50,40,30])
print(s1.journal, s1.tests, sep='\n')
print(s1.get_gpa())
print(s1.get_av_tests_balls('Математика'))