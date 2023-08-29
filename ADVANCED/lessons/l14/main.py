def is_prime(p: int) -> bool:
    """
    Checks the number P for simplicity using finding the
    remainder of the division in the range [2, P).
    """
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


help(is_prime)


# команды в терминале:

# 1. вход в режим интерпретатора
# python

# 2. импорт функции из файла
# from main import is_prime

# 3. запуск числа 42
# is_prime(42)

# 4. запуск числа 73
# is_prime(73)

# 5. выход в терминал
# exit()