# Напишите следующие функции:
# * Нахождение корней квадратного уравнения
# * Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# * Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# * Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.

import csv
import json
import math
import os
from random import randint

file_csv = 'ADVANCED\homeworks\hw9\my_file.csv'
file_json = 'ADVANCED\homeworks\hw9\my_file.json'


def generate_csv(rows, filename):
    with open(filename, 'w+', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        for _ in range(rows):
            lst = []
            for _ in range(3):
                lst.append(randint(-10, 10))
            csv_writer.writerow(lst)


def deco_maker_equations(func):
    def wrapper(*args, **kwargs):
        with open(file_csv, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
            for row in csv_reader:
                a, b, c = map(int, row)
                if a != 0:
                    func(a, b, c)
        result = func(*args, **kwargs)
        return result
    return wrapper


def deco_json_saver(func):
    counter = 0
    def wrapper(*args):
        nonlocal counter
        try:
            with open(file_json, 'r') as f_read:
                data = json.load(f_read)
        except:
            data = {}
        with open(file_json, 'w', encoding='utf-8') as f_write:
            solution = func(*args)
            diction = {
                'a' : args[0],
                'b' : args[1],
                'c' : args[2],
                'x1, x2' : solution
            }
            data[counter] = diction
            json.dump(data, f_write, indent=2, ensure_ascii=False)
        result = func(*args)
        counter += 1
        return result

    return wrapper


@deco_maker_equations
@deco_json_saver
def quadratic_equations(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif discriminant == 0:
        x = -b / (2 * a)
        return round(x, 2)

generate_csv(100, file_csv)
quadratic_equations(1, 2, -3)
