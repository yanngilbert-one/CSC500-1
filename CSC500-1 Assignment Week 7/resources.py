import json
#function to load the course info stored in json data
def load_course_data_json():
    #json data path
    file_path = "src/course_info.json"
    #keys to be searched in the json
    keys = ["Room Number", "Instructor", "Meeting Time"]
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        #error handling
        if not isinstance(data, dict):
            print(f"Error: JSON file does not contain a dictionary at the top level.")
            return None
        if not all(key in data for key in keys):
            print(f"Error: JSON file does not contain the expected key data. Please ensure the following keys exist: {keys}")
            return None
        
        #creating our three dictionaries
        room_numbers = data["Room Number"]
        instructors = data["Instructor"]
        meeting_times = data["Meeting Time"]

        return room_numbers, instructors, meeting_times
    #error handling
    except FileNotFoundError:
        print(f"Error: JSON file does not exist at: {file_path}")

    except json.JSONDecodeError:
        print(f"Error: JSON file formatting is not viable and could not be decoded. Please check your JSON file at path: {file_path}")

#function to display course info if user input is viable
def display_course_info(course_number, room_numbers, instructors, meeting_times):
    #check if user input is valid key existing in all 3 dictionaries
    if course_number in room_numbers and course_number in instructors and course_number in meeting_times:
            print(f"Selected Course: {course_number}")
            print(f"  Room Number: {room_numbers[course_number]}")
            print(f"  Instructor: {instructors[course_number]}")
            print(f"  Meeting Time: {meeting_times[course_number]}")
            return True
    return False

#function to display all unique keys existing in all dictionaries
def list_available_courses(room_numbers, instructors, meeting_times):
    unique_course_number = set()
    unique_course_number.update(room_numbers.keys())
    unique_course_number.update(instructors.keys())
    unique_course_number.update(meeting_times.keys())
    return unique_course_number