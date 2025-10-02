import resources

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

#print total cost of cart
print("\n--- Items in your list: ---")
total_cost = sum(item.print_item_cost() for item in item_list)
print(f"\nTotal cost of all ({len(item_list)}) items in cart: ${total_cost:.2f}")