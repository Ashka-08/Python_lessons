# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

# рандомим коэффициенты
def create_koeff(k):
    lst = [random.randint(0,101) for i in range(k+1)]
    return lst

# создаем многочлен в виде строки 
def create_str(sp):
    lst= sp[::-1]
    temp = ''
    if len(lst) < 1:
        temp = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                temp += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    temp += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                temp += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    temp += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                temp += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                temp += ' = 0'
    return temp

k = int(input("Введите натуральную степень k = "))
result = create_str(create_koeff(k))
print(result)
with open('task_4.txt', 'w') as data:
    data.write(result)
