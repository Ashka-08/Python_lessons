class UserException(Exception):
    pass
    

class UserNegativeSideRectangleError(UserException):
    """Класс ошибки создания прямоугольника со сторонами отрицательной длины
    Принимает в качестве аргумента при вызове сторону с ошибкой"""

    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        string = f'Нельза создать прямоугольник со сторонами отрицательной длины!\n'\
                f'Ошибка здесь: {self.value}'
        return string


class UserMatrixSizeError(UserException):
    """Класс ошибки размера матрицы
    Принимает в качестве аргумента при вызове количество строк или столбцов, 
    которые содержат значение не более 1"""

    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        string = f'Матрица должна содержать более 1 строк и более 1 столбца!\n'\
                f'Ошибка здесь: {self.value}'
        return string


class UserNotEqualsMatrix(UserException):
    """Класс ошибки в случае сравнения размеров двух матриц.
    Принимает в качестве аргумента при вызове количество строк или столбцов, 
    обеих матриц, которые не равны между собой"""

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __str__(self):
        string = f'Матрицы должны быть равных размеров! Размер одной {self.value1}, '\
            f'а другой {self.value2}'
        return string


class UserEqualsClassesError(UserException):
    """Класс ошибки в случае сравнения двух классов.
    Принимает в качестве аргумента при вызове 
    тип одного из сравниваемых объектов"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Объекты должны быть экземплярами одного класса! Ошибка здесь: {self.value}'


class UserUserNotMultipleSumError(UserException):
    """Класс ошибки в случае ввода суммы, не кратной 50.
    Принимает в качестве аргумента при вызове 
    тип одного из сравниваемых объектов"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Сумма должна быть кратна 50! Ошибка здесь: {self.value}'

class UserIntSumError(UserException):
    """Класс ошибки в случае ввода не целочисленного числа.
    Принимает в качестве аргумента при вызове введенное число"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Сумма должна быть целым числом! Ошибка здесь: {self.value}'