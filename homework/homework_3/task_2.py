# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

num = list(map(int, input("Введите числа через пробел: ").split()))
num2 = []
count = -1
i = 0
size = len(num) / 2
while i < size:
    num2.append(num[i]*num[count])
    count -= 1
    i += 1
print(num2)