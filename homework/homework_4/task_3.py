# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# v1
lst = list(map(int, input("Введите числа через пробел:\n").split()))
lst_count_digit = []
for i in lst:
    count = 0
    for k in lst:
        if k == i:
            count += 1
    lst_count_digit.append(count)
result = []
for i in range(len(lst_count_digit)):
    if lst_count_digit[i] == 1:
        result.append(lst[i])
print(result)

# v2
from random import randint
# собираем рандомный список
a = randint(5, 10)
b = []
for i in range(a):
    b.append(randint(1,9))
print(b)
c = []
for i in b:
    if b.count(i) == 1:
        c.append(i)
print(c)

# решение ошибочное. Сет собирает множество:
a= [1,2,2,2,2,3,1,4]
print(set(a))
# ответ {1, 2, 3, 4}

# v3
num_list = input("введиите список натуральных чисел через пробел: ")
num_list1 = num_list.split(" ")
unique = []

for check_num in num_list1:

    if num_list.count(check_num) == 1:
        unique.append(check_num)

print(unique)

# v4
numbers = input('Задайте последовательность чисел:\n').split()
li = []
for i in numbers :
    if not i in li : li.append(i)

print (f"Список не повторяющихся элементов - {li}")

# v5
digits = [1, 2, 4, 5, 3, 2, 1, 1, 2, 4, 5, 7, 8]
dct = {}
for k in set(digits): #сбор множества ключей в словарь
    dct.setdefault(k, digits.count(k))
print(f'Неповторяющиеся элементы:', end=' ')
for k, v in dct.items():
    if int(v) == 1:
        print(k, end=' ')