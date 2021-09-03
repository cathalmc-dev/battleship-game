from random import randint


size = None
cpu_board = []
player_board = []
boards = cpu_board + player_board

def set_grid_size():
    global size
    size = input('Set grid row and column size: ')


def main():
    """
    Run all program functions
    """
    set_grid_size()
    print(size)


print("Welcome to Battleships!")
main()
