# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

lst = [6, 1, 2, 2, 3, 4, 6, 7, 4, 1, 4]
COUNT = 2
i = 0
while i < len(lst):
    if lst.count(lst[i]) == COUNT:
        temp = lst[i]
        lst.remove(temp)
        lst.remove(temp)
    else:
        i += 1
print(lst)
    