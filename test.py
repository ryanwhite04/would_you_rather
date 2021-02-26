from admin import *
from json import dump, load
input_int("Type an integer: ")
input_something("Type anything but whitespace: ")
input_boolean("Type Yes or No")
list = [1, 2, 3]
save_data(list)
for i, v in enumerate(load_data()):
    print(v == list[i])

addQuestion()

print(load_data())

