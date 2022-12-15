# Task 
# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них

# было решение
# lst = []
# for i in range(5):
#     x = int(input(f'Введите число {i+1}: '))
#     lst.append(x)
# max = 0
# for i in lst:
#     if max < i: max = i
# print(f'Максимальное число номер {i} = {max}')

# enumerate 
ls = list(map(int, input("Введите числа через пробел:\n").split()))
ls_num = list(enumerate(ls, start=1))
max = max(ls_num, key=lambda i : i[1])
print(f'Максимальное число номер {max[0]} = {max[1]}')