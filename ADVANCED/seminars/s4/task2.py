# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def to_ord(string):
    return sorted(set(map(ord, list(string))), reverse=True)


print(to_ord('Карл у Клары украл кораллы'))

# v2
ord_l = lambda x: sorted(set(map(ord, list(x))), reverse=True)
print(ord_l('Карл у Клары украл кораллы'))