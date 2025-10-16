from Classes.item_to_purchase import ItemToPurchase
#initalize class
class ShoppingCart:
    #constructor
    def __init__(self, customer_name="none", current_date="January 1, 2020", cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
    #function to add an item, requires provided item_to_purchase
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)
    #function to remove an item, requires provided item_name
    def remove_item(self, item_name):
        item_removed = False
        #iterate through items in cart and remove item using item name provided
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                print(f"Item \"{item_name}\" was removed from the cart.")
                item_removed = True
                break
        #if we dont set the flag to true for item removed, it means we never found a match to item existing in cart so print error
        if not item_removed:
            print(f"Item \"{item_name}\" was not found in cart. Nothing was removed.")
    #function to modify an item, requires item_to_purchase to be provided
    def modify_item(self, item_to_purchase):
        item_modified = False
        #iterate through cart items looking for a match with provided name
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                if item_to_purchase.item_description != "none":
                    item.item_description = item_to_purchase.item_description
                if item_to_purchase.item_price != 0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                item_modified = True
                break
        #if item_modified flag is not changed this means we never found a successful match, print error
        if not item_modified:
            print(f"Item \"{item_to_purchase.item_name}\" was not found in card. Nothing was modified.")
    #function to get number of items in cart
    def get_num_items_in_cart(self):
        total_items_in_cart = 0
        #loop through each cart item and add quantity of that item to total quantity
        for item in self.cart_items:
            total_items_in_cart += item.item_quantity
        return total_items_in_cart
    #function to get total cost of cart
    def get_cost_of_cart(self):
        total_cost_of_cart = 0
        #loop through cart and add price times quantity of each item to total
        for item in self.cart_items:
            total_cost_of_cart += item.item_price * item.item_quantity
        return total_cost_of_cart
    #function to print total items and cost of cart
    def print_total(self):
        total_cost_of_cart = self.get_cost_of_cart()
        if not self.cart_items:
            print("Shopping cart is empty.")
        else:
            print(f"{self.customer_name}'s Shopping Cart for {self.current_date}")
            print(f"Number of Items in Cart: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total Cost of Cart: ${total_cost_of_cart:.2f}")
    #function to print all items and their description in cart
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart for {self.current_date}")
        print("Item Descriptions:")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")