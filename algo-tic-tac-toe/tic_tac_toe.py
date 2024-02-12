import random

# Function to print board
def print_board(board):
    for row in board:
        print('-' * 9)
        print(" | ".join(row))
    print('-' * 9)

# Check board as 2D 3x3 grid for a winning combo, board[row[column]]
# Rows, columns, and diagonals
def check_winner(board):
    for i in range(3):
        # If all in a row equal, return first item in row
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
        # If all in a column equal, return first item in a column
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]
    # Diagonal cases
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

# Check if the board is full or not
def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Find all empty cells
def empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

# Simulate computer move
def computer_move(board):
    moves = empty_cells(board)
    return random.choice(moves)

# Main function
def main():
    # Create new board
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    
    # Get user choice of mark
    sym = ''
    comp_sym = ''
    while sym != 'X' and sym != 'O':
        sym = input("Would you like to be X or O? ")
        if sym == 'X':
            comp_sym = "O"
        elif sym == 'O':
            comp_sym = "X"
        else:
            print("Not a valid choice. Try again.")
            continue
    
    # Start loop
    moves = 0
    while moves <= 9:
        # Show player empty board
        print_board(board)
        # Get user input and display on board
        user_choice = False
        while user_choice == False: 
            row = int(input("Select a row (1, 2, or 3): ")) - 1
            col = int(input("Select a column (1, 2, or 3): ")) - 1
            if board[row][col] != ' ':
                print("That space is filled. Try again.")
                continue
            else:
                board[row][col] = sym
                user_choice = True
        
        # Check if the player wins
        if check_winner(board) == sym:
            print_board(board)
            print("You win!")
            break
        
        # Check if board is full
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Computer move
        print("Computer's move:")
        comp_tuple = computer_move(board)
        board[comp_tuple[0]][comp_tuple[1]] = comp_sym
        
        # Check if the computer wins
        if check_winner(board) == comp_sym:
            print_board(board)
            print("Computer wins!")
            break
        
        # Check if the board is full again
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        moves += 1
        
# Run main
if __name__ == "__main__":
    main()
