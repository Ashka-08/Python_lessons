# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

# num: int = int(input('Введите число: '))
# sys_select: int = int(input('Введите систему исчесления: '))
# res: str = ''
# n: int = num
# while n > 0:
#     res = str(n % sys_select) + res
#     n = n // sys_select
# print(res)
# print('Проверка:')
# if sys_select == 2:
#     print(bin(num)[2:])
# elif sys_select == 8:
#     print(oct(num)[2:])


BINARY: int = 2
OCTAL: int = 8
number: int = int(input('Введите число: '))

def convert(number: int, n_sys: int) -> str:
    result = list()
    while number > 0:
        result.append(str(number % n_sys))
        number //= n_sys
    return ''.join(reversed(result))

print(bin(number)[2:] == convert(number, BINARY))
print(oct(number)[2:] == convert(number, OCTAL))