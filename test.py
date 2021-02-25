from admin import *
from json import dump, load
input_int("Type an integer: ")
input_something("Type anything but whitespace: ")

list = [1, 2, 3]
save_data(list)
with open("data.txt") as input:
    for i, v in enumerate(load(input)):
        print(v == list[i])

