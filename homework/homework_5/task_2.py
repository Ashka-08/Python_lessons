# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: 
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более 
# чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего 
# конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def input_step(name):
    x = int(input(f"{name}, сколько конфет возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, попробуйте еще: "))
    return x

def message_print(name, k, v):
    print(f"Игрок {name} взял {k} конфет, осталось {v}.")

candy_lot = 151
max_step = 28
print(
    'Игра с конфетами.\n'
    f'На столе лежит {candy_lot} конфета.\n' 
    'Играют два игрока делая ход друг после друга.\n'
    'Первый ход определяется жеребьёвкой.\n'
    f'За один ход можно забрать не более чем {max_step} конфет.\n'
    'Все конфеты оппонента достаются сделавшему последний ход.\n'
    )

player1 = input('Имя 1 игрока: ')
player2 = input('Имя 2 игрока: ')
print(f'{player1} и {player2}, начнем игру!')

# Определение очередности ходов
number_player = randint(0, 1) 
number_player = randint(0,2)
if number_player:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

# цикл ходов
while candy_lot > 28:
    if number_player:
        k = input_step(player1)
        candy_lot -= k
        number_player = False
        message_print(player1, k, candy_lot)
    else:
        k = input_step(player2)
        candy_lot -= k
        number_player = True
        message_print(player2, k, candy_lot)

print()
if number_player:
    print(f"Оставшиеся конфеты достаются игроку {player1}. Победа за ним")
else:
    print(f"Оставшиеся конфеты достаются Игроку {player2}. Победа за ним")