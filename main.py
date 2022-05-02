def put_x():
    position_x = input('Where do you want to put X? Type the number of row (1-3) and the number of column (1-3) '
                 'without space:\n')
    try:
        num_row_x = int(position_x[0])
        num_col_x = int(position_x[1])
        if map[num_row_x - 1][num_col_x - 1] == "⬜️":
            map[num_row_x - 1][num_col_x - 1] = "X"
            print(f"{row1}\n{row2}\n{row3}")
        else:
            print("This position is already taken")
            put_x()
    except (ValueError, IndexError):
        print("Invalid character, please type 2 digits from 1 to 3 without space")
        put_x()


def put_o():
    position_o = input('Where do you want to put O? Type the number of row (1-3) and the number of column (1-3) '
                 'without space:\n')
    try:
        num_row_o = int(position_o[0])
        num_col_o = int(position_o[1])
        if map[num_row_o - 1][num_col_o - 1] == "⬜️":
            map[num_row_o - 1][num_col_o - 1] = "O"
            print(f"{row1}\n{row2}\n{row3}")
        else:
            print("This position is already taken")
            put_o()
    except (ValueError, IndexError):
        print("Invalid character, please type 2 digits from 1 to 3 without space")
        put_o()


def check():
    if row1 == ["X", "X", "X"] or row2 == ["X", "X", "X"] or row3 == ["X", "X", "X"]:
        print("X wins!")
        return 1
    elif row1[0] == "X" and row2[0] == "X" and row3[0] == "X":
        print("X wins!")
        return 1
    elif row1[1] == "X" and row2[1] == "X" and row3[1] == "X":
        print("X wins!")
        return 1
    elif row1[2] == "X" and row2[2] == "X" and row3[2] == "X":
        print("X wins!")
        return 1
    elif row1[0] == "X" and row2[1] == "X" and row3[2] == "X":
        print("X wins!")
        return 1
    elif row1[2] == "X" and row2[1] == "X" and row3[0] == "X":
        print("X wins!")
        return 1
    elif row1 == ["O", "O", "O"] or row2 == ["O", "O", "O"] or row3 == ["O", "O", "O"]:
        print("O wins!")
        return 1
    elif row1[0] == "O" and row2[0] == "O" and row3[0] == "O":
        print("O wins!")
        return 1
    elif row1[1] == "O" and row2[1] == "O" and row3[1] == "O":
        print("O wins!")
        return 1
    elif row1[2] == "O" and row2[2] == "O" and row3[2] == "O":
        print("O wins!")
        return 1
    elif row1[0] == "O" and row2[1] == "O" and row3[2] == "O":
        print("O wins!")
        return 1
    elif row1[2] == "O" and row2[1] == "O" and row3[0] == "O":
        print("O wins!")
        return 1
    else:
        return 0

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

game_on = True
while game_on:
    put_x()
    if check() == 1:
        break
    put_o()
    if check() == 1:
        game_on = False