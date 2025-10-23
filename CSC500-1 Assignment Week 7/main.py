import resources
#get data from json using function in resources
data = resources.load_course_data_json()
#if the data was found
if data: 
    #initialize the three dictionaries
    room_numbers, instructors, meeting_times = data
    #function to get the list of unique keys from all 3 dictionaries
    unique_courses = resources.list_available_courses(room_numbers, instructors, meeting_times)
    #set stop loop to false to start our loop on user input
    stop_loop = False
else:
    #if data was not found, print error message and prevent loop from starting
    print("Failed to load course data.")
    stop_loop = True
#loop on user input
while not stop_loop: 
    #ask user for a course number, capitalize for safety
    user_input = input("Enter a course number you wish to see information for: ").upper()
    #if the display_course_info function returns false, tell user the input was invalid and ask if they want to see a list of valid input
    if not resources.display_course_info(user_input, room_numbers, instructors, meeting_times):
        print(f"Course number provided '{user_input}' was not found in the provided data.")
        #input to ask if the user wants to see a list of valid input
        user_see_course_input = input("Would you like to see a list of available course data?(yes/no): ").lower()
        if user_see_course_input == "yes":
            print("List of available course data by course number:")
            #print each unique key for user
            for course in sorted(unique_courses):
                print(course)
    #input to ask user if they would like to search another course
    user_loop_input = input("Would you like to search another course(yes/no): ").lower()
    if user_loop_input != "yes":
        stop_loop = True
