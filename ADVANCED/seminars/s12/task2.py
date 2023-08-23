# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.


import json

class Factorial:

    def __init__(self):
        self._arg_archive = []
        self._number_archive = []
        self._factorial = 1

    def __call__(self, num):
        self._arg_archive.append(num)
        self.num = num
        factorial = 1
        for i in range(num):
            factorial *= (i + 1)
        self._number_archive.append(factorial)
        return factorial

    def __str__(self):
        return f'{self._arg_archive}, {self._number_archive}'

    def number_archive(self):
        return self._arg_archive, self._number_archive

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.res = dict(zip(self._arg_archive, self._number_archive))
        self.json_file = open(r'ADVANCED\seminars\s12\task2_res.json', 'w')
        json.dump(self.res, self.json_file, indent=2)
        self.json_file.close()


fac = Factorial()
fac1 = Factorial()

print(fac(3))
print(fac1(4))
print(fac1(5))
print(fac.number_archive())
print(fac1.number_archive())

jw = Factorial()
with jw as cm:
    cm(5)

with jw as cm2:
    cm2(6)