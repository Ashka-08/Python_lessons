# Напишите программу, которая принимает на вход вещественное число и показывает 
# сумму его цифр.
# Пример:
# - 0,56 -> 11

# было решение
num = input('Введите число: ')
s = 0
for i in num:
    if i.isdigit(): s += int(i)
print(f"Сумма цифр числа {num} равна:", s)

# Отправлено на проверку
# list comprehension
n = input('Введите число: ')
data = [int(x) for x in str(n) if x !='.']
sum = 0
for i in data:
    sum += i
print(f"Сумма цифр числа {num} равна:", sum)

# v3 
n = abs(float(input('Введите число: ')))
if n % 1 != 0:
    x = len(str(float(n))[str(float(n)).index('.')+1:])
    while x > 0:
        n = round(n * 10, x)
        x -= 1
n = str(int(n))
print(sum(map(int, n)))

# v4
print(sum(map(int, (filter(str.isdigit, input("Введите число: "))))))
# внутри фильтра функция isdigit ставится без скобок 

# v5
a = float(input('Введите число: '))
print(sum(map(int, str(a).replace('.', '').replace('-', ''))))