# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она возвращает. 
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

import json


def json_saver(func):
    def wrapper(*args, **kwargs):
        with open(f'ADVANCED\seminars\s9\{func.__name__}.json', 'a', encoding='utf-8') as file:
            temp_dict = {'args' : args}
            temp_dict.update(kwargs)
            result = func(*args, **kwargs)
            temp_dict['result'] = result
            json.dump(temp_dict, file, ensure_ascii=False, indent=2)
        return result
    return wrapper

@json_saver
def find_max(a, b, c='9'):
    return max(a, b, c)

# print(find_max(1, 4, c= 9))
print(find_max(10, 4, c= 5))