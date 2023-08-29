import pytest
from matrix import Matrix, ClassesEqualsError, MatrixNotEquals, MatrixMinSizeError


@pytest.fixture
def data():
    m1 = Matrix([[2,2],[3,3]])
    m2 = Matrix([[1,1,1],[2,2,2]])
    return [m1, m2]
    
def test_type(data):
    with pytest.raises(ClassesEqualsError):
        data[0] - 1

def test_sizes(data):
    with pytest.raises(MatrixNotEquals):
        data[1] - data[0]

def test_create_Matrix():
    with pytest.raises(MatrixMinSizeError):
        Matrix([[1,1], [1]])

if __name__ == '__main__':
    pytest.main(['-v'])