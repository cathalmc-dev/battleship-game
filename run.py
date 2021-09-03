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


def main():
    """
    Run all program functions
    """
    set_grid_size()
    print(size)


print("Welcome to Battleships!")
main()
