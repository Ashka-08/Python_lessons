#  Для натурального n создать словарь индекс-значение, состоящий из элементов 
# последовательности 3n + 1.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input('Введите число: '))
# cl = []
# for i in range(n):
#     cl.append(3 * (i+1) + 1)
# print(cl)
# for i in range(len(cl)):
#     print(f'{i+1}: {cl[i]}', end=', ')

# n = int(input('Введите число: '))
# cl = []
# for i in range(n):
#     cl.append(3 * (i+1) + 1)
#     print(f'{i+1}: {cl[i]}', end=', ')

n = int(input('Введите число: '))
d = {i: 3 * i + 1 for i in range(1, n+1)}
print(d)