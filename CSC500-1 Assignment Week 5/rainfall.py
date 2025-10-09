import resources
from month import Month

#get years input from user
number_of_years_input = resources.get_years()

#initialize variables for total months and rainfall to be added to every month
total_months = 0
total_rainfall = 0

#outer loop for year based on number of years provided
for year in range(1, number_of_years_input + 1):
    print(f"Year {year}: ")
    #create our month object containing the names of all the months
    months = Month()
    #nested loop to loop through the months for each year
    for month_name in months:
        #get user input for rainfall this month
        rainfall = resources.get_rainfall(month_name)

        #add months rainfall to total and month number to number of months to be used to get average later
        total_rainfall += rainfall
        total_months += 1
#get average rainfall using data collected during the for loop
average_rainfall_by_month = total_rainfall / total_months

#print results
print("---Results---")
print(f"Number of months: {total_months}")
print(f"Total rainfall: {total_rainfall:.2f} inches")
print(f"Average rainfall per month: {average_rainfall_by_month:.2f} inches")