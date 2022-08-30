'''
##############################
User Input Challenge
##############################

Create a program that asks the user to enter their name and their age. Print out a message 
addressed to them that tells them the year that they will turn 100 years old.

Add on to the previous program by asking the user for another number and printing out that 
many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n" is the same as pressing the ENTER button)
'''

# User Name & Age
user_age = int(input("What is your age? "))
user_name = input("What is your name? ")

# Display 100th Birthyear
print((100 - user_age) + 2022)

# Display Number of Messages
number = input("Enter another number: ")
print((100 - user_age) + 2022)