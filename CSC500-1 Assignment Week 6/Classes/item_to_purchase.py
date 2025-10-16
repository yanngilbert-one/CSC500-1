#initialize class
class ItemToPurchase:
    #constructor
    def __init__(self, item_name = "none", item_description = "none", item_price = 0, item_quantity = 0): 
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity
        
    #function to print item cost using all attributes
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")
        return total_cost
    