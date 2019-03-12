
board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
chance = 0
mylist = [1,2,3,4,5,6,7,8,9]

def ask_first_player():
    # This function ask the player to chose their symbols
    # OUTPUT: list of symbols as [player1, player2]
    global chance
    player1 = input('Which one you will select? \'x\' or \'o\': ')
    while player1 != 'x' and player1 != 'o':
        player1 = input('Which one you will select? \'x\' or \'o\': ')

    if player1=='x':
        player2='o'
    else:
        player2='x'

    chance = player1

    return [player1, player2]
    

def display_board(board):

    print(' '*10 + board[7]+'|'+board[8]+'|'+board[9])
    
    print(' '*10 + board[4]+'|'+board[5]+'|'+board[6])
   
    print(' '*10 + board[1]+'|'+board[2]+'|'+board[3])

def check_win(new_board):
    if [new_board[1], new_board[2], new_board[3]] == ['o']*3 or [new_board[1], new_board[2], new_board[3]] == ['x']*3:
        return True
    elif [new_board[4], new_board[5], new_board[6]] == ['o']*3 or [new_board[4], new_board[5], new_board[6]] == ['x']*3:
        return True
    elif [new_board[7], new_board[8], new_board[9]] == ['o']*3 or [new_board[7], new_board[8], new_board[9]] == ['x']*3:
        return True
    elif [new_board[7], new_board[5], new_board[3]] == ['o']*3 or [new_board[7], new_board[5], new_board[3]] == ['x']*3:
        return True
    elif [new_board[1], new_board[5], new_board[9]] == ['o']*3 or [new_board[1], new_board[5], new_board[9]] == ['x']*3:
        return True
    else:
        return False

def get_input():
    
    global chance
    if chance == player1:
        playerstring = 'Player1'
    else:
        playerstring = 'Player2'

    location = int(input(playerstring + ' please enter the location: '))
    
    while not location in mylist:
        location = int(input(playerstring + ' please enter the location: '))
    
    board[location] = chance
    mylist.pop(mylist.index(location))

    display_board(board)

    if check_win(board):
        print(playerstring + ' Wins!')
    else:
        if chance == player1:
            chance = player2
        elif chance == player2:
            chance = player1
        else:
            pass

def check_location_filled():
    if ' ' in board:
        return False
    else:
        return True



[player1, player2] = ask_first_player()
print('Now play!')

display_board(board)

while not check_win(board):
    if check_location_filled():
        print('It\'s a draw')
        break
    else:
        get_input()
    



