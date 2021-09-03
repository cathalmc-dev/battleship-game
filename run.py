from random import randint

size = None
LETTERS = [" ", "A", "B", "C", "D", "E"]
cpu_board = []
player_board = []
ship = []


def set_grid_size():
    print("Please set the grid size using 1 integer.")
    print("The number of rows and columns will be equal.")
    message = "Please enter an integer between 3 and 5: "
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
            valid = 2 < size < 6
            if not valid:
                message = "Enter an integer between 3 and 5: "
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
    if size < 4:
        number_of_ships = 3
    elif size < 5:
        number_of_ships = 4
    else:
        number_of_ships = 5
    return number_of_ships


def create_ship():
    column = random_column(cpu_board)
    row = random_row(cpu_board)
    ship = [column] + [row]
    print(ship)
    valid = ship_on_grid()
    if not valid:
        create_ship()
    else:
        return ship


def ship_on_grid():
    valid = True
    for i in ship:
        if i[0] > size:
            valid = False
            break
        elif i[1] > size:
            valid = False
            break
        else:
            valid = True
    return valid

def create_cpu_ships():
    ships = []
    ships.append(create_ship() * amount_of_ships())
    print(ships)

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
