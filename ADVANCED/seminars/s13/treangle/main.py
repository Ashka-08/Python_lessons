from triangle import *

print(Triangle(1, 2, 3))
print(Triangle('1', 1, 2))
print(Triangle(1, '1', '1.00'))

# print(Triangle('-1', 2, 3)) #TriangleNegativeValueError
# print(Triangle([1,1], 2, 3)) #TriangleValueError
# print(Triangle(1, 1, 10)) #TriangleExistsError: