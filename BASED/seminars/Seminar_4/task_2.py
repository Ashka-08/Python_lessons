# В текстовом файле посчитать количество строк, а также для каждой отдельной строки 
# определить количество в ней символов и слов.

data = open('file.txt', 'r', encoding='UTF-8')

for s in data.readlines():
    print(s, end='')
    print(f'Количество символов = {len(s)}')
    print(f"Количество слов = {len(s.split())}")
    print()
data.close()