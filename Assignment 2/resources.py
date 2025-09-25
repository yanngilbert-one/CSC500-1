#importing the regex and datetime modules
import re
import datetime

#food_calculations.py functions

#initialize a constant for the tip and sales tax percentages, ideally these constants would be stored in a seperate file to make it more scalable when working with a larger scale program
TIP = 0.18
SALES_TAX = 0.07

#function to validate user input for the price
def get_price_input(user_input_number):
    valid_input = False
    while not valid_input:
        try:
            number = float(input(user_input_number))
            if number >= 0:
                valid_input = True
            else: 
                print("Invalid input: Please enter a positive value.")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    return number

#function to calculate tip amount using the established constant
def calculate_tip_amount(food_price):
    return food_price * TIP

#function to calculate tax amount using the established constant
def calculate_tax_amount(food_price):
    return food_price * SALES_TAX

#function to calculate total price using our two other functions
def calculate_total_price(food_price):
    return food_price + calculate_tip_amount(food_price) + calculate_tax_amount(food_price)



# clock_calculation.py functions


#function to validate user input for current time
def get_time_input(user_time_input):
    valid_input = False
    #a regex is used to set a format for the values to be entered by the user, this is a cleaner way to do data validation when expecting very specific input
    regex = r"^([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$"
    while not valid_input:
        try:
            time_input = input(user_time_input)
            if not re.match(regex, time_input):
                print ("Invalid input. Hours must be between 0 and 23, minutes and seconds must be between 0 and 59.")
                #continue lets us loop this function until the user provides proper input
                continue
            else:
                valid_input = True

        except ValueError:
            print("Invalid input, please follow the provided format when entering the time.")
    return time_input

#function to validate user input for the alarm time
def get_alarm_input(user_alarm_input):
    valid_input = False
    #second regex different from the first to allow for a large amount of hours to be provided. With the other regex we could not provide more than 23 hours.
    regex = r"^(\d+):[0-5][0-9]:[0-5][0-9]$"
    while not valid_input:
        try:
            alarm_input = input(user_alarm_input)
            if not re.match(regex, alarm_input):
                print ("Invalid input. Hours must be positive or 0, minutes and seconds must be between 0 and 59.")
                continue
            else: valid_input = True

        except ValueError:
            print("Invalid input, please follow the provided format when enterering the alarm time.")
    return alarm_input

#function to turn the given string of time into seconds
def time_string_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))

    return hours * 3600 + minutes * 60 + seconds

#function to calculate total seconds using the current time and the amount of time the alarm will take
def calculate_alarm_ring_time(time, alarm_amount):

    total_seconds = time_string_to_seconds(time) + time_string_to_seconds(alarm_amount)
    result_time = str(datetime.timedelta(seconds=total_seconds))

    return result_time

