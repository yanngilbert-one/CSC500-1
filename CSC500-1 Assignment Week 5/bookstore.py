import resources

#get and validate user input for books purchased
number_of_books_purchased = resources.get_books_purchased()
#calculate points earned based on books purchased
points_earned = resources.get_points_earned(number_of_books_purchased)
#print results
print(f"The amount of points you have earned by buying {number_of_books_purchased} books this month is: {points_earned} points.)")