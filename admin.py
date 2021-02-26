# Name: Ryan White 
# Student Number: 10554949  

# This file is provided to you as a starting point for the "admin.py" program of Assignment 2
# of Programming Principles in Semester 1, 2021.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the json module to allow us to read and write data in JSON format.
import json


# This function repeatedly prompts for input until an integer is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
def input_int(prompt):
    while True:
        try:
            integer = int(input(prompt)) 
        except ValueError:
            print("Please input an Integer")
            continue 
        break
    return integer
    
# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def input_something(prompt):
    while True:
        something = input(prompt);
        if len(something.strip()) == 0:
            print("Please enter something other than whitespace")
            continue
        else:
            break
    return something

def input_boolean(prompt):
    while True:
        value = input_something(prompt)
        if value.lower() in ["yes", "y"]:
            return True
        elif value.lower() in ["no", "n"]:
            return False
        else:
            print("Not a valid answer")
            continue

# This function opens "data.txt" in write mode and writes data_list to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def save_data(data_list):
    with open("data.txt", "w") as output:
        json.dump(data_list, output)

# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.
def load_data():
    with open("data.txt") as text:
        return json.load(text)

def addQuestion():
    questions = data = load_data()
    question = {
        "option_1": input_something("Enter first option: "),
        "option_2": input_something("Enter second option: "),
        "mature": input_boolean("Is this question for mature audiences only?: "),
        "votes_1": 0,
        "votes_2": 0,
    }
    questions.append(question)
    save_data(questions)

def listQuestions():
    pass

def searchQuestions():
    pass

def viewQuestion():
    pass

def deleteQuestion():
    pass


# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the "Would You Rather" Admin Program.')

if __name__ == "__main__":
    while True:
        print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
        choice = input('> ').lower() # Convert input to lowercase to make choice selection case-insensitive.
            
        if choice == 'a':
            # Add a new question.
            # See Point 3 of the "Requirements of admin.py" section of the assignment brief.
            addQuestion()
        
        elif choice == 'l':
            # List the current questions.
            # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
            listQuestions()

        elif choice == 's':
            # Search the current questions.
            # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
            searchQuestions()

        elif choice == 'v':
            # View a question.
            # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
            viewQuestion()

        elif choice == 'd':
            # Delete a question.
            # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
            deleteQuestion()

        elif choice == 'q':
            # Quit the program.
            # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
           break

        else:
            # Print "invalid choice" message.
            # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
            print("Invalid Choice, try again")

# If you have been paid to write this program, please delete this comment.
