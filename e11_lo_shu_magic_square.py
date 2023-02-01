ROW = 3
COL = 3


def main():
    numbers = [[4, 9, 2],
               [3, 5, 7],
               [8, 1, 6]]

    # row total
    row_list = []
    total_row = 0
    for row in range(ROW):
        total_row = 0
        for col in range(COL):
            value = numbers[row][col]
            total_row += value
        row_list.append(total_row)
    print(row_list)

    # column total
    column_list = []
    total_col = 0
    for col in range(COL):
        total_col = 0
        for row in range(ROW):
            value = numbers[row][col]
            total_col += value
        column_list.append(total_col)
    print(column_list)

    # diagonal left down
    diag1 = []
    diag1_total = 0
    for row in range(ROW):
        for col in range(COL):
            if col == row:
                diag1.append(numbers[row][col])
    for num in diag1:
        diag1_total += num
    print(diag1_total)

    # diagonal left up
    diag2 = []
    diag2_total = 0
    col = 0
    for row in range(ROW, 0, -1):
        diag2.append(numbers[row - 1][col])
        col += 1
    for num in diag2:
        diag2_total += num
    print(diag2_total)

    if total_row == total_col and total_row == diag1_total and total_row == diag2_total and total_col == diag1_total and total_col == diag2_total and diag1_total == diag2_total:
        print('The list is a Lo Shu Square')
    else:
        print('The list is NOT a Lo Shu Square')


if __name__ == '__main__':
    main()
