from matrix import Matrix
import doctest

def test_matr():
    """
    Метод тестрирвония класса Матрица с помощью модуля доктест.
    >>> print(Matrix([[2,2],[3,3]]).rows)
    2
    >>> print(Matrix([[2,2],[3,3]]).cols)
    2
    >>> print(repr(Matrix([[2,2],[3,3]])))
    Matrix([[2, 2], [3, 3]])
    >>> print(repr(Matrix([[2,2],[3,3]]) - Matrix([[1,1],[2,2]])))
    Matrix([[1, 1], [1, 1]])
    >>> print(repr(Matrix([[2,2],[3,3]]) + Matrix([[1,1],[2,2]])))
    Matrix([[3, 3], [5, 5]])
    """
    pass

if __name__ == '__main__':
    doctest.testmod(verbose=True)