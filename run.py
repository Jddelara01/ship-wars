""" Battleship game - Single Player """
# pylint: disable-all

from random import randrange

# Global variable for board size
board_size = 0
# Global variable for computer ships coordinates
computer_coordinates = []
# Global variable for user ships coordinates
user_coordinates = []
# Global variable for game board
user_board = [["."] * board_size for i in range(board_size)]
computer_board = [["."] * board_size for i in range(board_size)]
# Global variable to store user and computer attacks
user_attacks = []
computer_attacks = []
# Global variable to store hit points of user
user_hp = 0
# Global variable to store hit points of computer
computer_hp = 0
# Global variable for count the turns
turns = 1


class Board:
    """
    Battleship game class. Sets the size of the board.
    """
    def __init__(self, board_type):
        """
        Create board object. Set the size of the board
        """
        self.board_type = board_type

    def input_user_name():
        """
        User input preferred name.
        Maximum length of name is 20 chars
        """
        while True:
            username = input("Please enter your name:\n")
            if len(username) > 20:
                print("Username invalid! (Maximum length = 20)")
            elif username == "":
                print("You did not input a name")
            else:
                break
        
        return username

    def display_board(self, name):
        """
        Display the user's board
        """
        print(f"{name}'s board")
        for row in self.board_type:
            print(" ".join(row))
        print("\n")

    def input_board_size():
        """
        User input the size of the board and validate input
        Set the global variables accordingly
        """
        global board_size
        global user_board
        global computer_board

        print("Board size minimum is 5(5x5) and maximum of 10(10x10)")

        while True:
            try:
                board_size = int(input("Please enter a size of the board:\n"))
            except ValueError:
                print("You must input an integer")
                continue

            if board_size < 5 or board_size > 10:
                print("You can only enter a size between 5 and 10")
                continue
            else:
                break

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
        Validate to make sure no duplicate coordinates
        """
        coordinates = []
        global board_size
        global computer_hp

        while len(coordinates) < computer_hp:
            self.row = randrange(board_size)
            self.column = randrange(board_size)
            if (self.row, self.column) in coordinates:
                pass
            else:
                coordinates.append((self.row, self.column))
        
        computer_coordinates.append(coordinates)

    def create_user_ships(self):
        """
        Create ships with random co-ordinates for user
        and store them in a list
        Validate to make sure no duplicate coordinates
        """
        coordinates = []
        global board_size
        global user_hp

        while len(coordinates) < user_hp:
            self.row = randrange(board_size)
            self.column = randrange(board_size)
            if (self.row, self.column) in coordinates:
                pass
            else:
                self.board_type[self.row][self.column] = "*"
                coordinates.append((self.row, self.column))
        
        user_coordinates.append(coordinates)
        return self.board_type

    def input_number_of_ships():
        """
        User input number of ships for each player for this game
        Minimum number of ships is 3 and maximum is 10
        1 ship = 1 hp
        """
        global user_hp
        global computer_hp

        while True:
            try:
                ships_amount = int(input("Please enter number of ships " 
                                         "for each player for this game:\n"
                                         "(minimum of 3 and maximum of 10)\n"))
            except ValueError:
                print("You must input an integer")
                continue

            if ships_amount < 3 or ships_amount > 10:
                print("Please enter a number between 3 and 10")
                continue
            else:
                break

        user_hp = ships_amount
        computer_hp = ships_amount

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
                Ship.reduce_computer_hp()
                print(f"Computer hp: {computer_hp}")
            else:
                print("You missed!")
                print(f"Computer hp: {computer_hp}")
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
        if Ship.validate_computer_attack(row, column):
            Ship.attack_user(self)
        else: 
            for i in user_coordinates:
                # check if the attack co-ordinates is present in the list
                if attack in i:
                    print("Computer hit your ship!")
                    self.board_type[row][column] = "O"
                    Ship.reduce_user_hp()
                    print(f"User hp: {user_hp}")
                else:
                    print("Computer missed!")
                    print(f"User hp: {user_hp}")
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
                print(f"Please enter a number between 0 and {max_lenght}")
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
                print(f"Please enter a number between 0 and {max_lenght}")
                continue
            else:
                break    

        return column

    def validate_user_attack(attack_row, attack_column):
        """
        Check if the user input row and column is already used before
        This will help avoid user inputting the same co-ordinates
        """
        global user_attacks
        value = (attack_row, attack_column)

        if value in user_attacks:
            print("Coordinates already used.")
            return True
        else:
            user_attacks.append(value)
            return False

    def validate_computer_attack(attack_row, attack_column):
        """
        Check if the computer random row and column is already used before
        This will help avoid computer inputting the same co-ordinates
        """
        global computer_attacks
        value = (attack_row, attack_column)

        if value in computer_attacks:
            return True
        else:
            computer_attacks.append(value)
            return False

    def reduce_user_hp():
        """
        When computer hits an user ship, user's hitpoints decrease by 1
        """
        global user_hp

        user_hp -= 1
    
    def reduce_computer_hp():
        """
        When user hits a computer ship, comptuer's hitpoints decrease by 1
        """
        global computer_hp

        computer_hp -= 1

    def add_turn():
        global turns

        print(f"Turn: {turns}")
        turns += 1


def display_intro():
    """
    Print all the introduction message and the legend
    of the game. This will help user understand the game
    """
    game_description = ("This is a single player game (User vs Computer).\n"
                        "The aim of the game is to destroy oppenents ships.\n"
                        "The user and the computer will take turns on "
                        "attacking each other.\n" 
                        "User will have to input the co-ordinates (n, n) of "
                        "where he/she thinks the computer ships are located.\n" 
                        "To input the co-ordinates user has to input the row "
                        "number and column number.\n"
                        "If a ship is hit, the user/computer "
                        "will lose 1 hit point.\n"
                        "If computer hit points reaches 0, then the user have "
                        "won, vice versa but if both hit points reaches 0,"
                        "then it is a draw\n"
                        "Please see game legend below and Enjoy the game!\n")

    print("Welcome to SHIP-WARS!\n")
    print(game_description)
    print("** '*' = user ship location **")
    print("** 'O' = attack hit a ship **")
    print("** 'X' = missed attack **\n")
    print("Board format is row: 0 and column: 0 would be the very top left\n")


def print_attack_instructions(board_size):
    board_size -= 1
    print(f"Enter a number from 0 - {board_size}\n"
          "Where 0 is the very top left.\n")


def StartGame():
    """
    Store the logic of the game here
    """
    display_intro()

    player_name = Board.input_user_name()
    Board.input_board_size()
    user = Board(user_board)
    computer = Board(computer_board)
    Ship.input_number_of_ships()
    print(f"User hp: {user_hp}")
    Ship.create_computer_ships(computer)
    print(f"Computer hp: {computer_hp}\n")
    Ship.create_user_ships(user)

    user.display_board(player_name)
    computer.display_board("Computer")
    Ship.add_turn()

    while user_hp > 0 and computer_hp > 0:
        print_attack_instructions(board_size)
        row = Ship.input_row()
        column = Ship.input_column()
        if Ship.validate_user_attack(row, column):
            pass
        else:
            Ship.attack_computer(computer, row, column)
            computer.display_board("Computer")
            Ship.attack_user(user)
            user.display_board(player_name)
            Ship.add_turn()

    if user_hp == 0 and computer_hp == 0:
        print("It is a DRAW!")
    elif user_hp == 0:
        print("Game Over, you lost!")
    elif computer_hp == 0:
        print("Congratualation, you won!")
    else:
        print("Something went wrong!")
   

StartGame()
