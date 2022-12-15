# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# отправленно на проверку
# import random

# # рандомим коэффициенты
# def create_koeff(k):
#     lst = [random.randint(0,101) for i in range(k+1)]
#     return lst

# создаем многочлен в виде строки 
# def create_str(sp):
#     lst= sp[::-1]
#     temp = ''
#     if len(lst) < 1:
#         temp = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 temp += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0 or lst[i+2] != 0:
#                     temp += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 temp += f'{lst[i]}x'
#                 if lst[i+1] != 0 or lst[i+2] != 0:
#                     temp += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 temp += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 temp += ' = 0'
#     return temp

# k = int(input("Введите натуральную степень k = "))
# result = create_str(create_koeff(k))
# print(result)
# with open('task_4.txt', 'w') as data:
#     data.write(result)


# v2 не работает, ошибка объекта лист при добавлении в список f(x)
# from random import randint

# kk = randint(2, 6)
# print(f'Пусть коэффициент k = {kk}')

# a = list()
# for i in range(kk+1):
#     a.append(randint(0,100))
# print(f'Список коэффициентов многочлена:\n{a}')

# b = list()
# for j in range(0, kk+1):
#     b.insert(0, j)
# print(f'Список степеней k:\n{b}')

# c = list()
# for l in range(kk-1):
#     c.append(f'{a(l)}*x**{b(l)}')
# c.append(f'{a[-2]}*x')
# c.append(a[-1])
# print(f'Список множителей многочлена:\n{c}')

# d = []
# for h in range(kk):
#     d += (f'{c(h)} + ')
# d += (f'{c[-1]} = 0')
# print(d)

# for m in range (kk):
#     print(f'{a(m)} * x ** {b(m)} +')

# v3 работает
# number = int(input('введите степень: '))
# coefficients = [randint(0, 100) for _ in range(number + 1)]
# powers = [f'*x^{i}'if i > 1 else '*x' for i in range(number, 0, -1)]
# terms = [str(a) + str(b) for a, b in zip(coefficients, powers + [''])]
# print(' + '.join(terms) + ' = 0')
# with open('homework\\hw_4\\4_polynomial_w.txt', 'w') as data:
# data.write(' + '.join(terms) + ' = 0')

# v4 
# poly = [f'{kff[i]}x^{k - i}' for i in range(len(kff))]

# v5
# degree_k = int(input("Введите натуральную степень k: "))
# list_coef = [randint(0, 100) for i in range(101)]

# result = str(list_coef[randint(0, 100)]) + 'x^' + str(degree_k)

# degree_k = degree_k - 1

# while degree_k >= 0 :
# coef = randint(0, 1)
# if coef == 1 :
# if degree_k == 0 :
# result += ' + ' + str(list_coef[randint(0, 100)])
# else :
# result += ' + ' + str(list_coef[randint(0, 100)]) + 'x^' + str(degree_k)
# degree_k -= 1

# result = result + ' = 0'

# with open('home_work/dz_4/polynomials_degree_k.txt', 'w') as poly_degree_k :
# poly_degree_k.write(result)

# версия от преподавателя

from random import randint
k = int(input('Insert equation power: '))
koefs = list()
for i in range(1, k + 2):
    koefs.append(randint(1, 100))
    ans = list()
for i in range(len(koefs)):
    if k == 1:
        ans.append(f'{koefs[i]}*x')
    elif k == 0:
        ans.append(f'{koefs[i]}')
    else:
        ans.append(f'{koefs[i]}*x**{k}')
    flag = randint(0, 1)
    ans.append(str(-1**flag))
    k -= 1
    # if flag == 1:
    #     ans.append('+')
    # elif flag == 0:
    #     ans.append('-')
    # k -= 1

ans.pop(-1) # удаление последнего символа в списке
ans.append('=0')

print(''.join(ans))
fout = open('output.txt', 'w') # W - создает или изменяет строчку
fout.write(''.join(ans))
fout.close()