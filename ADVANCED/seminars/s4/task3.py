# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def make_dick(string: str):
    beginning, ending = sorted(string.split())
    return {ord(str(x)): x for x in range(int(beginning), int(ending)+1)}


print(make_dick(' 7 3'))