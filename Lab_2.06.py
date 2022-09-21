'''
#################
Lab 2.06
#################
1. In your Notebook
-------------------
Predict what will be printed then type the program in your console to confirm
Example 1
    a = 0
    while a < 10:
        print(a)

prediction: 0
actual: infinite 0's

Example 2
    a = 0
    while a < 10:
        a = a + 1
        print(a)

prediction: 0 1 2 3 4 5 6 7 8 9 10
actual:  1 2 3 4 5 6 7 8 9 10

2. In your Notebook
-------------------
Create a set of test cases for the following sample code and predict the behavior
    a = input("Would you like to quit: ")
    while a != "y" and a != "n" :
        a = input("Would you like to quit: ")

test cases: 'y', 'n', 'q', 'cat'

3. Implement the Tic Tac Toe game using a while loop
----------------------------------------------------
Allow users to keep playing (max 9 times).

Use variables to decide whose turn it is, and greet them as Xs or Os.

User picks a location on the board according to the number:
        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9


Depending on the position user gave, update the corresponding position of the board to reflect that.

Print the updated board out.

You will not need to determine the winner at this point.
(Copy and paste your previous tic-tac-toe version and modify the code to implement the above)
'''


# Player Distinction
print("Welcome to Tic-Tac-Toe! Player 1 is X's and Player 2 is O's.")

# Board
restart = False

game = True
board_spaces = 9
if restart == True:
        board = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}" '\n')
print('---------''\n')
print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}"'\n')
print("---------"'\n')
print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}"'\n')


### GAME FUNCTIONALITY ###
playing = True
while playing:
    if board_spaces > 0:
        while game and board_spaces % 2 == 1:
            p_x_cell_selected = int(input("Player 1 where would you like to place your move? "))
            if p_x_cell_selected == 1 or p_x_cell_selected == 2 or p_x_cell_selected == 3:
                if type(board[0][p_x_cell_selected - 1]) ==  int: 
                    if p_x_cell_selected == 1:
                        board[0][0] = 'X'
                        board_spaces -= 1
                    elif p_x_cell_selected == 2:
                        board[0][1] = 'X'
                        board_spaces -= 1
                    elif p_x_cell_selected == 3:
                        board[0][2] = 'X'
                        board_spaces -= 1
            elif p_x_cell_selected == 4 or p_x_cell_selected == 5 or p_x_cell_selected == 6:
                if type(board[1][p_x_cell_selected - 4]) == int:
                    if p_x_cell_selected == 4:
                        board[1][0] = 'X'
                        board_spaces -= 1
                    elif p_x_cell_selected == 5:
                        board[1][1] = 'X'
                        board_spaces -= 1
                    elif p_x_cell_selected == 6:
                        board[1][2] = 'X'
                        board_spaces -= 1
            elif p_x_cell_selected == 7 or p_x_cell_selected == 8 or p_x_cell_selected == 9:
                if type(board[2][p_x_cell_selected - 7]) == int:
                    if p_x_cell_selected == 7:
                        board[2][0] = 'X'
                        board_spacesnothing -= 1
                    elif p_x_cell_selected == 8:
                        board[2][1] = 'X'
                        board_spaces -= 1
                    elif p_x_cell_selected == 9:
                        board[2][2] = 'X'
                        board_spaces -= 1
            else:
                print("That is not a valid number!")

        print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}" '\n')
        print('---------''\n')
        print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}"'\n')
        print("---------"'\n')
        print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}"'\n')
    else:
        print("The game is over!")
        playing = False

    if board_spaces > 0:
        while board_spaces > 0 and board_spaces % 2 == 0:
            p_o_cell_selected = int(input("Player 2, where would you like to place your move?"))
            if p_o_cell_selected == 1 or p_o_cell_selected == 2 or p_o_cell_selected == 3:
                if type(board[0][p_o_cell_selected - 1]) ==  int: 
                    if p_o_cell_selected == 1:
                        board[0][0] = 'O'
                        board_spaces -= 1
                    elif p_o_cell_selected == 2:
                        board[0][1] = 'O'
                        board_spaces -= 1
                    elif p_o_cell_selected == 3:
                        board[0][2] = 'O'
                        board_spaces -= 1
            elif p_o_cell_selected == 4 or p_o_cell_selected == 5 or p_o_cell_selected == 6:
                if type(board[1][p_o_cell_selected - 4]) ==  int: 
                    if p_o_cell_selected == 4:
                        board[1][0] = 'O'
                        board_spaces -= 1
                    elif p_o_cell_selected == 5:
                        board[1][1] = 'O'
                        board_spaces -= 1
                    elif p_o_cell_selected == 6:
                        board[1][2] = 'O'
                        board_spaces -= 1
            if p_o_cell_selected == 7 or p_o_cell_selected == 8 or p_o_cell_selected == 9:
                if type(board[2][p_o_cell_selected - 7]) == int:
                    if p_o_cell_selected == 7:
                        board[2][0] = 'O'
                        board_spaces -= 1
                    elif p_o_cell_selected == 8:
                        board[2][1] = 'O'
                        board_spaces -= 1
                    elif p_o_cell_selected == 9:
                        board[2][2] = 'O'
                        board_spaces -= 1
            else:
                print("That is not a valid number!")

        print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}" '\n')
        print('---------''\n')
        print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}"'\n')
        print("---------"'\n')
        print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}"'\n')
    else:
        print("The game is over!")
        again = input("Would you like to play again?")
        if again == 'yes':
            playing = True
        elif again == 'no':
            playing = False