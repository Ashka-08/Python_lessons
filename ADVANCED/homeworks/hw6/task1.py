# В модуль с проверкой даты добавьте возможность запуска в терминале 
# с передачей даты на проверку.

from sys import argv
from datetime import datetime


def check(input_date):
    *_, year = list(input_date.split("."))
    try:
        datetime.strptime(input_date, "%d.%m.%Y").date()
        check_year(int(year))
        return True
    except ValueError:
        print("Где-то ошибка")
        return False


def check_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Високосный")
    else:
        print("Не високосный")


if __name__ == "__main__":
    # print(check(input('Введите дату в формате DD.MM.YYYY: ')))
    print(check(*(argv[1:])))

""" запуск в win cmd
Ввод 1 :
python task1.py 21.03.1989
Вывод:
Не високосный
True

Ввод 2
python task1.py 33.01.2020
Вывод:
Где-то ошибка
False

Ввод 3:
python task1.py 13.01.2020
Вывод:
Високосный
True
"""
