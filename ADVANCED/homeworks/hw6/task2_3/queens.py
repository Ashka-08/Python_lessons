def check_queens(position):
    hit = True
    for i in range(len(position)):
        row, col = position[i]
        for j in range(i + 1, len(position)):
            row_2, col_2 = position[j]
            if row == row_2 or col == col_2 or abs(row - row_2) == abs(col - col_2):
                hit = False
    return hit


if __name__ == "__main__":
    pass