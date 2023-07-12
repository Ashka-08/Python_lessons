# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# 12 = 2*2*3
# 225 = 3*3*5*5

# v1
num = int(input("Введите число: "))
i = 2
lst = []
temp = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Список простых множителей числа {temp}: {lst}")

# v2
n = int(input("Введите число N: "))
i = 2
list = []
while i <= n:
    if n % i == 0:
        list.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"Простые множители введенного числа указаны в списке: {list}")

# v2
a = int(input("Введите число: "))
b = []
c = 2
while c*c <= a:
    if a % c == 0:
        b.append(c)
        a //= c
    else:
        c += 1
if a > 1:
    b.append(a)
print(b)