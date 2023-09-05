from custom_exeptions import TriangleExistsError, \
                            TriangleNegativeValueError, \
                            TriangleValueError


class Side:

    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.parameter_name, float(value))

    def validate(self, side):
        if isinstance(side, int | float) and side > 0 or \
            isinstance(side, str) and side.replace('.', '', 1).isdigit():
            return side
        if isinstance(side, int | float) and side >= 0:
            raise TriangleNegativeValueError(side)
        if isinstance(side, str) and side.startswith('-') and \
            side.replace('-','', 1).replace('.', '', 1).isdigit():
            raise TriangleNegativeValueError(side)
        raise TriangleValueError(side)


class Triangle:
    side_a = Side()
    side_b = Side()
    side_c = Side()

    def __init__(self, a, b, c) -> None:
        self.side_a = a
        self.side_b = b
        self.side_c = c
        if not Triangle._is_exists(a, b, c):
            print('ERROR')
        self.sides = (self.side_a, self.side_b, self.side_c)

    @property
    def type_triangle(self):
        if len(set(self.sides)) == 1:
            kind = 'Равносторонний'
        elif len(set(self.sides)) == 2:
            kind = 'Равнобедренный'
        else:
            kind = 'Разносторонний'
        return kind

    def __str__(self) -> str:
        return f'{self.type_triangle} треугольник {self.sides}'

    @staticmethod
    def _is_exists(a, b, c):
        sides = list(map(float, [a, b, c]))
        for side in sides:
            other_sides = sides.copy()
            other_sides.remove(side)
            if side > sum(other_sides):
                raise TriangleExistsError(side, other_sides)
        return True
