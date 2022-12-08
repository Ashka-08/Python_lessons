# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите 
# на экран их сумму.
# Пример:
# Для n = 4: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06

# n = int(input('Введите число: '))
# cl = []
# sum = 0
# for i in range(n):
#     cl.append((1 + (1 / (i+1))) ** (i+1))
#     print(f'{i+1}: {round(cl[i], 2)}', end=', ')
#     sum += cl[i]
# print(f' Сумма {round(sum, 2)}')

n = int(input())
summ = 0
for i in range(1, n + 1):
    summ += (1 + 1 / i) ** i
print(summ)