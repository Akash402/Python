# TicTac toe

test_board = [' ']*10
positionList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def instructions():
    board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print("Welcome to Tic Tac Toe :)")
    print("Player 1 gets to choose his/her marker, The markers can be 'X' or 'O'.")
    print("Tic Tac Toe board structure as per the position mapping is shown below.")
    print("Good Luck :)")
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])


def display(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])


def full_board_check(board):
    count = 0
    for i in range(1, len(board)):
        if board[i] == 'X' or board[i] == 'O':
            count += 1

    return count == 9


def win_check(board):
    for i in range(1, 10, 3):  # Horizontal wins
        if board[i] == 'X' and board[i + 1] == 'X' and board[i + 2] == 'X':
            print('X has won!')
            exit(0)
        elif board[i] == 'O' and board[i + 1] == 'O' and board[i + 2] == 'O':
            print('O has won!')
            exit(0)
        else:
            pass

    for i in range(1, 4):  # Vertical wins
        if board[i] == 'X' and board[i + 3] == 'X' and board[i + 6] == 'X':
            print('X has won!')
            exit(0)
        elif board[i] == 'O' and board[i + 3] == 'O' and board[i + 6] == 'O':
            print('O has won!')
            exit(0)
        else:
            pass

    for i in range(1, 9, 4):  # Diagonal 1 wins
        if board[i] == 'X' and board[i + 4] == 'X' and board[i + 8] == 'X':
            print('X has won!')
            exit(0)
        elif board[i] == 'O' and board[i + 4] == 'O' and board[i + 8] == 'O':
            print('O has won!')
            exit(0)
        else:
            break

    for i in range(3, 7, 2):  # Diagonal 2 wins
        if board[i] == 'X' and board[i + 2] == 'X' and board[i + 4] == 'X':
            print('X has won!')
            exit(0)
        elif board[i] == 'O' and board[i + 2] == 'O' and board[i + 4] == 'O':
            print('O has won!')
            exit(0)
        else:
            break


def play_tic_tac_toe(board):
    marker = ''
    player1_marker = ''
    player2_marker = ''
    boardflag = False
    player1_position = 0
    player2_position = 0
    while marker != 'X' and marker != 'O':
        marker = input("Player 1: Enter Either 'X' or an 'O' - ")
        player1_marker = marker
        if player1_marker == 'X':
            player2_marker = 'O'
        else:
            player2_marker = 'X'

    while not boardflag:
        if not full_board_check(board):
            player1_position = int(input('Player 1: Enter position from 1-9 '))
            while player1_position in positionList and player1_position != player2_position:
                print('Player: 1, Marker: {}, Position: {}'.format(player1_marker, player1_position))
                place_marker(board, player1_marker, player1_position)
                display(board)
                win_check(board)
                break
        else:
            boardflag = True

        if not full_board_check(board):
            player2_position = int(input('Player 2: Enter position from 1-9 '))
            while player2_position in positionList and player2_position != player1_position:
                print('Player: 2, Marker: {}, Position: {}'.format(player2_marker, player2_position))
                place_marker(board, player2_marker, player2_position)
                display(board)
                win_check(board)
                break
        else:
            boardflag = True
    else:
        print('Board is full! The game was a draw')


def place_marker(board, marker, position):
    board[position] = marker

instructions()
play_tic_tac_toe(test_board)
display(test_board)
