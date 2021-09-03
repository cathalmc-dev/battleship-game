from random import randint

size = None
LETTERS = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I",
           "J", "K", "L", "M", "N", "O"]
cpu_board = []
player_board = []
number_of_ships = 0
ship = []
ship1 = []
ship2 = []
ship3 = []
ship4 = []
ship5 = []


def set_grid_size():
    print("Please set the grid size using 1 integer.")
    print("The number of rows and columns will be equal.")
    message = "Please enter an integer between 5 and 9: "
    global size
    # https://stackoverflow.com/questions/52439284/error-handling-that-prompt-the-user-to-enter-only-integer-greater-than-1
    valid = False
    while not valid:
        size = input(message)
        try:
            size = int(size)
        except ValueError:
            message = "Please enter integer values only: "
        else:
            valid = 4 < size < 10
            if not valid:
                message = "Enter an integer between 5 and 9: "
    print(f"You have entered {size}.")


def initialize_board(board):
    board.append(LETTERS[:size + 1])
    for i in range(size):
        board.append([f"{i + 1}"] + ["0"] * size)


def print_board(board):
    for i in board:
        print(" ".join(i))


def print_boards():
    print("CPU")
    print_board(cpu_board)
    print(" ")
    print("Player")
    print_board(player_board)


def random_column(board):
    return randint(1, len(board[0]) - 1)


def random_row(board):
    return randint(1, len(board) - 1)


def amount_of_ships():
    global number_of_ships
    if size < 7:
        number_of_ships = 3
    elif size < 9:
        number_of_ships = 4
    else:
        number_of_ships = 5


def create_ship():
    column = random_column(cpu_board)
    row = random_row(cpu_board)
    length = randint(2, 5)
    orientation = randint(0, 1)
    if orientation == 0:
        for i in range(length):
            point = [(column + i)] + [row]
            ship.append(point)
    print(ship)

# def cpu_ships():
    

def main():
    """
    Run all program functions
    """
    set_grid_size()
    initialize_board(cpu_board)
    initialize_board(player_board)
    print_boards()
    # column = LETTERS[random_column(cpu_board)]
    # row = random_row(cpu_board)
    # print(column, row)
    create_ship()


print("Welcome to Battleships!")
main()
