# Создайте класс Матрица.
# Добавьте методы для:
# * вывода на печать,
# * сравнения,
# * сложения,
# * *умножения матриц

from random import randint


class Matrix:
    """Класс Матрица. Позволяет создавать экземпляры как в ручном режиме, 
    так и режиме рандомного заполнения"""

    def __init__(self, matrix=None):
        """Метод создания экземпляра класса Матрица.
        :param: matrix - список списков. 
        Если не передать вызовет метод create_matrix()
        """
        if matrix != None:
            self.matrix = matrix
        else:
            self.matrix = self.create_matrix()
        self._rows = len(self.matrix)
        self._cols = len(self.matrix[0])

    def check_size(self, other):
        """Метод сравнения размеров двух матриц"""
        return self._rows == other._rows and self._cols == other._cols

    def __eq__(self, other):
        """Метод сравнения двух матриц"""
        if self is other:
            return True
        if not isinstance(other, Matrix): 
            raise TypeError('Сравниваемые должны быть одного класса')
        if self.check_size(other):
            for i in range(self._rows):
                for j in range(self._cols):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        return False
        else:
            raise ValueError('Размер матриц не совпадает')
        return True

    def __add__(self, other):
        """Метод сложения двух матриц"""
        if isinstance(other, Matrix):
            if self.check_size(other):
                res = []
                for i in range(self._rows):   
                    row = [self.matrix[i][j] + other.matrix[i][j] for j in range(self._cols)]
                    res.append(row)
                return Matrix(res)
            else:
                raise ValueError('Размер матриц не совпадает')
        else:
            raise TypeError('Слагаемые должны быть одного класса')
    
    def __sub__(self, other):
        """Метод вычитания двух матриц"""
        if isinstance(other, Matrix):
            if self.check_size(other):
                res = []
                for i in range(self._rows):   
                    row = [self.matrix[i][j] - other.matrix[i][j] for j in range(self._cols)]
                    res.append(row)
                return Matrix(res)
            else:
                raise ValueError('Размер матриц не совпадает')
        else:
            raise TypeError('Вычитаемые должны быть одного класса')

    def __mul__(self, other):
        """Метод умножения двух матриц"""
        if isinstance(other, Matrix):
            if self.check_size(other):
                res = [[sum(one * two for one, two in zip(one_row, two_col)) 
                        for two_col in zip(*other.matrix)]
                          for one_row in self.matrix]
                res = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
                for i in range(self._rows):
                    for j in range(self._cols):
                        for k in range(other._rows):
                            res[i][j] += self.matrix[i][k] * other.matrix[k][j]
                return Matrix(res)
            else:
                raise ValueError('Размер матриц не совпадает')
        else:
            raise TypeError('Множители должны быть одного класса')

    def create_matrix(self):
        """Метод наполнения матрицы элементами с помощью рандома"""
        res = []
        rows = randint(1, 5)
        cols = randint(1, 5)
        for _ in range(rows):   
            a = []
            for _ in range(cols):  
                a.append(randint(-10, 10))
            res.append(a)
        return res
    
    def __str__(self):
        """Метод строкового представления класса Матрица"""
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix]) + '\n'
    
    def __repr__(self):
        """Метод представления класса Матрица"""
        return f'Matrix({self.matrix})'


print(matr1 := Matrix([[1,2, 3, 4], [-1, -2, -3 , -4], [1, 1, 1, 1]]))
print(matr2 := Matrix([[5, 6, 7, 8], [-5, -6, -7 , -8], [2, 2, 2, 2]]))
print(repr(matr3 := matr2))

print(matr1 + matr2)
print(matr2 - matr1)
print(matr1 * matr2)

print(matr1 == matr2)
print(matr2 == matr3)