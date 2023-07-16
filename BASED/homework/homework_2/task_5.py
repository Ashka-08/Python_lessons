# Реализуйте алгоритм перемешивания списка.

# s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(f'Первоначальный список: {s}')
# import random
# for i in range(len(s)-1, 0, -1):
#     j = random.randint(0, i + 1) 
#     s[i], s[j] = s[j], s[i]
# print(f'Перемешанный список: {s}')

# import random
# some_list = [1, 5, 'erag', 54, 6]
# random.shuffle(some_list)
# print(some_list)

import random
list = ["Anna", "Alex", 3.14159, 0]
for i in range(len(list)):
    index_a = random.randint(0, len(list) - 1)
    list[i], list[index_a] = list[index_a], list[i]
print(list)