# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков архивов
# list-архивы также являются свойствами экземпляра

# Задание №3
# Добавьте к задачам 1 и 2 строки документации для классов.

# Задание №4
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.


class Archive:
    """Класс Архив, который хранит пару свойств: число и строку.
    При нового экземпляра класса, старые данные из ранее
    созданных экземпляров сохраняются в пару списков архивов
    list-архивы также являются свойствами экземпляра"""

    _instance = None

    def __new__(cls, string, number):
        """Это создание потомка
        :param string: Это в архив строк
        :param number: Это в архив чисел"""

        if cls._instance is None:
            cls._instance = super().__new__(cls)     
            cls._instance._string_archive = []
            cls._instance._number_archive = []
        else:
            cls._instance._string_archive.append(cls._instance.string)
            cls._instance._number_archive.append(cls._instance.number)
        return cls._instance

    def __init__(self, string, number):
        """Создание экземпляра класса
        :param string: Это в архив строк
        :param number: Это в архив чисел"""
        self.string = string
        self.number = number

    def __str__(self):
        """Переопределение метода str
        :return: Строка с данными"""
        return f"{self.number, self.string}"

    def __repr__(self):
        """Переопределение метода str
        :return: Строка с данными"""
        return f'Archive("{self.string}", {self.number})'

    def string_archive(self):
        """Архивация строк
        :return: Архив строк"""
        return self._string_archive
    
    def number_archive(self):
        """Архивация чисел
        :return: Архив чисел"""
        return self._number_archive
    

print(first := Archive('a', 1))
print(first.string_archive(), first.number_archive(), end='\n\n')

print(second := Archive('b', 2))
print(second.string_archive(), second.number_archive(), end='\n\n')

print(third := Archive('c', 3))
print(third.string_archive(), third.number_archive())

print(repr(third))

my_list = [first, second, third]
print(my_list, end='\n\n')
print(*my_list)