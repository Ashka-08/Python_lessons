# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

import re
from string import ascii_letters
from doctest import testmod


def string_cleaner(s):
    return re.sub(r'[^a-z ]*', '', s.lower())


def removal(input_str):
    # """
    # Удаляет все символы, кроме латинских букв в нижнем регистре и пробелов:
    # >>> removal('language')
    # 'language'
    # >>> removal('LanguagE')
    # 'language'
    # >>> removal('l,an.gu:a!g?e')
    # 'language'
    # >>> removal('lфanguage')
    # 'language'
    # >>> removal('Lфв,an.gu:a!g?E')
    # 'language'
    # """
    rezult = ''
    for i in input_str:
        if i in ascii_letters or i == ' ':
            rezult += i.lower()
    return rezult

if __name__ == '__main__':
    input_str = 'Pф3$y.t,hoN| i**s --a g(o)Od LanguagE'
    print(f'Исходная строка: {input_str}')
    print(removal(input_str))
    print(string_cleaner(input_str))

    testmod(verbose=True)