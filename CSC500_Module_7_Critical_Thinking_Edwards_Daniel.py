# Dictionary of class information
class_information = {
        
    "room_number": {
        "CSC101": 3004,
        "CSC102": 4501,
        "CSC103": 6755,
        "NET110": 1244,
        "COM241": 1411
    },
    
    # Dictionary of class instructors
    "class_instructors": {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    },
    
    # Dictionary of class meeting times
    "meeting_times": {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m."
    }
}

# While loop to prompt user for class number
while True:
    class_number = input("Enter a class number or 'q' to quit: ")

    # If class number is in the dictionary, print the class information
    if class_number in class_information["room_number"] and class_number in class_information["class_instructors"] and class_number in class_information["meeting_times"]:
        room_number = class_information["room_number"][class_number]
        instructor = class_information["class_instructors"][class_number]
        meeting_time = class_information["meeting_times"][class_number]
        print(f"\n{class_number} is taught by Professor {instructor}, and meets at {meeting_time} in classroom number {room_number}.\n")
    elif class_number == "":
        print("No class number entered. Please try again.")
    elif class_number.lower() == 'q': # If user enters 'q', the program will quit
        print("\nYou have quit the program")
        break
    else:
        print(f"Information for class number {class_number} is not available.")


############################################################################################################
# Pseudocode

# Define Funciton class_information dictionary containing room numbers, instructors, and meeting times for different classes.

# While True:
#     User input to enter a class number or 'q' to quit.
#     Read user input.

#     If the input class number is present in all dictionaries inside class_information:
#         Retrieve room number, instructor, and meeting time corresponding to the entered class number.
#         Output the retrieved information about the class.
#     ElseIf the input is an empty string:
#         Output a message that no class number was entered and prompt the user again.
#     ElseIf the input is 'q':
#         Output a message for quitting the program.
#         Break Statement out of the loop which quits the program
#     Else:
#         Print a message information for the entered class number is not available.