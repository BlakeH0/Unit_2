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

game = True
board_spaces = 9

board = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]

print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}" )
print('---------')
print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
print("---------")
print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")


### GAME FUNCTIONALITY ###
while game and board_spaces % 2 == 1:
    p_x_cell_selected = int(input("Player 1 where would you like to place your move? "))    
    if p_x_cell_selected == 1:
        board[0][0] = 'X'
        board_spaces -= 1
        print(board_display)
    elif p_x_cell_selected == 2:
        board[0][1] = 'X'
        board_spaces -= 1
        print(board_display)
    elif p_x_cell_selected == 3:
        board[0][2] = 'X'
        board_spaces -= 1
        print(board_display)
    elif p_x_cell_selected == 4:
        board[1][0] = 'X'
        board_spaces -= 1
        print(board_display)
    elif p_x_cell_selected == 5:
        board[1][1] = 'X'
        board_spaces -= 1
        print(board_display)
    elif p_x_cell_selected == 6:
        board[1][2] = 'X'
        print(board_display)
    elif p_x_cell_selected == 7:
        board[2][0] = 'X'
        board_spaces -= 1
        print(board_display)
    elif p_x_cell_selected == 8:
        board[2][1] = 'X'
        board_spaces -= 1
        print(board_display)
    elif p_x_cell_selected == 9:
        board[2][2] = 'X'
        board_spaces -= 1
        print(board_display)
    else:
        print("That is not a valid number!")

while game == True and board_spaces % 2 == 0:
    p_o_cell_selected = int(input("Player 2, where would you like to place your move?"))
if p_o_cell_selected == 1:
    board[0][0] = 'O'
    board_spaces -= 1
    print(board_display)
elif p_o_cell_selected == 2:
    board[0][1] = 'O'
    board_spaces -= 1
    print(board_display)
elif p_o_cell_selected == 3:
    board[0][2] = 'O'
    board_spaces -= 1
    print(board_display)
elif p_o_cell_selected == 4:
    board[1][0] = 'O'
    board_spaces -= 1
    print(board_display)
elif p_o_cell_selected == 5:
    board[1][1] = 'O'
    board_spaces -= 1
    print(board_display)
elif p_o_cell_selected == 6:
    board[1][2] = 'O'
    board_spaces -= 1
    print(board_display)
elif p_o_cell_selected == 7:
    board[2][0] = 'O'
    board_spaces -= 1
    print(board_display)
elif p_o_cell_selected == 8:
    board[2][1] = 'O'
    board_spaces -= 1
    print(board_display)
elif p_o_cell_selected == 9:
    board[2][2] = 'O'
    board_spaces -= 1
    print(board_display)
else:
    print("That is not a valid number!")
