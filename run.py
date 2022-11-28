""" Battleship game - Single Player """
# pylint: disable-all

from random import randrange

# Global variable for board size
board_size = 5
# Global variable for computer ships coordinates
computer_coordinates = []
# Global variable for user ships coordinates
user_coordinates = []
# Global variable for game board
user_board = [["."] * board_size for i in range(board_size)]
computer_board = [["."] * board_size for i in range(board_size)]
# Global variable to store hit points of user
user_hp = 1
# Global variable to store hit points of computer
computer_hp = 1


class Board:
    """
    Battleship game class. Sets the size of the board.
    """
    def __init__(self, board_type):
        """
        Create board object. Set the size of the board
        """
        self.board_type = board_type

    def display_board(self, name):
        """
        Display the user's board
        """
        print(f"{name}'s board")
        for row in self.board_type:
            print(" ".join(row))
        print("\n")

    def input_board_size():
        global board_size
        global user_board
        global computer_board
        print("Board size minimum is 5x5 and maximum of 10x10")
        board_size = int(input("Please enter a size of the board:\n"))

        user_board = [["."] * board_size for i in range(board_size)]
        computer_board = [["."] * board_size for i in range(board_size)]

        return board_size


class Ship:
    """
    Ship class. Set the number of ships and
    the coordinates for each ship
    """
    def __init__(self, board_type):
        """
        Create ship object.
        """
        self.board_type = board_type

    def create_computer_ships(self):
        """
        Create ships with random co-ordinates for computer
        and store them in a list
        """
        ships_row = []
        ships_column = []
        global board_size

        for i in range(3):
            self.row = randrange(board_size)
            self.column = randrange(board_size)
            ships_row.append(self.row)
            ships_column.append(self.column)
        
        computer_coordinates = list(zip(ships_row, ships_column))
        # need to check for validation to make sure there no duplicates
        return computer_coordinates

    def create_user_ships(self):
        """
        Set the ship locations
        """
        coordinates = []
        global board_size

        for i in range(3):
            self.row = randrange(board_size)
            self.column = randrange(board_size)
            self.board_type[self.row][self.column] = "*"
            coordinates.append((self.row, self.column))
        
        user_coordinates.append(coordinates)
        return self.board_type

    def attack_computer(self, row, column):
        """
        For user to attack the computer and check if
        row and column hit a ship.
        Update the board accordingly "O" for hits "X"
        for misses
        """
        attack = (row, column)
        for i in computer_coordinates:
            # check if the attack co-ordinates is present in the list
            if attack in i:
                print("You hit a ship!")
                self.board_type[row][column] = "O"
            else:
                print("You missed!")
                self.board_type[row][column] = "X"

        return self.board_type

    def attack_user(self):
        """
        Computer generates an attack to user
        Update the board accordingly "O" for hits "X"
        for misses
        """
        row = randrange(board_size)
        column = randrange(board_size)
        attack = (row, column)
        for i in user_coordinates:
            # check if the attack co-ordinates is present in the list
            if attack in i:
                print("Computer hit your ship!")
                self.board_type[row][column] = "O"
                Ship.reduce_user_hp()
            else:
                print("Computer missed!")
                self.board_type[row][column] = "X"
        
        return self.board_type

    def input_row():
        """
        User input a row number on where he wants to attack.
        Validate the user input
        """
        max_lenght = board_size - 1
        while True:
            try:
                row = int(input("Please enter a row number:\n"))
            except ValueError:
                print("You must input an integer")
                continue

            if row < 0 or row > max_lenght:
                print(f"Please enter a row number between 0 and {max_lenght}")
                continue
            else:
                break
        
        return row

    def input_column():
        """
        User input a column number on where he wants to attack.
        Validate the user input
        """
        max_lenght = board_size - 1
        while True:
            try:
                column = int(input("Please enter a column number:\n"))
            except ValueError:
                print("You must input an integer")
                continue

            if column < 0 or column > max_lenght:
                print(f"Please enter a column number between 0 and {max_lenght}")
                continue
            else:
                break    

        return column

    def reduce_user_hp():
        """
        When computer hits an user ship, user's hitpoints decrease by 1
        """
        global user_hp
        user_hp -= 1

        return user_hp


def display_intro():
    """
    Print all the introduction message and the legend
    of the game. This will help user understand the game
    """
    game_description = ("This is a single player game (User vs Computer).\n"
                        "The aim of the game is to destroy oppenents ships.\n"
                        "The user and the computer will take turns on "
                        "attacking each other.\n"
                        "If a ship is hit, the user/computer "
                        "will lose 1 hit point.\n"
                        "If computer hit points reaches 0, then the user "
                        "have won, vice versa.\n"
                        "Please see game legend below and Enjoy the game!\n")

    print("Welcome to SHIP-WARS!\n")
    print(game_description)
    print("** '*' = user ship location **")
    print("** 'O' = attack hit a ship **")
    print("** 'X' = missed attack **\n")


def StartGame():
    """
    Store the logic of the game here
    """
    display_intro()

    # Board.input_board_size()
    user = Board(user_board)
    computer = Board(computer_board)
    computer_locations = Ship.create_computer_ships(computer)
    computer_coordinates.append(computer_locations)
    print(computer_coordinates)
    Ship.create_user_ships(user)
    print(user_coordinates)

    user.display_board("John")
    computer.display_board("Computer")

    while user_hp > 0:
        row = Ship.input_row()
        column = Ship.input_column()
        Ship.attack_computer(computer, row, column)
        computer.display_board("Computer")
        Ship.attack_user(user)
        user.display_board("John")
    
    if user_hp == 0:
        print("Computer won!")
    else:
        print("User won")


StartGame()
