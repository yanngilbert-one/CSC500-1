import resources

#initialize a variable that will loop the program until the user does not enter 'yes' to the final question
next_calculation_input='yes'

#while loop that will repeat the program until the answer from the user to the final question is not 'yes'
while next_calculation_input=='yes':
    #initialize num1 and num2 using functions from the resources.py file
    num1 = resources.get_number_input('Please input your first number: ')
    num2 = resources.get_number_input('Please input your second number: ')
    #initialize operator using a function from the resources.py file
    operator = resources.get_operator_input()

    #prints the result of the operation
    print(resources.calculate(num1, num2, operator))

    #asks the user if they would like to perform another calculation, this determines whether the program will loop or exit
    next_calculation_input = input('Would you like to perform another calculation? (yes or no): ').lower()
