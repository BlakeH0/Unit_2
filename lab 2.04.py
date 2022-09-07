'''
###########################
Lab 2.04
###########################
1. In your notebook
For each example below, predict what will be printed. Run the program and write down the output in your notebook.

Example 1
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[0])
    print(a[3])

    prediction:   a d                                         
    actual: a d

Example 2
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 3])

    prediction: 2
    actual: c

Example 3
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 6])

    prediction: invalid index 
    actual: e

Example 4
    a = ['a', 'b', 'c', 'd', 'e']
    a[3] = 'haha'
    print(a)

    prediction: ['a', 'b', 'haha', 'd', 'e']
    actual:['a', 'b', 'c', 'haha', 'e']

2. Create this game again using lists and indexes
--------------------------------------------------
Declare 10 prizes (prize0, prize1, prize2 at the top of your file), but store them all in a list.

User picks a number.

Print prize associated with the door user picked.

# Prize Game
prizes = ["a chocolate bunny!" ,  "a brand new car of your choice!" , "a free vacation to Stockholm, Sweden!" , "$1,000,000!" , "a $10 coupon to Lowe's!" , "a pair of fingerless gloves..." , "a 2 week old puppy!" , "seven ostrich eggs and an incubator!" , "nothing...sorry!" , "one free meal from denny's?"]

choice = input("What prize would you like between 1-10? ")
if choice == '1':
    print(prizes[0])
elif choice == '2':
    print(prizes[1])
elif choice == '3':
    print(prizes[2])
elif choice == '4':
    print(prizes[3])
elif choice == '5':
    print(prizes[4])
elif choice == '6':
    print(prizes[5])
elif choice == '7':
    print(prizes[6])
elif choice == '8':
    print(prizes[7])
elif choice == '9':
    print(prizes[8])
elif choice == '10':
    print(prizes[9])
else:
    print("Invalid prize choice!") 

3. Create a quiz
--------------------------------------------------
Create a food quiz using lists and indexes.

List of 6 different foods.

Ask the user 8 vague questions to find out what their favorite food is using the list.

Update the score and print their top 2 favorite foods.

Hint: Use a search engine to find the largest number in a python list.

----------------------
​Starter code here​:
----------------------
food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','baggles']
score = [0,0,0,0,0,0]

print('Please answer each questions with "y" for "yes" and "n" for "no."')
user_input = input('Do you like food with holes? ')
if user_input == 'y':
  score[0] = score[0] + 1
  score[5] = score[5] + 1

##############################
Together in class:
##############################
Research nested lists and work through the following Examples:

Bonus Example 1
a = ['a', 'b', 'c', ['d', 'e']]
print(len(a))
Bonus Example 2
a = ['a', 'b', 'c', ['d', 'e']]
b = a[3]
print(b)
Bonus - In your Notebook
How would you access d from the list a?
'''

# Food Quiz



food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','baggles']
score = [0,0,0,0,0,0]

print('Please answer each questions with "y" for "yes" and "n" for "no."')
user_input = input('Do you like food with holes? ')
if user_input == 'y':
  score[0] = score[0] + 1 # Add 1 to donuts
  score[5] = score[5] + 1 # Add 1 to baggles
elif user_input == 'n':
    score[1] = score[1] + 1 # Add 1 to pancakes
    score[2] = score[2] + 1 # Add 1 to bacon
    score[3] = score[3] + 1 # Add 1 to waffles
    score[4] = score[4] + 1 # Add 1 to eggs
else:
    print("That is not a valid answer, please answer with 'y' for yes or 'n' for no!")


user_input = input('Do you like batter/dough made food? ')
if user_input == 'y':
    score[0] = score[0] + 1 # Add 1 to donuts
    score[1] = score[1] + 1 # Add 1 to pancakes
    score[3] = score[3] + 1 # Add 1 to waffles
    score[5] = score[5] + 1 # Add 1 to baggles

elif user_input == 'n':
    score[2] = score[2] + 1 # Add 1 to bacon
    score[4] = score[4] + 1 # Add 1 to eggs

else:
    print("That is not a valid answer, please answer with 'y' for yes or 'n' for no!")

user_input = input('Do you like salty food? ')
if user_input == 'n':
    score[0] = score[0] + 1 # Add 1 to donuts
    score[1] = score[1] + 1 # Add 1 to pancakes
    score[3] = score[3] + 1 # Add 1 to waffles
    score[5] = score[5] + 1 # Add 1 to baggles

elif user_input == 'y' :
    score[2] = score[2] + 1 # Add 1 to bacon
    score[4] = score[4] + 1 # Add 1 to eggs

else:
    print("That is not a valid answer, please answer with 'y' for yes or 'n' for no!")

    user_input = input('Do you like crunchy/crispy food? ')
if user_input == 'n':
    score[0] = score[0] + 1 # Add 1 to donuts
    score[1] = score[1] + 1 # Add 1 to pancakes
    score[3] = score[3] + 1  # Add 1 to waffles
    score[4] = score[4] + 1 # Add 1 to eggs
    score[5] = score[5] + 1 # Add 1 to baggles

elif user_input == 'y':
    score[2] = score[2] + 1 # Add 1 to bacon
else:
    print("That is not a valid answer, please answer with 'y' for yes or 'n' for no!")

user_input = input('Do you like inherently sugary foods? ')
if user_input == 'y':
    score[0] = score[0] + 1 # Add 1 to donuts

elif user_input == 'n':
    score[3] = score[3] + 1 # Add 1 to waffles
    score[4] = score[4] + 1 # Add 1 to eggs
    score[5] = score[5] + 1 # Add 1 to baggles

else:
    print("That is not a valid answer, please answer with 'y' for yes or 'n' for no!")

user_input = input('Do you like food with a sugary glaze? ')
if user_input == 'y':
    score[0] = score[0] + 1 # Add 1 to donuts
    score[1] = score[1] + 1 # Add 1 to pancakes
    score[3] = score[3] + 1 # Add 1 to waffles

elif user_input == 'n':
    score[5] = score[5] + 1 # Add 1 to baggles
    score[2] = score[2] + 1 # Add 1 to bacon
    score[4] = score[4] + 1 # Add 1 to eggs

else:
    print("That is not a valid answer, please answer with 'y' for yes or 'n' for no!")

user_input = input('Do you like food that you tend to cut in half? ')
if user_input == 'y':
    score[5] = score[5] + 1 # Add 1 to baggles
elif user_input == 'n':
    score[0] = score[0] + 1 # Add 1 to donuts
    score[1] = score[1] + 1 # Add 1 to pancakes
    score[2] = score[2] + 1 # Add 1 to bacon
    score[4] = score[4] + 1 # Add 1 to eggs
    score[3] = score[3] + 1 # Add 1 to waffles

else:
    print("That is not a valid answer, please answer with 'y' for yes or 'n' for no!")


print(f"Your favorite food is  {food[score.index(max(score))]}")