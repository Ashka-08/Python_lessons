import sys

# print()

print(object, sep=' ', end='\n', file=sys.stdout, flush=False)
# sep по умолчанию пробел. Разделяет все объекты, перечисленные через запятую, н-р список
# end по умолчанию'\n'. То, что print() добавляет после вывода всех объектов
# file – ожидается объект с методом write (string), по умолчанию sys.stdout;
# Если flush=True, поток принудительно сбрасывается в файл, по умолчанию False

# вывод в файл
sourceFile = open('python.txt', 'w')
print("Круто же, правда?", file = sourceFile)
sourceFile.close()

# тернарный оператор
my_math = int(input('2 + 2 = '))
print('Верно!' if 2 + 2 == my_math else 'Вы уверены?')


"""
'r' открытие на чтение (является значением по умолчанию).
'w' открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
'x' открытие на запись, если файла не существует, иначе исключение.
'a' открытие на дозапись, информация добавляется в конец файла.
'b' открытие в двоичном режиме.
't' открытие в текстовом режиме (является значением по умолчанию).
'+' открытие на чтение и запись"""

# if
passw = 'text'
result = input('Input password: ')
if result == passw:
    print('Доступ разрешён')

# else
pwd = 'text'
res = input('Input password: ')
if res == pwd:
    print('Доступ разрешён')
    my_math = int(input('2 + 2 = '))
    if 2 + 2 == my_math:
        print('Вы в нормальном мире')
    else:
        print('Но будьте осторожны')
else:
    print('Доступ запрещён')
print('Работа завершена')

# elif
color = input('Твой любимый цвет: ')
if color == 'красный':
    print('Любитель яркого')
elif color == 'зелёный':
    print('Ты не охотник?')
elif color == 'синий':
    print('Ха, классика!')
else:
    print('Тебя не понять')

# match и case
color = input('Твой любимый цвет: ')
match color:
    case 'красный' | 'оранжевый':
        print('Любитель яркого')
    case 'зелёный':
        print('Ты не охотник?')
    case 'синий' | 'голубой':
        print('Ха, классика!')
    case _:
        print('Тебя не понять')

# Логические выражжения
year = int(input('Введите год в формате yyyy: '))
if year % 4 != 0:
    print("Обычный")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Високосный")

if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print("Обычный")
else:
    print("Високосный")

# in
data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
num = int(input('Введи число: '))
if num in data:
    print('Леонардо передаёт привет!')
elif num not in data:
    print('Леонардо грустит :-(')

# while
num = float(input('Введите число: '))
count = 0
while count < num:
    print(count)
    count += 2

num = float(input('Введите число: '))
STEP = 2
limit = num - STEP
count = -STEP
while count < limit:
    count += STEP
    if count % 12 == 0:
        continue # прервать и досрочно вернуться к проверке условия
    print(count)

min_limit = 0
max_limit = 10
while True: # бесконечный цикл
    print('Введи число между', min_limit, 'и', max_limit, '? ')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break # для досрочного завершения
print('Было введено число ' + str(num))

min_limit = 0
max_limit = 10
count = 3
while count > 0:
    print('Попытка ' + str(count))
    count -= 1
    num = float(input('Введи число между ' + str(min_limit) + ' и ' + str(max_limit) + ': '))
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break
else: # выход из цикла по "лжи" в while
    print('Исчерпаны все попытки. Сожалею.')
    quit()
print('Было введено число ' + str(num))

# for in
data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
for item in data:
    print(item)

# range(start, stop, step)
num = int(input('Введите число: '))
for i in range(0, num, 2):
    print(i)

# Имена переменных в цикле
count = 10
for i in range(count):
    for j in range(count):
        for k in range(count):
            print(i, j, k)
        
animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
for animal in animals:
    print(animal)

# enumerate()
animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
for i, animal in enumerate(animals, start=1):
    print(i, animal)