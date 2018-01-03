import time

board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]


def print_header():
    print("TIC TAC TOE")
    print("Rules: ")
    print("  " + "Player_1 symbols X and Player_2 symbols O  ")


def print_board():
    print('      |     |      ')
    print(' ' + board[1] + '    |' + board[2] + '    |' + board[3] + ' ')
    print(' -----|-----|------')
    print('      |     |      ')
    print(' ' + board[4] + '    | ' + board[5] + '   | ' + board[6] + ' ')
    print(' -----|-----|------')
    print('      |     |      ')
    print(' ' + board[7] + '    | ' + board[8] + '   | ' + board[9] + ' ')


while True:
    print_header()
    print_board()
    # Get Player 1 input
    choice = input("Choose any empty space for Player_1: ")
    choice = int(choice)

    # Check to see if the space is empty
    if board[choice] == " ":
        board[choice] = "X"
    else:
        print("Sorry, space is not empty! ")
        time.sleep(1)
        print("Please choose another empty space")
        time.sleep(1)
    # Check for Player 1 win
    if board[1] == "X" and board[2] == "X" and board[3] == "X" or \
            board[4] == "X" and board[5] == "X" and board[6] == "X" or \
            board[7] == "X" and board[8] == "X" and board[9] == "X" or \
            board[1] == "X" and board[4] == "X" and board[7] == "X" or \
            board[2] == "X" and board[5] == "X" and board[8] == "X" or \
            board[3] == "X" and board[6] == "X" and board[9] == "X" or \
            board[1] == "X" and board[5] == "X" and board[9] == "X" or \
            board[3] == "X" and board[5] == "X" and board[7] == "X":
        print_board()
        print("Congratulations! X wins")
        break
    print_header()
    print_board()

    # check for tie
    isFull = True
    if " " in board:
        isFull = False

    if isFull:
        print(" Game tie ")

    # Get player 2 input
    choice = input("Choose any empty space for Player_2: ")
    choice = int(choice)

    # Check to see if space is empty
    if board[choice] == " ":
        board[choice] = "O"
    else:
        print("Sorry, space is not empty! ")
        time.sleep(1)
        print("Please choose another empty space")
        time.sleep(1)

    # Check for Player 2 win
    if board[1] == "O" and board[2] == "O" and board[3] == "O" or \
            board[4] == "O" and board[5] == "O" and board[6] == "O" or \
            board[7] == "O" and board[8] == "O" and board[9] == "O" or \
            board[1] == "O" and board[4] == "O" and board[7] == "O" or \
            board[2] == "O" and board[5] == "O" and board[8] == "O" or \
            board[3] == "O" and board[6] == "O" and board[9] == "O" or \
            board[1] == "O" and board[5] == "O" and board[9] == "O" or \
            board[3] == "O" and board[5] == "O" and board[7] == "O":
        print_board()
        print("Congratulations! O wins")
        break

    # check for tie
    isFull = True
    if " " in board:
        isFull = False

    if isFull:
        print(" Game tie ")
