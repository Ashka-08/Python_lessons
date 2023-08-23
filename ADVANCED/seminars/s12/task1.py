# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.


# v1 с синглотоном

class Factorial:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._arg_archive = []
            cls._instance._number_archive = []
            cls._instance._factorial = 1
        return cls._instance

    def __call__(self, num):
        self._arg_archive.append(num)
        self.num = num
        factorial = 1
        for i in range(num):
            factorial *= (i + 1)
        self._number_archive.append(factorial)
        return factorial


    def __str__(self):
        return f'{self._arg_archive}, {self._number_archive}'

    def number_archive(self):
        return self._arg_archive, self._number_archive


fac = Factorial()

print(fac(3))
print(fac(4))
print(fac(5))
print(fac.number_archive())


# v2 

class Factorial:

    def __init__(self):
        self._arg_archive = []
        self._number_archive = []
        self._factorial = 1

    def __call__(self, num):
        self._arg_archive.append(num)
        self.num = num
        factorial = 1
        for i in range(num):
            factorial *= (i + 1)
        self._number_archive.append(factorial)
        return factorial

    def __str__(self):
        return f'{self._arg_archive}, {self._number_archive}'

    def number_archive(self):
        return self._arg_archive, self._number_archive


fac = Factorial()
fac1 = Factorial()

print(fac(3))
print(fac1(4))
print(fac1(5))
print(fac.number_archive())
print(fac1.number_archive())
