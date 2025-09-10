#Functions file where we will define our math functions for addition, subtraction, multiplication and division.

#Addition
def add(num1, num2):
    return num1 + num2
#Substraction
def substract(num1, num2):
    return num1 - num2
#Multiplication
def multiply(num1, num2):
    return num1 * num2
#Division with a check for the second number to not be zero.
def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero."
    return num1/num2