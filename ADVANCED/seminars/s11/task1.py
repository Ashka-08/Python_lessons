# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

# Задание №3
# Добавьте к задачам 1 и 2 строки документации для классов.

import time
from getpass import getuser


class MyString(str):
    """Класс Моя Строка, где:
    * доступны все возможности класса str,
    * дополнительно хранятся имя автора строки и время создания (time.time)"""

    def __new__(cls, *args, **kwargs):
        """ Создание класса с присвоением параметров:
        :param: name - имя автора строки
        :param: time_val - время создания (time.time)"""
        instance = super().__new__(cls, *args, **kwargs)
        instance.name = getuser()
        instance.time_val = time.time()
        return instance

    def __init__(self, str_val):
        """Создание экземпляра класса Моя Строка"""
        self.str_val = str_val
    
    def __str__(self) -> str:
        """Переопределение метода str
        :return: Строка с данными"""
        return f'{self.str_val = }, username = {self.name}, time = {self.time_val}'


print(a := MyString('Строка'))
print(b := MyString('hello world'))