# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: 
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более 
# чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего 
# конкурента?

# a) Добавьте игру против бота

from random import randint

def input_step(name):
    x = int(input(f"{name}, сколько конфет возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, попробуйте еще: "))
    return x

def message_print(name, step, v):
    print(f"Игрок {name} взял {step} конфет, осталось {v}.")

player1 = input("Введите имя игрока: ")
player2 = "Бот"
candy_lot = 151
max_step = 28

number_player = randint(0,2)
if number_player:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

while candy_lot > 28:
    if number_player:
        step = input_step(player1)
        candy_lot -= step
        number_player = False
        message_print(player1, step, candy_lot)
    else:
        step = randint(1,29)
        candy_lot -= step
        number_player = True
        message_print(player2, step, candy_lot)

if number_player:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")