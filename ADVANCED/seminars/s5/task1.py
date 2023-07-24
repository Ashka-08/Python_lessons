# Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# * второе и третье число являются ключами.
# * первое число является значением для первого ключа.
# * четвертое и все возможные последующие числа хранятся в кортеже 
# как значения второго ключа.

# v1
# dct = {}
# data = input('Введите 4 или более числа через "/": ').split('/')
# dct[data[1]] = data[0]
# dct[data[2]] = data[3:]
# print(dct)

# v2
a, b, c, *d = input('Введите 4 или более числа через "/": ').split('/')
print({b: a, c: d})