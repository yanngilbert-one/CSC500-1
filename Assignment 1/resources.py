import math_operations

#function used to gather user input for a numerical values for num1 and num2
def get_number_input(user_input_number):
    #initialize a condition to be met for the loop to exit. If the user does not input a float viable input, the function will loop until they do
    valid_input = False
    while not valid_input:
        try:
            #user inputs their numeral value and it is converted to a float
            number = float(input(user_input_number))
            #if the conversion of the user input to a float is successful, we change our variable to True to exit the loop and return our result
            valid_input = True
        except ValueError:
            print("Invalid input. Please only enter numerical values.")
    return number

#function used to gather user input for an operator value
def get_operator_input():
    #initialize a condition to be met for the loop to exit. If the user does not input one of the proposed operators, the function will loop until they do
    valid_operator = False
    while not valid_operator:
        #user inputs their operator value and if the operator is one of the accepted values, exit the loop and return the operator. If it is not valid, loop and ask for a valid value
        operator = input("Please input operation method between one of the following: '+', '-', '*', '/': ")
        if operator in ('+', '-', '*', '/'):
            valid_operator = True
        else: 
            print('Invalid operator.')

    return operator

#function used to perform the calculations, the operations.py file is providing num1, num2, and the operator from the user
def calculate(num1, num2, operator):
    #using a switch case method to handle calculations based on operator
    match operator:
        case '+':
            return math_operations.add(num1, num2)
        case '-':
            return math_operations.substract(num1, num2)
        case '*':
            return math_operations.multiply(num1, num2)
        case '/':
            return math_operations.divide(num1, num2)
