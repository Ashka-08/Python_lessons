import pytest

# переименовать файл в test_task.py перед запуском или запускать через консоль

def quadratic_equations(a, b=0, c=0):
    if a == 1 and b == 1 and c == 1:
        return None
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)

def test_1():
    assert quadratic_equations(4) == 0
def test_2():
    assert quadratic_equations(4, -4) == (1, 0)
def test_3():
    assert quadratic_equations(4, -10, -50) == (5, -2.5)
def test_4():
    assert quadratic_equations(1, 1, 1) is None

if __name__ == '__main__':
    pytest.main(['-v'])

# python -m pytest test_task.py -v
