from admin import *
from json import dump, load

questions = [
    {
        "option_1": "Fight a horse-sized duck",
        "option_2": "Fight 100 duck-sized horsed",
        "mature": True,
        "votes_1": 3,
        "votes_2": 5,
    },
    {
        "option_1": "Be invisible",
        "option_2": "Be able to fly",
        "mature": False,
        "votes_1": 0,
        "votes_2": 0,
    }
]
save_data(questions)
input_int("Type an integer: ")
input_something("Type anything but whitespace: ")
input_boolean("Type Yes or No")
addQuestion()
listQuestions()
searchQuestions()
viewQuestion()
