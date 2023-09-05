class TriangleException(Exception):
    def __init__(self, name: str, message: str) -> None:
        self.name = name
        self.message = message
    
    def __str__(self) -> str:
        return f'Triangle ERROR!\n{self.name}\n{self.message}'


class TriangleExistsError(TriangleException):
    def __init__(self, side: float | int, other_sides: list[int | float]) -> None:
        super().__init__('Ошибка создания',
                        f'Треугольник не может быть создан, т.к. сторона {side}'\
                        f'больше суммы двух других сторон {other_sides}')


class TriangleNegativeValueError(TriangleException):
    def __init__(self, side) -> None:
        super().__init__('Ошибка данных', 
                        f'Сторона треугольника не может иметь отрицательную длину {side}')


class TriangleValueError(TriangleException):
    def __init__(self, side) -> None:
        super().__init__('Ошибка данных', 
                        f'Сторона треугольника должна быть числом {side}')
