import os
from pathlib import Path
import shutil


# Текущий каталог

print(os.getcwd())
print(Path.cwd())

print(os.getcwd())
print(Path.cwd())
os.chdir('../..')
print(os.getcwd())
print(Path.cwd())


# Создание каталогов

os.mkdir('new_os_dir')
Path('new_path_dir').mkdir()

os.makedirs('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').mkdir() # FileNotFoundError
Path('some_dir/dir/new_path_dir').mkdir(parents=True)

# os.rmdir('dir') # OSError
# Path('some_dir').rmdir() # OSError
os.rmdir('dir/other_dir/new_os_dir')
Path('some_dir/dir/new_path_dir').rmdir()


# Удаление каталогов

shutil.rmtree('dir/other_dir')
shutil.rmtree('some_dir')


# Формирование пути

file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
print(f'{file_1 = }\n{file_1}')

file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_2 = }\n{file_2}')


# Чтение данных о каталогах

print(os.listdir())

p = Path(Path().cwd())
for obj in p.iterdir():
    print(obj)


# Проверка на директорию, файл и ссылку

dir_list = os.listdir()
for obj in dir_list:
    print(f'{os.path.isdir(obj) = }', end='\t')
    print(f'{os.path.isfile(obj) = }', end='\t')
    print(f'{os.path.islink(obj) = }', end='\t')
    print(f'{obj = }')

p = Path(Path().cwd())
for obj in p.iterdir():
    print(f'{obj.is_dir() = }', end='\t')
    print(f'{obj.is_file() = }', end='\t')
    print(f'{obj.is_symlink() = }', end='\t')
    print(f'{obj = }')


# Обход папок через os.walk()

for dir_path, dir_name, file_name in os.walk(os.getcwd()):
    print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')


# Переименование файлов

os.rename('old_name.py', 'new_name.py')

p = Path('old_file.py')
p.rename('new_file.py')

Path('new_file.py').rename('newest_file.py')


# Перемещение файлов

os.replace('newest_file.py', os.path.join(os.getcwd(), 'dir', 'new_name.py'))

old_file = Path('new_name.py')
new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)


# Копирование файлов

shutil.copy('one.txt', 'dir')
shutil.copy2('two.txt', 'dir') #+метаданные


#скопировать каталог со всем его содержимым в новое место

shutil.copytree('dir', 'one_more_dir') 


# Удаление файлов

os.remove('one_more_dir/one.txt')
Path('one_more_dir/one_more.txt').unlink()


# Удаление всего каталога целиком с содержимым

shutil.rmtree('dir')


# задание

for i in range(10):
    with open(f'file_{i}.txt', 'w', encoding='utf-8') as f:
        f.write('Hello world!')
os.mkdir('new_dir')
for i in range(2, 10, 2):
    f = Path(f'file_{i}.txt')
    f.replace('new_dir' / f)
shutil.copytree('new_dir', Path.cwd() / 'dir_new')

