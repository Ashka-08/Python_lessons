# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# Отправлено на проверку
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

# Еще одно решение
s=[2, 3, 4, 5, 6]
t=[x*y for x, y in zip(s[-1:int(len(s)/2)-2:-1], s[0:int(len(s)/2+1):1])]
print(t)

# решение от преподавателя
list = [3, 4, 5, 6]
result_list = []
for i in range((len(list)+1)//2):
    result_list.append(list[i]*list[len(list)-1-i])
print()
print(result_list)
print()

# решение от преподавателя 2
import random
b = int(input('Введите кол-во чисел в списке for 2# = '))
list_b = list(random.randint(0, 10) for i in range(b))
print(list_b)
proiz_b = list(list_b[i]*list_b[-1*(1+i)] for i in range(b//2+1*(b%2)))
print(proiz_b)