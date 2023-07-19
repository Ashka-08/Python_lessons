# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в верхнем регистре, если в строке есть хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях

import re

data = input('Введите данные: ')
if data.isdigit():
    print('Целое положительное число', int(data))
elif (data.replace('.', '')).isdigit():
    print('Вещественное положительное число', float(data))
elif data.startswith('-') and (data.replace('.', ''))[1::].isdigit():
    print('Вещественное отрицательное число', float(data))
elif re.match(r"\d+\.*\d*", data) or re.match(r"-\d+\.*\d*", data):
    print('Вещественное положительное или отрицательное число', float(data))
elif any(i.isupper() for i in data):
    print('Строка в верхнем регистре', data.upper())
# elif not data.islower():
#     print('Строка в верхнем регистре', data.upper()
else:
    print('Строка в нижнем регистре', data.lower())