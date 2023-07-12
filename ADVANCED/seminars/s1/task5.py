# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n. 

print('Посчитаем сумму чётных элементов от 1 до n, исключая кратные e')
n = int(input('Введите n: '))
e = int(input('Введите e: '))
if e == 0:
    print('на ноль делить нельзя')
    exit()
i = 0
sum = 0
EVEN = 2
while i <= n:
    if i % EVEN == 0 and i % e != 0:
        sum += i
    i += EVEN
print(f'sum = {sum}')