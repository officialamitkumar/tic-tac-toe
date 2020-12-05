from IPython.display import clear_output

def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('------------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('------------')

    
test_board=['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)
display_board(test_board)

def player_input():
    '''
    OUTPUT = (Player 1 marker,Player 2 marker)
    '''
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker=input('Player1: Choose X or O: ').upper()
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')
    
    
player1_marker , player2_marker = player_input()

def place_marker(board, marker, position):
    board[position] = marker
    
place_marker(test_board,'$',8)
display_board(test_board)

def win_check(board,mark):
    
    return((board[7]==mark and board[8]==mark and board[9]==mark) or #across
    (board[4]==mark and board[5]==mark and board[6]==mark) or #across
    (board[1]==mark and board[2]==mark and board[3]==mark) or #across
    (board[7]==mark and board[4]==mark and board[1]==mark) or  #downward
    (board[8]==mark and board[5]==mark and board[2]==mark) or # downward
    (board[9]==mark and board[6]==mark and board[3]==mark) or #downward
    (board[7]==mark and board[5]==mark and board[3]==mark) or # diagonal
    (board[9]==mark and board[5]==mark and board[1]==mark)) #diagonal


win_check(test_board,'X')



import random
def choose_first():
    flip=random.randint(0,1)
    
    if flip == 0:
        return 'player 1'
    else:
        return 'player 2' 
    
def space_check(board,position):
    return board[position] == ' '


def full_board_check(board):
    
    for i in range(0,10):
        if space_check(board,i):
            return False
    return True


def player_choice(board):
    
    position = 0 
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Choose Position: (1-9)'))
        
    return position

def replay():
    choice = input("play again? Enter Yes or No")
    
    return choice =='Yes'