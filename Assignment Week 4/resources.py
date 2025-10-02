#import ItemToPurchase class
from item_to_purchase import ItemToPurchase

#function to get and validate all item data from user
def get_user_item():
    #input validation variable
    valid_input = False
    #get item name, no validation needed here. In a real scenario we would put a character limit of some sort here and security features like SQL injection protection
    item_name = input("Enter the item name: ")

    #loop until data input is valid
    while not valid_input:
        try:
            #converting input to float
            item_price = float(input("Enter the item price: "))
            #if item price is less than 0, it must be negative and therefor not acceptable input
            if item_price < 0:
                print("Price cannot be negative, please enter a positive value for the price.")
            else:
                #validate input and exit loop
                valid_input = True
                break
        #if value conversion to float is not valid, throw error and display error message
        except ValueError:
            print("Invalid value. Please enter a positive numerical value.")

    #input validation variable
    valid_input = False
    #loop until data input is valid
    while not valid_input:
        try: 
            #converting input to int
            item_quantity = int(input("Enter the item quantity: "))
            #if item quantity is less than 0, it must be negative and therefor not acceptable input
            if item_quantity < 0:
                print("Quantity cannot be negative, please enter a positive value for the quantity.")
            else:
                #validate input and exit loop
                valid_input = True
                break
        #if value conversion to int is not valid, throw error and display error message
        except ValueError:
            print("Invalid value. Please enter a positive integer without any decimals, quantity cannot be a decimal value, you cannot buy a third of an item!")
    #return item with its attributes
    return ItemToPurchase(item_name, item_price, item_quantity)