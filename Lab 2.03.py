'''
##########################################
Lab 2.03 - Game Show
##########################################
In your Notebook
Follow the flow of execution in the following programs and predict what will happen for each
one
---------------------------------------
Example 1
---------------------------------------
a = input("What... is your quest")
b = "to seek the holy grail"
if a != b:
    print("Go On. Off you go")
else:
    b = input("What...is the air-speed velocity of an unladen swallow?")
    if b == "What do you mean? An African or European swallow?":
        print("I don't know that...AHHH [Bridgekeeper was thrown over bridge]")
    else:
        print("[you were thrown over bridge]")

Prediction: Go On. Off you go
Actual: Go On. Off you go

---------------------------------------
Example 2
---------------------------------------
user_input = input("What is your favorite color")
if user_input == 'blue':
    print("Blueskadoo")
elif user_input == "red":
    print("Roses are red!")
elif user_input == "yellow":
    print("Mellow Yellow")
elif user_input == "green":
    print("Green Machine")
elif user_input == "orange":
    print("Orange you glad I didn't say banana.")
elif user_input == "black":
    print("I see a red door and I want it painted black")
elif user_input == "purple":
    print("And we'll never be royalllssss")
elif user_input == "pink":
    print("Pinky- and the Brain")
else:
    print("I don't recognize that color. Is it even...??")

Prediction: And we'll never be royalllssss
Actual: And we'll never be royalllssss

---------------------------------------
In your Notebook
---------------------------------------
Translate this Snap! program into a Python program
***Refer to the image provided on Moodle located below the Lab 2.03 link***
Write program below:
# Rewritten Snap! Code


# Variables
x = int(input("What is x? "))
y = int(input("What is y? "))
z = int(input("What is z? "))
p = int(x + y + z)

# Type of Triangle
if x + y > z and y + z > x and z + x > y:
    print(f"The perimeter of your triangle is {p}")
    if x**2 + y**2 == z**2:
        print("This is a right triangle! ")
    if y**2 + z**2 == x**2:
        print("This is a right triangle! ")
    elif z**2 + x**2 == y**2:
        print("This is a right triangle! ")
    elif x == y == z:
        print("This is an equilateral triangle! ")
    elif z == x or x == y or y == z:
        print("This is an isoceles triangle!")
    else: print("This is a scalene triangle!")
else: print("This is not a valid triangle!")


---------------------------------------
Create a game show program
---------------------------------------
Declare 10 prizes (prize1, prize2, prize 3 at the top of your file)
User picks a number
The prize corresponding with that door is printed for the user.
Write code below the multiline comment
'''
prize1 = "a chocolate bunny!"
prize2 = "a brand new car of your choice!"
prize3 = "a free vacation to Stockholm, Sweden!"
prize4 = "$1,000,000!"
prize5 = "a $10 coupon to Lowe's!"
prize6 = "a pair of fingerless gloves..."
prize7 = "a 2 week old puppy!"
prize8 =  "seven ostrich eggs and an incubator!"
prize9 = "nothing...sorry!"
prize10 = "one free meal from denny's?"

prize_choice = input("Pick a number from 1-10 for a prize!")

if prize_choice == '1':
    print(f"You received {prize1}")
elif prize_choice == '2':
    print(f"You received {prize2}")
elif prize_choice == '3':
    print(f"You received {prize3}")
elif prize_choice == '4':
    print(f"You received {prize4}")
elif prize_choice == '5':
    print(f"You received {prize5}")
elif prize_choice == '6':
    print(f"You received {prize6}")
elif prize_choice == '7':
    print(f"You received {prize7}")
elif prize_choice == '8':
    print(f"You received {prize8}")
elif prize_choice == '9':
    print(f"You received {prize9}")
elif prize_choice == '10':
    print(f"You received {prize10}")
else:
        print("That is not a valid number!")

