# Напишите программу, которая подсчитает и выведет сумму квадратов всех 
# двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.

# Обратите внимание: на 9 должно делиться исходное двузначное число, 
# а не его квадрат.

a = [i for i in range(10,100)]
print(sum(list(map(lambda x: x*x, list(filter(lambda i: i % 9 == 0, a))))))

print(sum(map(lambda x: x**2, filter(lambda x: x%9 == 0, range(10,100)))))

print(sum(map(lambda x: x**2, filter(lambda x: not x%9, range(10,100)))))

# print(a)
# b = list(filter(lambda x: x % 9 == 0, a))
# print(b)
# b = list(map(lambda x: x*x, b))
# print(b)
# res = sum(b)
# print(res)