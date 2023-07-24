# Создайте функцию генератор чисел Фибоначчи
# первые два числа равны 0 и 1, а каждое последующее число равно сумме двух предыдущих


def fib_gen(n: int):
    fib = [0, 1]
    while n > 0:
        yield fib[-1]
        fib.append(fib[-1] + fib[-2])
        n -= 1


for num in fib_gen(10):
    print(num)