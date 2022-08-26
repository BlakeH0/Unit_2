'''
In your notebook
Predict what the following inputs will result in
Once you have filled in the "prediction" column, check your answers in interactive mode and write the actual result.
    Input                                       Prediction                                      Result
1.  float('1')                                  1.0                                             1.0
2.  str(1 + '2')                                error                                           error
3.  str('2')                                    '2'                                             '2'
4.  int('abc')                                  error                                           error
5.  int(float('1.6'))                           error                                           error
6.  float(int(1.6))                             error                                           1.0
7.  str(float(1))                               '1.0'                                           1.0


In script mode
Create a program which will take in an input and print out that input divided by 2.
Alter one line of that program to return only whole numbers.

'''
# User Input
number_input_1 = input('Enter a number: ')

# Division/Display
print(int(number_input_1)/2)

# Whole Numbers Only

    #Input
number_input_2 = int(input('Enter a number: '))

    # Division Whole Number
whole_number = int(number_input_2/2)

    # Display WHole Number
print(whole_number)