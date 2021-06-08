def display_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')

def place_marker(board,marker,position):
    board[position]=marker

def win_cheak(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


def space_cheak(board,position):
    return board[position] == ' '

def full_board_cheak(board):

    for i in range(1,10):
        if space_cheak(board,i):
            return False
    return True


def player_choice(board):
    position=' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_cheak(board,int(position)):
        position = input('choose your next position(1 to 9): ')
    return int(position)


def replay():
    return input('Do you want to play again?Enter Yes or No.').lower().startswith('y')



print('Welcome to tic tac toe!')
player1_marker, player2_marker = 'O','X'

while True:
    theBoard = [' ']*10
    turn = 'player 1'
    print('Player 1 will go first!')
    game_on = True
    while game_on:
        if turn == 'player 1':
            display_board(theBoard)
            print('PLAYER 1...symbol = O')
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)

            if win_cheak(theBoard,player1_marker):
                display_board(theBoard)
                print('congrats,player 1, has won !!')
                game_on = False
            else:
                if full_board_cheak(theBoard):
                    display_board(theBoard)
                    print('the game is draw!!')
                    break
                else:
                    turn='player 2'
        else:
            display_board(theBoard)
            print('PLAYER 2... symbol = X')
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_cheak(theBoard, player2_marker):
                display_board(theBoard)
                print('congrats,player 2, has won !!')
                game_on = False
            else:
                if full_board_cheak(theBoard):
                    display_board(theBoard)
                    print('the game is draw!!')
                    break
                else:
                    turn = 'player 1'
    if not replay():
        break
