# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

numbers = [1, 2, 3]
s = 'super'
letter = 'a'

def rename():
    variables = globals()
    temp = {}
    for key, value in variables.items():
        if len(key) > 1 and key.endswith('s'):
            temp[key[:-1]] = variables[key]
            temp[key] = None
    variables.update(temp)

rename()

# print(numbers, s, letter, number) #None super a [1, 2, 3]

print({key: values for key, values in locals().items() if not key.startswith('__')})
# {'numbers': None, 's': 'super', 'letter': 'a', 'rename': <function rename at 0x0000016561D1D9E0>, 'number': [1, 2, 3]}
