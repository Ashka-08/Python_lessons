from random import randint


class Matrix:
    """Класс Матрица позволяет создавать экземпляры как в ручном режиме, 
    так и режиме рандомного заполнения"""

    def __init__(self, matrix=None):
        """Метод создания экземпляра класса Матрица.
        :param: matrix - список списков. 
        Если не передать вызовет метод create_matrix()
        """
        if matrix is not None:
            list_size_col = []
            for el in matrix:
                list_size_col.append(len(el))
            min_size_col = min(list_size_col)
            if min_size_col <= 1 or len(matrix) <= 1:
                raise MatrixMinSizeError
            if any(x != list_size_col[0] for x in list_size_col):
                raise MatrixSizeError
            self.matrix = matrix
        else:
            self.matrix = self.create_matrix()
        self._rows = len(self.matrix)
        self._cols = len(self.matrix[0])

    @property
    def rows(self):
        """Количество строк"""
        return self._rows
    
    @property
    def cols(self):
        """Количество столбцов"""
        return self._cols

    def check_size_matrixes(self, other):
        """Метод сравнения размеров двух матриц"""
        if not isinstance(other, Matrix): 
            raise ClassesEqualsError(self, other)
        if self._rows != other._rows or self._cols != other._cols:
           raise MatrixNotEquals(self, other)
        return True

    def __eq__(self, other):
        """Метод сравнения двух матриц"""
        if self is other:
            return True
        try:
            self.check_size_matrixes(other)
        except MatrixMinSizeError as e:
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
            self.check_size_matrixes(other)
        except MatrixMinSizeError as e:
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
            self.check_size_matrixes(other)
        except MatrixMinSizeError as e:
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
            self.check_size_matrixes(other)
        except MatrixMinSizeError as e:
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


class UserException(Exception):
    """Базовый класс ошибок"""

    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return f'{self.message}'


class MatrixMinSizeError(UserException):
    """Ошибка минимального размера матрицы"""
    
    def __init__(self):
        super(MatrixMinSizeError, self).__init__(f'Ошибка! '
            f'Количество строк/столбцов не божет быть меньше 2')

class MatrixSizeError(UserException):
    """Ошибка размеров матрицы"""
    
    def __init__(self):
        super(MatrixSizeError, self).__init__(f'Ошибка! '
            f'Количество элементов в каждой строке должно быть одинаковым, аналогично и строки')

class MatrixNotEquals(UserException):
    """Ошибка неравенства размеров двух матриц"""

    def __init__(self, matr1: Matrix, matr2: Matrix):
        super(MatrixNotEquals, self).__init__(f'Матрицы должны быть равных размеров! '
            f'Размер одной матрицы {matr1._rows}x{matr1._cols}, '
            f'а размер другой матрицы {matr2._rows}x{matr2._cols}')


class ClassesEqualsError(UserException):
    """Ошибки неравенства двух классов"""

    def __init__(self, matrix: Matrix, other):
        super(ClassesEqualsError, self).__init__(f'Ошибка типов! '
            f'Объекты должны быть экземплярами одного класса! '
            f'Ошибка здесь: {type(matrix) = }, {type(other) = }')


if __name__ == '__main__':

    # print(m0 := Matrix([[1, 2], [1, 2, 3, -4]]))
    # MatrixSizeError: Ошибка! Количество элементов в каждой строке должно быть одинаковым, аналогично и строки


    # m1 = Matrix([[1, 1], [1]])
    # m2 = Matrix([[1, 1, 1, 1, 1]])
    # MatrixSizeError: Ошибка! Количество строк/столбцов не божет быть меньше 2


    print(m3 := Matrix([[2,2],[3,3]]))
    print(Matrix([[2,2],[3,3]]).rows)
    print(m4 := Matrix([[1,1,1],[2,2,2]]))
    # print(m3 - m4) 
    # MatrixNotEquals: Матрицы должны быть равных размеров! Размер одной матрицы 2x2, а размер другой матрицы 3x2
    
    
    m6 = 6
    # print(m3 - m6) 
    # ClassesEqualsError: Ошибка типов! Объекты должны быть экземплярами одного класса! Ошибка здесь: type(matrix) = <class '__main__.Matrix'>, type(other) = <class 'int'>!