#initialize class
class Month:
    #array of the names of the months in a year, order matters
    MONTH_NAMES = [
        "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    ]
    #constructor
    def __init__(self):
        self.current_month_index = 0
    #iterator   
    def __iter__(self):
        return self
    #next iteration logic for iterating through the list of months
    def __next__(self):
        if self.current_month_index < len(self.MONTH_NAMES):
            month_name = self.MONTH_NAMES[self.current_month_index]
            self.current_month_index += 1
            return month_name
        else:
            raise StopIteration
