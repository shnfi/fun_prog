#!/bin/python3

string = "Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Yankee Oscar Uniform Dash Sierra One November Kilo India November Golf Dash Four Bravo Zero Uniform Seven"

string = string.split(" ")

numbers_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for i in string :
    if i.lower() == "dash" :
        print("-", end="")
    elif i.lower() in numbers_dict :
        print(numbers_dict[i.lower()], end="")
    else :
        print(i[0], end="")

print()
