# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

# num: int = int(input('Введите число: '))
# SYS_SELECT: int = 16
# res: str = ''
# n: int = num
# while n > 0:
#     dif = n % SYS_SELECT
#     if dif == 10:
#         dif = 'A'
#     elif dif == 11:
#         dif = 'B'
#     elif dif == 12:
#         dif = 'C'
#     elif dif == 13:
#         dif = 'D'
#     elif dif == 14:
#         dif = 'E'
#     elif dif == 15:
#         dif = 'F'
#     else:
#         dif = str(dif)
#     res += dif
#     n = n // SYS_SELECT
# print(res[::-1])
# print('Проверка:')
# print(hex(num)[2:])


# решение преподавателя
num = int(input('Введите число в десятичной системе: '))
print(f'Встроенная функция hex -> \t\t{hex(num)}')


def self_hex(number: int) -> str:
    if not number:
        return '0x0'
    result = ''
    hex_letters = list('0123456789abcdef')
    while number > 0:
        result = hex_letters[number % 16] + result
        number //= 16
    return '0x' + result


print(f'Собственная функция self_hex -> {self_hex(num)}')