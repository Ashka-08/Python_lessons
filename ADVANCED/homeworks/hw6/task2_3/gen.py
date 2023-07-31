from random import randint

from queens import check_queens

def arrange_queens():
    combinations = 4
    while combinations > 0:
        pos = list((i, randint(1, 8)) for i in range(1, 8))
        if check_queens(pos):
            print(*pos)
            combinations -= 1


if __name__ == "__main__":
    arrange_queens()