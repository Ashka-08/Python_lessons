# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("Введите числа через пробел:\n").split()))
lst_count_digit = []
for i in lst:
    count = 0
    for k in lst:
        if k == i:
            count += 1
    lst_count_digit.append(count)
result = []
for i in range(len(lst_count_digit)):
    if lst_count_digit[i] == 1:
        result.append(lst[i])
print(result)