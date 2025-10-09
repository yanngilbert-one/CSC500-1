##Part 1 functions

#function to get and validate year input
def get_years():
    #input validation variable
    valid_input = False
    #loop until data input is valid
    while not valid_input:
        try:
            #convert input to int
            amount_of_years = int(input("Enter amount of years to aggregate rain data: "))
            if amount_of_years < 1:
                print("Amount of years cannot be 0 or negative, please enter a positive integer.")
            else:
                valid_input = True
        #if value conversion to int is not valid, throw error and display error message
        except ValueError:
            print("Invalid value, please enter a positive integer.")
    #return data collected from user
    return amount_of_years

#function to get and validate data for monthly rainfall
def get_rainfall(month_name):
    #input validation variable
    valid_input = False
    #loop until data input is valid
    while not valid_input:
        try:
            #conver input to float
            rainfall = float(input(f"Enter rainfall in inches for {month_name}: "))
            #validate that rainfall is 0 or higher as we cannot have negative rainfall
            if rainfall >= 0:
                valid_input = True
            else: 
                print("Rainfall cannot be negative, please input a positive integer")
        #if value conversion to float is not valid, throw error and display error message
        except ValueError:
            print("Invalid value, please enter a positive integer.")
    #return data collected from user
    return rainfall

##Part 2 functions

#function to get and validate user input for books purchased
def get_books_purchased():
    #input validation variable
    valid_input = False
    #loop until data input is valid
    while not valid_input:
        try:
            #convert input to int
            amount_of_books = int(input("Enter the amount of books purchased this month: "))
            if amount_of_books < 0:
                print("Amount of books purchased cannot be negative, please enter a positive integer.")
            else:
                valid_input = True
        #if value conversion to int is not valid, throw error and display error message
        except ValueError:
            print("Invalid value, please enter a positive integer.")
    #return data collected from user
    return amount_of_books

#function to calculate points earned using provided books purchased
def get_points_earned(books_purchased):
    #using switch statement to calculate points
    match books_purchased:
        case 0 | 1:
            points = 0
        case 2 | 3:
            points = 5
        case 4 | 5:
            points = 15
        case 6 | 7:
            points = 30
        case _: 
            if books_purchased >= 8:
                points = 60
    return points
    