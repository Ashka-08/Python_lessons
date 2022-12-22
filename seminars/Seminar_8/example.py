# Задайте список чисел от 1 до 9 включительно. Напишите программу, которая4
# найдет сумму нечетных элементов списка
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(sum([i for i in range(1, 10) 
        if i % 2 != 0]))
# 25

# Вывести четное число списка и его квадрат
lst = [1, 2, 3, 5, 8, 15, 23, 38]
res = list((i, i*i) for i in lst 
        if i % 2 == 0)
print(res)
# [(2, 4), (8, 64), (38, 1444)]