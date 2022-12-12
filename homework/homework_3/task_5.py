# Задайте число. Составьте список чисел Фибоначчи, в том числе для 
# отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# отправлено на проверку
k = int(input('Введите число: '))
nf = [1, -1]
f = [1, 1]
for i in range(2, k):
    list = f[i-1] + f[i-2]
    f.append(list)
    list2 = nf[i-2] - nf[i-1]
    nf.append(list2)
nf.reverse()
f.insert(0, 0)
print(nf+f)

# еще одно решение
number = int(input("введите длину ряда для чисел Фибоначи: "))
if number==0:
    fib_num = [0]
elif number==1:
    fib_num = [1, 0, 1]
else:
    fib_num = [1, 0, 1]
for i in range(2, number+1):
    temp1 = fib_num[i]+fib_num[i-1]
    fib_num.append(temp1)
for i in range(2, number+1):
    temp2 = fib_num[1] - fib_num[0]
fib_num.insert(0,temp2)
print (fib_num)

# еще одно решение
print('Чтобы cоставить список чисел Фибоначчи, в том числе для отрицательных индексов введите число! ')
k = int(input('Введите число: '))

def fibonacciPos(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

dataPos = list(fibonacciPos(k))
print(f'Для введенного вами числа {k} список чисел Фибоначи: {dataPos}')

def fibonacciNeg(n):
    a, b = 1, -1
    for i in range(n):
        yield a
        a, b = b, a - b

dataNeg = list(fibonacciNeg(k))
print(f'Для введенного вами числа {k} список чисел Негфибоначи: {dataNeg}')

dataRes = dataNeg + [0] + dataPos
print(f'Для введенного вами числа {k} список чисел Фибоначчи, в том числе для отрицательных индексов: {dataRes}')


# от преподавателя
def lst_fibonacci_num():
    num = int(input('Введите любое натуральное число: '))
    fib = []
    a, b = 1, 1
    for i in range(num):
        fib.append(a)
        a, b = b, a + b
        a, b = 0, 1
    for j in range(num + 1):
        fib.insert(0, a)
        a, b = b, a - b
    print(f'Список чисел Фибоначчи для {num}: {fib}')

lst_fibonacci_num()