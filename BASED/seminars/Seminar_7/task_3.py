# На вход программы поступает список наименований рек, записанных в одну 
# строчку через пробел. Необходимо отсортировать этот список в порядке убывания 
# длин названий. Результат вывести в одну строчку через пробел.

# Sample Input:
# Лена Енисей Волга Дон
# Sample Output:
# Енисей Волга Лена Дон

# sort - сортировка списка от меньшего к большему, reverse=True - в обратном порядке
# key - ключ сортировки, можно через лямбду

# v1

def custom_key(str):
    return len(str)

str = ['Лена', 'Енисей', 'Волга', 'Дон']
str.sort(reverse=True, key=custom_key)
print(str)

# v2

a = 'Лена Енисей Волга Дон'
b = a.split()
res = sorted(b, reverse=True, key=lambda x: len(x))
print(' '.join(res))

# v3 от преподавателя
s=sorted(input().split(), key=lambda x: len(x))[::-1]
print(*s)

# v3

# river = 'Лена Енисей Волга Дон'.split()
# result = ''
# for i in range(len(river) - 1) :
#     if len(river[i]) < len(river[i + 1]) :
#         river[i], river[i + 1] = river[i + 1], river[i]
#         result += river[i] + ' '

# result += river[len(river) - 1]

# print(result)