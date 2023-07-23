# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def make_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, int | str | float | bool | tuple):
            result[value] = key
        else:
            result[str(value)] = key
    return result


print(make_dict(string='строка',
                     num=55,
                     flag=True,
                     my_list=['a', 'b', 'c']))