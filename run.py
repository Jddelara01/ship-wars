""" Battleship game - Single Player """
# pylint: disable-all

from random import randrange

# Global variable for board size
board_size = 5
# Global variable for computer ships coordinates
computer_coordinates = []
# Global variable for user ships coordinates
user_coordinates = []
# Glabal variable for game board
user_board = [["."] * board_size for i in range(board_size)]
computer_board = [["."] * board_size for i in range(board_size)]


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
        computer_ships_row = []
        computer_ships_column = []
        for i in range(3):
            self.row = randrange(board_size)
            self.column = randrange(board_size)
            computer_ships_row.append(self.row)
            computer_ships_column.append(self.column)
        
        computer_coordinates = list(zip(computer_ships_row, computer_ships_column))
        return computer_coordinates

    
    def create_user_ships(self):
        """
        Set the ship locations
        """
        for i in range(3):
            self.row = randrange(board_size)
            self.column = randrange(board_size)
            self.board_type[self.row][self.column] = "*"   

        return self.board_type   


user = Board(user_board)
computer = Board(computer_board)

computer_locations = Ship.create_computer_ships(computer)
print(computer_locations)
user_locations = Ship.create_user_ships(user)

user.display_board("John")
computer.display_board("Computer")
