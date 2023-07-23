# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def cut_sum(lst, start, stop):
    # return sum(lst[start+1:stop])
    return sum(lst[min(start, stop)+1:max(start, stop)])

lst = [i for i in range(100)]

print(cut_sum(lst, 3, 5)) # 4
print(cut_sum(lst, 98, 105)) # 99
print(cut_sum(lst, 95, 105)) # 390