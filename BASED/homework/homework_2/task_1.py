# Напишите программу, которая принимает на вход вещественное число и показывает 
# сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = input('Введите число: ')
s = 0
for i in n:
    if i.isdigit():
        s += int(i)
print(f"Сумма цифр числа {n} равна:", s)

# 2 способ
# n = input('Введите число: ')
# s = 0
# for i in n:
#     if i != '.':
#         s += int(i)
# print(f"Сумма цифр числа {n} равна:", s)

# 3 способ
# x = int(input().replace('.', ''))
# count = 0
# while x > 0:
#     count += x % 10
#     x = x//10
# print(count)

# 4 способ
# num = input("Введите вещественное число: ")
# sum = 0
# for i in num:
#     if i!=".":
#       sum = sum + int(i)
# print(f"Сумма цифр числа {num} : ", sum)

# 5 способ
# number = input("Введите число: ") number = number.replace("," , '') number = number.replace("." , '') sum = 0 for i in number : sum += int(i) print (sum)

# 6 способ
# print('Введите число')
# x=input()
# z=0
# l='0123456789'
# for i in range(len(x)):
#     if (x[i] in l):
#         z=z+int(x[i])
# print(z)

# 7 способ
# n = input('Введите вещественное число: ')
# res = 0
# for i in n:
#     try:
#         res = res + int(i)
#     finally:
#         continue
# print(f' - {n} -> {res}')

# 8 способ от преподавателя
# n = float(input('Введите число - '))
# while n % 1 > 0:
#     n *= 10
# summ = 0
# while n > 0:
#     summ += n % 10
#     n //= 10
# print(int(summ))

# a = float(input())
# a = str(a)
# summ = 0
# while len(a) != 0:
#     if a[-1].isdigit():
#         summ += int(a[-1])
#         a = a[:-1]
# print(summ)