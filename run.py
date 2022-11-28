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

    def reduce_user_hp():
        global user_hp
        user_hp -= 1

        return user_hp


def StartGame():
    """
    Store the logic of the game here
    """
    user = Board(user_board)
    computer = Board(computer_board)

    computer_locations = Ship.create_computer_ships(computer)
    computer_coordinates.append(computer_locations)
    print(computer_coordinates)
    Ship.create_user_ships(user)
    print(user_coordinates)

    user.display_board("John")
    computer.display_board("Computer")

    # Ship.attack_computer(computer, 3, 1)
    # computer.display_board("Computer")
    # Ship.attack_user(user)
    # user.display_board("John")
    while user_hp > 0:
        Ship.attack_computer(computer, 3, 1)
        computer.display_board("Computer")
        Ship.attack_user(user)
        user.display_board("John")


StartGame()
