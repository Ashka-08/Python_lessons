# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем 
# и знаменателем. Программа должна возвращать сумму и произведение дробей. 
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def c_gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

a = list(map(int, input('Введите 1 дробь вида “a/b”: ').split('/')))
b = list(map(int, input('Введите 2 дробь вида “a/b”: ').split('/')))

# сумма дробей
sum_up = a[0] * b[1] + a[1] * b[0]
sum_down = a[1] * b[1]
res_up = int(sum_up / c_gcd(sum_up, sum_down))
res_down = int(sum_down / c_gcd(sum_up, sum_down))
print(f'сумма {res_up}/{res_down}')
print('Проверка', Fraction(a[0], a[1]) + Fraction(b[0], b[1]))
print()

# умножение дробей
pr_up = a[0] * b[0]
pr_down = b[1] * a[1]
res_pr_up = int(pr_up / c_gcd(pr_up, pr_down))
res_mpr_down = int(pr_down / c_gcd(pr_up, pr_down))
print(f"произведение {res_pr_up}/{res_mpr_down}")
print('Проверка', Fraction(a[0], a[1])*Fraction(b[0], b[1]))