from random import randint

size = None
cpu_board = []
player_board = []
boards = cpu_board + player_board

def set_grid_size():
    print("Please set the grid size using 1 integer.")
    print("The number of rows and columns will be equal.")
    message = "Please enter an integer between 5 and 15: "
    global size
    valid = False
    while not valid:
        size = input(message)
        try:
            size = int(size)
        except ValueError:
            message = "Please enter integer values only: "
        else:
            valid = 4 < size < 16
            if not valid:
                message = "Enter an integer between 5 and 15: "
    print(f"You have entered {size}.")


def initialize_board(board):
    for i in range(size):
        board.append(["0"] * size)


def print_board(board):
    for i in board:
        print(" ".join(i))

def main():
    """
    Run all program functions
    """
    set_grid_size()
    initialize_board(cpu_board)
    initialize_board(player_board)
    print_board(cpu_board)
    print(" ")
    print_board(player_board)


print("Welcome to Battleships!")
main()
