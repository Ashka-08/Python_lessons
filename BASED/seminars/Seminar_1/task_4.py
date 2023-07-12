# Напишите программу, которая на вход принимает 5 чисел и 
# показывает четные и нечетные

lst = []
for i in range(5):
    x = int(input(f'Введите число {i}: '))
    lst.append(x)
    if i % 2 == 0:
        print(f'{i} - четное')
    else:
        print(f'{i} - нечетное')
print(lst)