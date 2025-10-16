#import ItemToPurchase class
from Classes.item_to_purchase import ItemToPurchase
from Classes.shopping_cart import ShoppingCart

#function to get and validate all item data from user
def get_user_item():
    #input validation variable
    valid_input = False
    #get item name, no validation needed here. In a real scenario we would put a character limit of some sort here and security features like SQL injection protection
    item_name = input("Enter the item name: ")
    item_description = input("Enter the item description: ")

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
    return ItemToPurchase(item_name, item_description, item_price, item_quantity)

#function to print menu navigation instructions
def print_menu():
    print("MENU")
    print("a - Add an item to cart")
    print("r - Remove an item from cart")
    print("c - Change an item's quantity")
    print("i - Output all item descriptions")
    print("o - Output entire shopping cart")
    print("q - Quit application")

#function that handles all menu modules
def handle_menu(cart):
    #print the menu
    print_menu()
    #initialize choice variable
    menu_choice = ''
    #looping until user exits loop
    while menu_choice != 'q':
        #get user input for menu option
        menu_choice = input("Choose an option from the menu: ")
        #using a switch case instead of if elif, either works but I prefer switches personally for static options
        match menu_choice:
            #case q, exit loop
            case 'q':
                break
            #case a, get all item attributes from user and append item to item list
            case 'a':
                print("ADD ITEM TO CART")
                item = get_user_item()
                cart.add_item(item)
            #case r, get item name and remove item from item list
            case 'r':
                print("REMOVE ITEM FROM CART")
                item_name = input("Enter the name of item to remove: ")
                cart.remove_item(item_name)
            #case c, get item name and then quantity to be changed to, handle incorrect values
            case 'c':
                print("CHANGE ITEM QUANTITY")
                item_name = input("Enter the name of the item youd want to change the quantity of: ")
                item_exists = False
                for item in cart.cart_items:
                    if item_name == item.item_name:
                        item_exists = True
                        valid_input = False
                        while not valid_input:
                            try: 
                                item_new_quantity = int(input(f"Enter the new quantity for item {item_name}: "))
                                if item_new_quantity <= 0:
                                    print("Quantity cannot be negative or 0, if you wish to remove the item use 'r' in the menu.")
                                else:
                                    valid_input = True
                                    break
                            except ValueError:
                                print('Invalid value. Please enter a positive integer.')
                        #modifiy function provided new quantity
                        modify_item = ItemToPurchase(item_name = item_name, item_quantity=item_new_quantity)
                        cart.modify_item(modify_item)
                if not item_exists:
                    print(f"Item \"{item_name}\" did not exist in cart. Nothing was changed.")
            #case i, use print_description function
            case 'i':
                print("OUTPUT ITEMS DESCRIPTIONS")
                cart.print_descriptions()
            #case o, use print_total function
            case 'o':
                print("OUTPUT SHOPPING CART")
                cart.print_total()
            #handle if menu choice is not valid
            case _: 
                print("Invalid menu choice. Please choose a valid option from the menu.")


