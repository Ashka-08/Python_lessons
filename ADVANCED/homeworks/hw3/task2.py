# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

lst = [0, 1, 2, 1, 2, 4, 3]
double_lst = []
i = 0
while i < len(lst):
    if lst.count(lst[i]) > 1:
        temp = lst[i]
        for j in range(lst.count(temp)):
            lst.remove(temp)
        double_lst.append(temp)
    else:
        i += 1

print(f'Cписок дубликатов {double_lst}')
print(f'Cписок без дубликатов {lst}')