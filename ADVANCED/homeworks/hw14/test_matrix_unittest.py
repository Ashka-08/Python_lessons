from matrix import Matrix, MatrixMinSizeError, MatrixSizeError, MatrixNotEquals
import unittest

class TestMatrix(unittest.TestCase):

    def setUp(self) -> None:
        self.matrix = Matrix([[2,2],[3,3]])
        self.matrix2 = Matrix([[1,2],[2,2],[3,3]])
    
    def test_create_error(self):
        with self.assertRaises(MatrixSizeError):
            Matrix([[2,2],[3,3,3]])

    def test_size_error(self):
        with self.assertRaises(MatrixNotEquals):
            self.matrix - self.matrix2
    
    def test_min_size_error(self):
        with self.assertRaises(MatrixMinSizeError):
            Matrix([[1, 1], [1]])


if __name__ == "__main__":
    unittest.main(verbosity=2)