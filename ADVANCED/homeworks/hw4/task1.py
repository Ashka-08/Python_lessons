# Напишите функцию для транспонирования матрицы

# Транспонированная матрица — матрица, полученная из исходной матрицы 
# заменой строк на столбцы. Формально, транспонированная матрица для матрицы 
# размеров m*n — матрица размеров n*m, определённая как [i, j] = [j, i].

from random import randint

ROWS = 3
COLUMNS = 4


def create_matrix(count_rows, count_columns):
    matrix = []
    for _ in range(count_rows):
        row = []
        for _ in range(count_columns):
            row.append(randint(0, 9))
        matrix.append(row)
    return matrix


def transposition_matrix(matrix):
    temp = create_matrix(len(matrix[0]), len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            temp[len(matrix[0])-j-1][i] = matrix[i][j]
    return temp[::-1]


print(matrix := create_matrix(ROWS, COLUMNS))
print(transposition_matrix(matrix))
