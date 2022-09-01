'''
##################################
Lab 2.02 Booleans & Expressions
##################################
In your Notebook
Predict if each of the following examples will produce a True or False output. Check your answers in interactive mode.
                 
Example 1
    >>> a = 100
    >>> b = "science"
    >>> a > 75 and b == "science"       Prediction: True                    Actual: True
Example 2
    >>> a = 100
    >>> b = "science"
    >>> a > 75 and b != "science"       Prediction: False                    Actual: False
Example 3
    >>> a = 100
    >>> b = "science"
    >>> a > 75 or b != "science"        Prediction: True                     Actual: True
Example 4
    >>> a = 100
    >>> b = "science"
    >>> c = True
    >>> not c and a > 75 and b == "science"     Prediction: False                 Actual: False

In your Console

Complete the following coding challenge
Create a "Can I be President?" program, which determines if the user meets the minimum requirements for becoming the President of the United States. 
Have the user input the information needed.

The minimum requirements to be president of the United States are:

1. Older than 35

2. Resident of US for 14 Years

3. Natural born citizen

Print True if the person could be president and False if they can't be president.

Create a "I can't be President?" program. Print True if the user cannot be President and False if they can be President.

Create a "Can I ride the roller coaster?" program. A roller coaster has the rule that a rider has to be over the height of 50 inches. Because of a legal 
loophole, if you are over the age of 18 you can ride regardless of your height. If you are allowed to ride, the coaster costs 4 quarters 
(although the operator accepts tips so more money is appreciated).

Also, the theme park sells frequent rider passes: with a frequent rider pass the roller coaster costs only 2 quarters. 
Ask the user how tall they are in inches, their age, how many quarters they have, and if they have a frequent rider pass. 
Print True if the person can ride and False if they can't.


Are the following expressions equivalent? Research DeMorgan's Laws and write why you think they are the same or why they are not the same
not(x or y) == not x and not y

not(x and y) == not x or not y
'''
# Variables
'''
president_age = int(35)
residency_in_US = int(14)
nat_born_cit = 'yes'

# User Input
user_age = int(input("What is your current age? "))
user_residency = int(input("How long have you been a resident of the US? "))
user_citizenship = input("Are you a natural born citizen of the US? ")

# Can I Be President?
print(user_age >= president_age and user_residency >= residency_in_US and user_citizenship == nat_born_cit)

# I Can't Be President?


president_age = int(35)
residency_in_US = int(14)
nat_born_cit = 'yes'

# User Input
user_age = int(input("What is your current age? "))
user_residency = int(input("How long have you been a resident of the US? "))
user_citizenship = input("Are you a natural born citizen of the US? ")

# I Can't Be President?
print(user_age < president_age and user_residency < residency_in_US and user_citizenship != nat_born_cit)

# Can I Ride the Roller Coaster
age_req = int(18)
height_req = int(50)

# User Input
rider_height = int(input("What is your height in inches? "))
rider_age = int(input("What is your age? "))

# Can I Ride the Roller Coaster?
print(rider_age >= age_req or rider_height >= height_req)
'''
# Can I Ride the Roller Coaster (Frequent Rider)

# Can I Ride the Roller Coaster
age_req = int(18)
height_req = int(50)
amt_quarters = int(4)
amt_quarters_frequent = int(2)
frequent_rider = "yes"

# User Input
rider_height = int(input("What is your height in inches? "))
rider_age = int(input("What is your age? "))
rider_quarters = int(input("How many quarters do you have? "))
rider_frequent_pass = input("Do you have a frequent rider pass? ")

# Logic Variables
can_pay = rider_quarters >= amt_quarters or (rider_quarters >= amt_quarters_frequent and frequent_rider == frequent_rider)
tall_enough = rider_height = height_req 
old_enough = rider_age = age_req

# Can I Ride the Roller Coaster? (Frequent Rider)
print((can_pay and tall_enough) or (can_pay and old_enough))