
file = 'text_data.txt'
f = open(file, mode='r', buffering=-1, encoding=None, errors=None,
    newline=None, closefd=True, opener=None)
print(f) #<_io.TextIOWrapper name='text_data.txt' mode='r' encoding='cp1251'>
f.close()

f = open('text_data.txt', 'r', encoding='utf-8')
print(f) #<_io.TextIOWrapper name='text_data.txt' mode='r' encoding='utf-8'>
print(list(f))
f.close()

"""
'r' — открыть для чтения (по умолчанию)
'w' — открыть для записи, предварительно очистив файл
'x' — открыть для эксклюзивного создания. Вернёт ошибку, если файл уже существует
'a' — открыть для записи в конец файла, если он существует
'b' — двоичный режим
't' — текстовый режим (по умолчанию)
'+' — открыты для обновления (чтение и запись)
"""

f = open('bin_data', 'wb', buffering=64)
f.write(b'X' * 1200)
f.close()


f = open('data.txt', 'wb')
f.write('Привет, '.encode('utf-8') + 'мир!'.encode('cp1251'))
f.close()

f = open('data.txt', 'r', encoding='utf-8')
# print(list(f)) # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xec in position 14: invalid continuation byte
f.close()
f = open('data.txt', 'r', encoding='utf-8', errors='replace')
print(list(f))
f.close()


with open('text_data.txt', 'r+', encoding='utf-8') as f1, \
    open('bin_data', 'rb') as f2, \
    open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3:
    print(list(f1))
    print(list(f2))
    print(list(f3))

# для Python 3.10 новая запись
with (
        open('text_data.txt', 'r+', encoding='utf-8') as f1,
        open('bin_data', 'rb') as f2,
        open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3
    ):
    print(list(f1))
    print(list(f2))
    print(list(f3))


with open('text_data.txt', 'r', encoding='utf-8') as f:
    res = f.read()
    print(f'Читаем первый раз\n{res}')
    res = f.read()
    print(f'Читаем второй раз\n{res}') # бесполезно


with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline():
        print(res)


SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline(SIZE):
        print(res)


with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')


SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line[:-1])
        print(line.replace('\n', ''))


text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
    'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
    'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]


with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(f'{line}\n')
        print(f'{res = }\n{len(line) = }')


with open('new_data.txt', 'w+', encoding='utf-8') as f:
    f.writelines('\n'.join(text))


with open('new_data.txt', 'w+', encoding='utf-8') as f:
    for line in text:
        print(line, file=f)


SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line[:-1])
        print(line.replace('\n', ''))


text2 = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
with open('new_data.txt', 'w+', encoding='utf-8') as f:
    res = f.write(text2)
    print(f'{res = }\n{len(text2) = }')


with open('new_data.txt', 'w+', encoding='utf-8') as f:
    for line in text:
        res = f.write(line)
        print(f'{res = }\n{len(line) = }')


with open('new_data.txt', 'w+', encoding='utf-8') as f:
    for line in text:
        res = f.write(f'{line}\n')
        print(f'{res = }\n{len(line) = }')


with open('new_data.txt', 'w+', encoding='utf-8') as f:
    f.writelines('\n'.join(text))


with open('new_data.txt', 'w+', encoding='utf-8') as f:
    for line in text:
        print(line, file=f)


with open('new_data.txt', 'w', encoding='utf-8') as f:
    for line in text:
        print(line, end='***\n##', file=f)


with open('new_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
        print(f.tell())


last = before = 0
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
        print(f'{last = }, {before = }')
        print(f'{f.seek(before, 0) = }')
        f.write('\n'.join(text))


last = before = 0
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
        print(f.seek(before, 0))
        print(f.truncate())


size = 64
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    print(f.truncate(size))

# задание
start = 10
stop = 100
with open('data.bin', 'bw+') as f:
    for i in range(start, stop + 1):
        f.write(str(i).encode('utf-8'))
        if i % 3 == 0:
            f.seek(-2, 1)
            f.truncate(stop)
        f.seek(0)
        res = f.read(start)
        print(res.decode('utf-8'))

