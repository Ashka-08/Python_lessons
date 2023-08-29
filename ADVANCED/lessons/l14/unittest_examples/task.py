import unittest
from collections import OrderedDict

def func(data: dict, first=True):
    if first:
        sort_data = OrderedDict(sorted(data.items()))
        list_values = list(sort_data.values())
        return list_values[0]
    else:
        list_values = list(data.values())
        return list_values[1]
    

data = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
print(func(data))
print(func(data, first=False))

class TestSample(unittest.TestCase):
    def setUp(self) -> None:
        self.data = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
    def test_step_1(self):
        self.assertEqual(func(self.data), 4)
    def test_step_2(self):
        self.assertEqual(func(self.data, first=False), 2)


if __name__ == '__main__':
    unittest.main()