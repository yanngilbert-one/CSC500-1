import resources
import datetime
from Classes.shopping_cart import ShoppingCart

#initialize item list array as well as validation for the loop handling if user would like to continue or stop inputing items
item_list = []
next_item_input = "yes"

#loop to build item list array
while next_item_input.lower() == "yes":
    #get user item data from user
    item = resources.get_user_item()
    #add item to list of items
    item_list.append(item)
    #ask user if continuing to input items
    next_item_input = input("Would you like to add another item? (yes/no): ")

#get customer name input
customer_name = input("Enter customer's name: ")
#using current date as date/could also just ask for date from user if needed
current_date = datetime.datetime.now()
#create shoppingcart object using customer name, the current time formatted and the list of items provided
cart = ShoppingCart(customer_name, current_date.strftime("%B %d, %Y"), item_list)
#menu handler for all required cases
resources.handle_menu(cart)