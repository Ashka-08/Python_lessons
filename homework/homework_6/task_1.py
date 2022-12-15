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

# list comprehension
n = input('Введите число: ')
data = [int(x) for x in str(n) if x !='.']
sum = 0
for i in data:
    sum += i
print(f"Сумма цифр числа {num} равна:", sum)