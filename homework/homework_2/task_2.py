# Напишите программу, которая принимает на вход число N и выдает набор 
# произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите число: '))
# p = []
# f = 1
# for i in range(1, n+1):
#     f *= i
#     p.append(f)
# print(p)

# n = int(input('Введите число: '))
# f = 1
# for i in range(n):
#     i = i + 1
#     f = i * f
#     print(f, end=", ")

number = int(input("введите натуральное число N :"))
count = 1
for i in range(1,number+1):
    count = count*i
    print(count, end=' ')