# Реализуйте алгоритм перемешивания списка.

s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Первоначальный список: {s}')
import random
for i in range(len(s)-1, 0, -1):
    j = random.randint(0, i + 1) 
    s[i], s[j] = s[j], s[i]
print(f'Перемешанный список: {s}')