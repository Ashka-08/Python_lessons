from random import randint
from error import UserMatrixSizeError, UserNotEqualsMatrix, UserEqualsClassesError

class Matrix:
    """Класс Матрица. Позволяет создавать экземпляры как в ручном режиме, 
    так и режиме рандомного заполнения"""

    def __init__(self, matrix=None):
        """Метод создания экземпляра класса Матрица.
        :param: matrix - список списков. 
        Если не передать вызовет метод create_matrix()
        """
        if matrix != None:
            if len(matrix) <= 1:
                raise UserMatrixSizeError(f'количество столбцов {len(matrix)}')
            if len(matrix[0]) <= 1:
                raise UserMatrixSizeError(f'количество строк {len(matrix[0])}')
            self.matrix = matrix
        else:
            self.matrix = self.create_matrix()
        self._rows = len(self.matrix)
        self._cols = len(self.matrix[0])

    def check_size(self, other):
        """Метод сравнения размеров двух матриц"""
        if not isinstance(other, Matrix): 
            raise UserEqualsClassesError(f'{type(other) =}')
        if self._rows != other._rows and self._cols == other._cols:
           raise UserNotEqualsMatrix(self._rows, other._rows)
        if self._cols == other._cols:
           raise UserNotEqualsMatrix(self._cols, other._cols)
        return True

    def __eq__(self, other):
        """Метод сравнения двух матриц"""
        if self is other:
            return True
        try:
            self.check_size(other)
        except UserMatrixSizeError as e:
            print(e)
        else:
            for i in range(self._rows):
                for j in range(self._cols):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        return False
        return True

    def __add__(self, other):
        """Метод сложения двух матриц"""
        try:
            self.check_size(other)
        except UserMatrixSizeError as e:
            print(e)
        else:
            res = []
            for i in range(self._rows):   
                row = [self.matrix[i][j] + other.matrix[i][j] for j in range(self._cols)]
                res.append(row)
            return Matrix(res)
    
    def __sub__(self, other):
        """Метод вычитания двух матриц"""
        try:
            self.check_size(other)
        except UserMatrixSizeError as e:
            print(e)
        else:
            res = []
            for i in range(self._rows):   
                row = [self.matrix[i][j] - other.matrix[i][j] for j in range(self._cols)]
                res.append(row)
            return Matrix(res)

    def __mul__(self, other):
        """Метод умножения двух матриц"""
        try:
            self.check_size(other)
        except UserMatrixSizeError as e:
            print(e)
        else:
            res = [[sum(one * two for one, two in zip(one_row, two_col)) 
                    for two_col in zip(*other.matrix)]
                    for one_row in self.matrix]
            res = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
            for i in range(self._rows):
                for j in range(self._cols):
                    for k in range(other._rows):
                        res[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(res)

    def create_matrix(self):
        """Метод наполнения матрицы элементами с помощью рандома,
        размером не более 5х5"""
        res = []
        rows = randint(2, 5)
        cols = randint(2, 5)
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


matr1 = Matrix([[1], [-1, -2, -3 , -4], [1, 1, 1, 1]])
# UserMatrixSizeError: Матрица должна содержать более 1 строк и более 1 столбца!
# Ошибка здесь: количество строк 1

matr2 = Matrix([[1, 1, 1, 1, 1]])
# UserMatrixSizeError: Матрица должна содержать более 1 строк и более 1 столбца!
# Ошибка здесь: количество столбцов 1

matr3 = Matrix([[2,2],[3,3]])
matr4 = Matrix([[1,1], [2,2],[3,3]])
print(matr3 - matr4) 
# UserNotEqualsMatrix: Матрицы должны быть равных размеров! Размер одной 2, а другой 3

matr5 = 5
print(matr3 - matr5) 
# UserEqualsClassesError: Объекты должны быть экземплярами одного класса!