# Tic Tac Toe

# Initialize the board
board = [' ' for _ in range(9)]
print("The number 0-9 depicts the order of the entries of the player row wise.")
print("Demo:")
print("1|2|3")
print("-----")
print("4|5|6")
print("-----")
print("7|8|9")
print("-----")

# Function to print the board
def print_board():
    print(' | '.join(board[0:3]))
    print('---------')
    print(' | '.join(board[3:6]))
    print('---------')
    print(' | '.join(board[6:9]))

# Function to check if someone has won
def check_win(player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full
def check_draw():
    return ' ' not in board

# Main game loop
current_player = 'X'
while True:
    print_board()
    move = input(f"Player {current_player}, enter your move (1-9): ")
    try:
        move = int(move) - 1
        if 0 <= move < 9 and board[move] == ' ':
            board[move] = current_player
            if check_win(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                break
            elif check_draw():
                print_board()
                print("It's a draw!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")
    except ValueError:
        print("Invalid input. Enter a number between 1 and 9.")