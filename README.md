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

- _Increase Turn_
    - There is a functionality to keep track of the turns.
    - After the user and the computer attack, the turn will be incremented by 1 and will be displayed for the user to see how many turns have passed and the current turn.
    - Each turn, the user and the computer will take turns attacking each other.

- _Reduce Hit Points_
    - User and the computer will have hit points(hp). 1 Ship = 1 Hit points. 
    - The hp for the user and computer will be displayed after the user inputted the number of ships and also every after turn.
    - User and computer hp will be reduce by 1 everytime the user/computer ship were hit. Hp for the user will then be updated to help user know how many hp he/she and the computer currently have.
    - When user hp is reduced to zero, the computer wins. If the computer hp is reduced to zero, then user wins. There could also be a possibility of draw if both user and computer hp is reduced to zero at the same turn.

- _User Attack_
    - The user will be asked to guess the coordinates of the computer ships by inputting the row number and column number.
    - If the user guessed is correct, it would then hit a computer ship and the computer board will display "O" on the coordinate the user has inputted. But if it is a miss, the computer board will then display an "X".
    - The max number of row and column that a user could input would be based on the inputted board size (minus 1 as the index starts at 0)
    - There is also a validation to make sure that the user does not input an invalid value (not an integer, number that is less than 0 or more than the maximum size of the board) for the row and column.
    - The user will then be notified that they have input an invalid value and will be asked to input a row/column number again.

![User Attack](/images/user_attack.png)

- _Computer Attack_
    - This functionality will let computer attack the user by generating a random row number and column number(coordinates).
    - If computer attack hits a user ship, the user board will be updated and the "*" in the board will be changed to "O" to let user know that the user has hit this ship.
    - If computer attack missed, the user board will be updated and will display an "X" into the location/coordinate of the computer attack.
    - There is also a validation to make sure that the randomly generated attack has correct values.

![Computer Attack](/images/computer_attack.png)

- _Validate Attack_
    - Validate attack functionality will help prevent the user and computer attack the same co-ordinate twice.
    - User will be notified and will be asked to attack(input a row number a column number) again, the he/she has inputted a coordinate that was already used on an attack before.
    - The computer will generate new random number for the row and column if the generated row and column number was already used in the previous attacks.

![Validate Attack](/images/validate_attack.png)

