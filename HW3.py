#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301HW03 - Iteration
"""

__author__ = """Madison Schlaff"""
__collab__ = """I worked on the homework assignment alone, using only this semesters course materials."""





"""
Function name: scariest_ride
Parameters: string
Return value: int

"""

##########################

def scariest_ride(scream):
    num = 0
    for letter in scream:
        if letter .isupper():
            num += 1
    return num

##########################





"""
Function name: mind_reader
Parameters: string
Return value: string

"""

##########################

def mind_reader(message):
    num = 0
    letters = 0
    string = ""
    
    for letter in message:
        if letter .isalpha() and letters % 2 == 1:
            string += str(letter)
            
        elif letter == " ":
            string += str(letter)

        elif num < 3 and letters % 2 == 0:
            if letter .isdigit():
                string += str(letter)
                num += 1

        letters += 1

    return string

##########################





"""
Function name: bravest_soul
Parameters: string
Return value: string

"""

##########################

def bravest_soul(names):
    max_ride = 0
    curr_ride = ""
    name = ""
    current_name = ""
    index = 0
    x = 0

    while x < len(names):
        curr_ride = ""
        while x < len(names) and names[x].isdigit():
            curr_ride += str(names[x])
            x+=1
        if (curr_ride != "") and (int(curr_ride) > max_ride):
            max_ride = int(curr_ride)
            maxindex = index
        if curr_ride != "":
            index += 1
        else:
            x += 1
    index = 0
    y = 0
    while y <len(names):
        current_name = ""
        if names[y] == ",":
            index += 1
            y += 1
            continue
        if index == maxindex:
            while y < len(names) and (names[y].isalpha() or names[y] == " "):
                current_name += names[y]
                y+= 1
            break
        y += 1
    return current_name

##########################






"""
Function name: nausea
Parameters: string, bool
Return value: string

"""

##########################

def nausea(pattern, ate_lunch):
    
    letterO = 0
    if ate_lunch:
        for letter in pattern:
            if letter == "O":
                letterO += 1
            elif letter != "O":
                letterO = 0
            if letterO >= 3:
                return "I don't feel so good..."

    if ate_lunch == False:
        for letter in pattern:
            if letter == "O":
                letterO += 1
            elif letter != "O":
                letterO = 0
            if letterO >= 3:
                return "I got this."
            
    return "Let's do this!"

##########################





"""
Function name: dessert_knockoffs
Parameters: string, string, string
Return value: string
"""
##########################

def dessert_knockoffs(dessert, knockoff):

    similarity = 0
    num_letters1 = 0
    num_letters2 = 0

    for letter in dessert:
        num_letters1 += 1
    for letters in knockoff:
        num_letters2 += 1
        
    if num_letters1 == num_letters2:
        for letter in dessert:
            for letters in knockoff:
                if letter == letters:
                    similarity += 1
                else:
                    similarity += 0

    if similarity >= (num_letters1 // 2):
        return True

    else:
        return False
    
##########################
