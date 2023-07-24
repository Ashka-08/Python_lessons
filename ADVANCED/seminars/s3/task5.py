# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# Нумерация начинается с единицы.
# маржовый оператор присвоит значение и сразу распечатает

print(lst := [1, 2, 2, 3, 5, 4, 5, 6])  #маржовый оператор
print(*[i+1 for i in range(len(lst)) if lst[i] % 2])

res = []
for i in range(len(lst)):
    if lst[i] % 2: # можно не писать ни !=0, ни == 1, все равно будет True
        res.append(i+1)
print(*res)
