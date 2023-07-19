# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

from pprint import pprint

my_tuple = \
    (
    1, [None], (1, 3), {1, 2}, 42, (1+2j), [], dict(one='one', two='2'),
    'two', 3.0, 'four', 115, True, 12.5, False, (1, 2), (2+3j)
    )
res = {}

for i in my_tuple:
    if type(i).__name__ not in res:
        res[type(i).__name__] = []
    res[type(i).__name__].append(i)

for k,v in res.items():
    print(f'{k:>10} : {v}')

"""
       int : [1, 42, 115]
      list : [[None], []]
     tuple : [(1, 3), (1, 2)]
       set : [{1, 2}]
   complex : [(1+2j), (2+3j)]
      dict : [{'one': 'one', 'two': '2'}]
       str : ['two', 'four']
     float : [3.0, 12.5]
      bool : [True, False]"""

pprint(res)

"""
{'bool': [True, False],
 'complex': [(1+2j), (2+3j)],
 'dict': [{'one': 'one', 'two': '2'}],
 'float': [3.0, 12.5],
 'int': [1, 42, 115],
 'list': [[None], []],
 'set': [{1, 2}],
 'str': ['two', 'four'],
 'tuple': [(1, 3), (1, 2)]}"""