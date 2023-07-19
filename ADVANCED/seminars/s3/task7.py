# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают
# или не совпадают в ваших решениях.

txt = input('Введите строку текста: ')
# v1

d = {}
d2 = {}
for i in txt:
    d.update({i: txt.count(i)})
print(d)
for i in txt:
    if i not in d2:
        d2.setdefault(i, 1)
    else:
        d2.update({i: d2.get(i)+1})
print(d2)

# v2
from collections import Counter
res1 = {}
res2 = {}
res3 = Counter(txt)
res4 = {}

for i in txt:
    res1[i] = res1.setdefault(i, 0) + 1

for i in txt:
    if i not in res2:
        res2[i] = txt.count(i)

for i in txt:
    if i not in res4:
        res4[i] = 0
    res4[i] += 1

print(res1, res2, res3, res4, sep='\n')