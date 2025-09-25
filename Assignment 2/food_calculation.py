import resources

#get and validate input from user for food_price
food_price = resources.get_price_input('What was the price of your food?: $')

#calculate the tip and tax amounts based on food_price
tip_amount = resources.calculate_tip_amount(food_price)
tax_amount = resources.calculate_tax_amount(food_price)
#calculate the total cost of the food
full_price = resources.calculate_total_price(food_price)

#display total food cost as well as the amounts for each tip percentage
print(f"Your total for your food including a 18% tip (${tip_amount:.2f}) and a 7% sales tax (${tax_amount:.2f}) comes out to ${full_price:.2f}")