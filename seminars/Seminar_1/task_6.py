# Напишите программу, которая будет принимать на вход дробь и 
# показывать первую цифру дробной части числа.
# Примеры:
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# n = float(input('Введите число: '))
# if n % 1 != 0:
#     print (int(n % 1 * 10))
# else:
#     print('нет')

n = float(input('Введите число: '))
n = abs(n)
n = n - n // 1
if n == 0:
    print('нет')
else:
    n = n * 10
    n = n // 1
    print(int(n))
