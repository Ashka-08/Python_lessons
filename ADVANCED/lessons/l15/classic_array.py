from array import array, typecodes

byte_array = array('B', (1, 2, 3, 255))
print(byte_array)
print(typecodes)
"""
array('B', [1, 2, 3, 255])
bBuhHiIlLqQfd
"""

# Массивы поддерживают методы списка list

from array import array

long_array = array('l', [-6000, 800, 100500])
long_array.append(42)
print(long_array)
print(long_array[2])
print(long_array.pop())
"""
array('l', [-6000, 800, 100500, 42])
100500
42
"""

# Не расширяет типы

from array import array

long_array = array('l', [-6000, 800, 100500])

# long_array.append(2**32) 
# OverflowError: Python int too large to convert to C long

# long_array.append(3.14) 
# TypeError: 'float' object cannot be interpreted as an integer

# Задание

from pprint import pprint
from collections import namedtuple

Data = namedtuple('Data', ['mathematics', 'chemistry', 'physics', 'genetics'], 
                    defaults=[5, 5, 5, 5])
d = {
    'Ivanov': Data(4, 5, 3, 5),
    'Petrov': Data(physics=4, genetics=3),
    'Sidorov': Data(),
    }
pprint(d)
"""
{'Ivanov': Data(mathematics=4, chemistry=5, physics=3, genetics=5),
 'Petrov': Data(mathematics=5, chemistry=5, physics=4, genetics=3),
 'Sidorov': Data(mathematics=5, chemistry=5, physics=5, genetics=5)}
"""
