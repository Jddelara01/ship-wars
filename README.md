# Ship-Wars

Ship-Wards is a Python terminal game, which was developed using gitpod and has been deployed in Heroku.

Users will be going against the computer. For the user to win, he/she has to destroy all computer ships by guessing the correct co-ordinates. Each ships is has 1 co-ordinates(row, column) and each takes 1 slot in the game board.

![Responsive Mockup]()

----

## Instructions

This is a single player game (User vs Computer). The aim of the game is to destroy oppenents ships. The user and the computer will take turns on attacking each other. User will have to input the co-ordinates (n, n) of where he/she thinks the computer ships are located. To input the co-ordinates user has to input the row number and column number. If a ship is hit, the user/computer will lose 1 hit point. If computer hit points reaches 0, then the user have won and vice versa but if both hit points reaches 0, then it is a draw.

Game Legend:
'*' = user ship location
'O' = attack hit a ship
'X' = missed attack

For more information about the game, please check [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))

## Features

In this section, I will be going through the different functionalities of the game and I will provide descriptions for each functionalities and what the functionality do. 

### Current Features

- _Input User Name_
    - The first thing the game will ask user is to input his/her preffered name.
    - This name will then be used to let user know which is his/her board.
    - The name has a maximum limit of 20 characters. If user input a name with more the 20 characters, he/she will be notified to input another name.

![Input User Name](/images/input_name.png)

- _Input Board Size_
    - This functionality will ask user to input the board size he/she prefers.
    - The board has a minimum size of 5 and maximum size of 10
    - This also has a validation, when user inputs an incorrect value (not an integer, number that is less than or more than the minimum and maximum size), the user will then be notified that they have input an invalid value and will be asked to input the board size again.

![Input Board Size](/images/input_board_size.png)

- _Input Number of Ships_
    - User can input the number of ships the user and the computer could each have.
    - Minimum number of ships that can be inputted is 3 and maximum of 10.
    - If user input an incorrect value (not an integer, number that is less than or more than the minimum and maximum size), the user will then be notified that they have input an invalid value and will be asked to input a number of ships again.

![Input Number of Ships](/images/input_num_ships.png)

- _Create Ships_
    - Based on the inputted number of ships, this functionality will create randomly generated (coordinates per ship) ships for the user and the computer.
    - There is also a validation in place for this functionality to make sure that there are now duplicated co-ordinates.

- _Display Board_
    - After user input his/her name, board size and number of ships, this functionality will then display the user board and the computer board.
    - User board will have the name of the user at the top of the board and the randomly generated ships will then be display in the user board as "*".
    - Computer board will have the computer board at the top of the board, however the randomly generated ships for the computer won't be displayed in the computer board. This makes sure that the user would not know where the computer ships are.
    - The size of the board (the row and column) is based on the inputted number by the user for the board size.

![Display Board](/images/display_board.png)