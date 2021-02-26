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
# Import os to check if file exists
import os

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
        json.dump(data_list, output, indent=4)

# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.
def load_data():
    path = "data.txt"
    if os.path.isfile(path):
        with open(path) as text:
            return json.load(text)
    else:
        return []

def addQuestion():
    questions = load_data()
    print('Both options should be phrased to follow "Would you rather..."')
    option1 = input_something("Enter option 1: ")
    while True:
        option2 = input_something("Enter option 2: ")
        if option2 == option1:
            print("The options should be different")
            continue
        else:
            break
    question = {
        "option_1": option1[0:-1] if option1.endswith("?") else option1,
        "option_2": option2[0:-1] if option2.endswith("?") else option2,
        "mature": input_boolean("Is this question intended for mature audiences only? [Y/N]: "),
        "votes_1": 0,
        "votes_2": 0,
    }
    questions.append(question)
    save_data(questions)

def listQuestions():
    print("List of questions:")
    questions = load_data()
    if len(questions):
        for i, question in enumerate(questions):
            print(i+1, f'{question["option_1"]}/{question["option_2"]}') 
    else:
        print("No questions saved")

def searchQuestions():
    def questionHasTerm(term, question):
        option_1 = question[1]["option_1"].lower()
        option_2 = question[1]["option_2"].lower()
        query = term.lower()
        return query in option_1 or query in option_2

    query = input_something("Enter search term: ")
    questions = load_data()
    matches = [question for question in enumerate(questions) if questionHasTerm(query, question)]
    if len(matches):
        print("Search results:")
        for i, match in matches:
            print(f' {i+1}) {match["option_1"]} / {match["option_2"]}') 
    else:
        print("No questions saved")

def displayVotes(votes_1, votes_2):
    if (votes_1 or votes_2):
        ratio_1 = round(100*votes_1/(votes_1 + votes_2), 1)
        ratio_2 = round(100 - ratio_1, 1)
        noun_1 = "votes" if votes_1 != 1 else "vote"
        noun_2 = "votes" if votes_2 != 1 else "vote"
        print(f'Option 1 has received {votes_1} ({ratio_1}%) {noun_1}, Option 2 has received {votes_2} ({ratio_2}%) {noun_2}.') 
    else:
        print("Nobody has answered this question")

def displayQuestion(question):
    print("Would you rather...")
    print(f' Option 1) {question["option_1"]}?')
    print(f' Option 2) {question["option_2"]}?\n')
    question['mature'] and print('This question is for mature audiences only')
    displayVotes(question["votes_1"], question["votes_2"])

def viewQuestion():
    questions = load_data()
    if len(questions):
        index = input_int("Enter the index of a question: ") - 1
        if 0 <= index < len(questions):
            displayQuestion(questions[index])
        else:
            print("Invalid index number")
    else:
        print("No questions saved")

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
