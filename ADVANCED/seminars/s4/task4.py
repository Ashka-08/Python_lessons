# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

from random import randint

STR_SIZE = 10

def buble_sort(sorted_list):
    for i in range(STR_SIZE):
        for j in range(STR_SIZE - i - 1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]


print(my_list := [randint(0,100) for i in range(STR_SIZE)])
buble_sort(my_list)
print(my_list)