# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.


words = input('enter text: ').split()
"""
если у сплита поставить аргументом пробельный символ " ", 
то он каждый доп пробел обернет в элемент списка.
А если не указать ничего, то он возьмет в элементы списка все слова через
любые пробельные символы, таб(\t), перенос строки(\n) и сами пробелы, 
т.е. непечатаемые символы"""

max_len = len(max(words, key = len))

# v1
for i in range(len(sorted(words))):
    print(f'{i+1}.{words[i].rjust(max_len+1)}')

# v2
for i in range(len(words)):
    print(f'{i+1}.{sorted(words)[i]: >{max_len+1}}')

# v3
lst = list(input('Введите строку текста: ').split())
lst.sort()
l: int = 0
for i in lst:
    if len(i) > l:
        l = len(i)
for i in range(len(lst)):
    print(f'{(i+1)}. {lst[i]:>{l}}')

# Для копирования
# qqq www eeeeeeeee rr ttt aa bbbbbb lllllll iiii

""" Вывод:
1.        aa
2.    bbbbbb
3. eeeeeeeee
4.      iiii
5.   lllllll
6.       qqq
7.        rr
8.       ttt
9.       www"""

# v4
string = input('Введите строку текста: ').split()
string.sort()
maxx = max([len(i) for i in string])

for n, s in enumerate(string, 1):
    print(f'{n}. {" " * (maxx-len(s)+1)}{s}')

# v5
for n, s in enumerate(string, 1):
    print(f'{n}. {s:>{maxx}}')