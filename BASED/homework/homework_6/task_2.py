# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# было решение
list = [2, 3, 4, 5, 6]
result_list = []
for i in range((len(list)+1)//2):
    result_list.append(list[i]*list[len(list)-1-i])
print(result_list)

# list comprehension и zip
s=[2, 3, 4, 5, 6]
t=[x*y for x, y in zip(s[-1:int(len(s)/2)-2:-1], s[0:int(len(s)/2+1):1])]
print(t)

# v3 с 8 семинара
numbers = [2, 3, 4, 5, 6, 7, 5]
diff = [a*b for a, b in zip(numbers, numbers[:(len(numbers)//2) - 1: -1])]
print(diff)