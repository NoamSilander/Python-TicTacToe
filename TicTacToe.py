import time
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9',]

winning_combinations = ['012', '345', '678', '036', '147', '258', '048', '642']

game_running = False

def board_builder():
    print('+---+---+---+')
    print(f'| {board[0]} | {board[1]} | {board[2]} |')
    print('+---+---+---+')
    print(f'| {board[3]} | {board[4]} | {board[5]} |')
    print('+---+---+---+')
    print(f'| {board[6]} | {board[7]} | {board[8]} |')
    print('+---+---+---+')


while True:
    try:    
        start_input = str(input('Do you want to start a game of Tic Tac Toe? (y/n): ')).lower()
        if start_input not in ('y', 'n'):
            raise TypeError
        break
    except TypeError:
        pass

if start_input == 'y':
    game_running = True

elif start_input == 'n':
    game_running = False

while game_running:
    while True:
        choose_input = input('X or O (Player 2 gets the other): ').upper()
        if choose_input == 'X':
            player1 = 'X'
            player2 = 'O'
            break
        elif choose_input == 'O':
            player1 = 'O'
            player2 = 'X'
            break
    print(f'Player1 is {player1}, Player2 is {player2}')
    time.sleep(2)
    board_builder()
    
