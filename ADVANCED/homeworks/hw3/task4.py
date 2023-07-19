# Создайте словарь со списком вещей для похода в качестве ключа 
# и их массой в качестве значения. Определите какие вещи влезут в рюкзак 
# передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

from random import choice

d = \
    {
        'палатка' : 5,
        'спальник' : 2,
        'вещи' : 3,
        'еда' : 7,
        'аптечка' : 1,
    }
MAX = 10
count = 0
fit = {}
while count < MAX:
    key, value = choice(list(d.items()))
    if count + value > MAX:
        break
    count += value
    fit.setdefault(key, value)

print(fit, "=", count)