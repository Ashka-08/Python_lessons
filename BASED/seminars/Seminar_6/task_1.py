# 1.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить 
# в нем только двузначные числа. Реализовать программу с использованием функции 
# filter. Результат отобразить на экране в виде последовательности оставшихся чисел 
# в одну строчку через пробел.
# пример - 8 11 0 -23 140 1 => 11 -23

# filter
# Функция filter() применяет указанную функцию к каждому элементу итерируемого 
# объекта и возвращает итератор с теми объектами, для которых функция вернула True.
# f(x) ⇒ x - чётное
# filter(f, [ 1, 2, 3, 4, 5])
#                ↓
#             [ 2, 4 ]
# Нельзя пройтись дважды

# data = [x for x in range(10)]
# # res = list(filter(lambda x: x%2==0, data))
# res = list(filter(lambda x: not x % 2, data))
# print(res)


lst = list(map(int, input("Введите числа через пробел:\n").split()))
# res = list(filter(lambda x: x // 10 >= 1, lst)) не выводит отриц.числа
# res = list(filter(lambda x: x // 10 >= 1 or x // 10 <= -1, lst))
# res = list(filter(lambda x: (-100 < x < -9) or (9 < x < 100), lst))
res = list(filter(lambda x: abs(x) // 10 >= 1, lst))
print(res)

lst = input("Введите числа через пробел:\n").split()
res = list(filter(lambda x: len(str(abs(int(x)))) == 2, lst))
print(res)