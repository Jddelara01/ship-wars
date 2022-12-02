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

![Input User Name](/images/input_name.png)

- _Input Board Size_
    - This functionality will ask user to input the board size he/she prefers.
    - The board has a minimum size of 5 and maximum size of 10
    - This also has a validation, when user inputs an incorrect value (not an integer, number that is less than or more than the minimum and maximum size), the user will then be notified that they have input an invalid value and will be asked to input the board size again.

![Input Board Size](/images/input_board_size.png)
