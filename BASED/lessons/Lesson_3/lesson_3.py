# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

# Первое решение

path = 'C:/Users/Professional/Desktop/geekbrains/Python/lessons/Lesson_3/lesson_3.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []
while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]
out = []
for e in numbers:
    if not e % 2:
        out.append((e, e **2))
print(out)

# Решение через лямбду
def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()
res = select(int, data)
res = where(lambda e: not e % 2, res)
res = select(lambda e: (e, e**2), res)
print(res)

# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.
# f(x) ⇒ x + 10
# map(f, [ 1, 2, 3, 4, 5])
#          ↓  ↓  ↓  ↓  ↓
#      [ 11, 12, 13, 14, 15]
# Нельзя пройтись дважды

# Пример лямбды с map

data = list(map(int, input().split()))
print(data)

data = list(map(int, '1 2 3'.split()))

for e in data:
    print(e) 

# добавим map в пример
def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()
data = map(int, data)
data = where(lambda e: not e % 2, data)
data = list(map(lambda e: (e, e**2), data))

# filter
# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.
# f(x) ⇒ x - чётное
# filter(f, [ 1, 2, 3, 4, 5])
#                ↓
#             [ 2, 4 ]
# Нельзя пройтись дважды

data = [x for x in range(10)]
# res = list(filter(lambda x: x%2==0, data))
res = list(filter(lambda x: not x % 2, data))
print(res)

# добавим map в пример
data = '1 2 3 5 8 15 23 38'.split()
data = map(int, data)
data = filter(lambda e: not e % 2, data)
data = list(map(lambda e: (e, e**2), data))

# Функция zip
# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора
# zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
#  ↓
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# Нельзя пройтись дважды

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]

data = list(zip(users, ids))
print(data)

# в выводе будет
# [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(zip(users, ids, salary))
print(data)

# в выводе будет
# [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]

# Функция enumerate
# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
#  ↓
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# Нельзя пройтись дважды

users = ['user1', 'user2', 'user3', 'user4', 'user5']

data = list(enumerate(users))
print(data)
# в выводе будет
# [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]