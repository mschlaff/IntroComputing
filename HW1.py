#!/usr/bin/env python3


"""
Georgia Institute of Technology - CS1301
HW01 - Functions and Statements

"""

__author__ = """Madison Schlaff"""
__collab__ = """I worked on the homework assignment alone, using only this semesters course materials."""




"""
Function name: delivery_time()
Parameters: no parameters
Return value: None

"""
###########################

def delivery_time():
    num_nuggs = int(input("How many orders of nuggets woudl you like?"))
    num_milks = int(input("How many milkshakes would you like?"))
    num_corn = int(input("How many corn dogs would you like?"))

    delivery = (num_nuggs * 15) + (num_milks * 10) + (num_corn * 20)
    hours = int(delivery / 60)
    mins = delivery % 60

    print( str(num_nuggs) + " orders of nuggets, " + str(num_milks) + " milkshakes, and " + str(num_corn) + " corn dogs will take " + str(hours) + " hour(s) and " + str(mins) + " minutes.")

###########################




"""
Function name: shortcut()
Parameters: no parameters
Return value: None
"""
###########################
from math import sqrt

def shortcut():
    width = float(input("What is the width of Tech Green?"))
    length = float(input("What is the length of Tech Green?"))

    hypotenuse = sqrt(width**2 + length**2)
    hypotenuse = round(hypotenuse, 2)

    print("Tech Green with a width of " + str(width) + " on one side and " + str(length) + " on the other side has a diagonal length of " + str(hypotenuse) + ".")    

###########################




"""
Function name: buff_up()
Parameters: no parameters
Returns: None

"""
###########################

def buff_up():
    wanna_lift = int(input("How many pounds do you want to lift today?"))
    
    two_leftover = wanna_lift % 2
    
    fifteen_leftover = wanna_lift % 15

    ninety_leftover = wanna_lift % 90

    print ("When lifting " + str(wanna_lift) + " pounds, you would have " + str(two_leftover) + " pounds left using 2 pound weights, " + str(fifteen_leftover) + " pounds left using 15 pound weights, and " + str(ninety_leftover) + " pounds left using 90 pound weights.")

###########################




"""
Function name: vending()
Parameters: no parameters
Returns: None

"""
###########################

def vending():

    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01

    cost_chips = float(input("How much does the bag of chips cost? "))

    num_quarters = float(cost_chips // quarter)
    cost_chips = round(cost_chips % quarter, 2)

    num_dimes = float(cost_chips // dime)
    cost_chips = round(cost_chips % dime, 2)

    num_nickels = float(cost_chips // nickel)
    cost_chips = round(cost_chips % nickel, 2)

    num_pennies = cost_chips * 100

    print("You need " + str(num_quarters) + " quarters, " + str(num_dimes) + " dimes, " + str(num_nickels) + " nickels, and " + str(num_pennies) + " pennies to pay for the chips.")


###########################




"""
Function name: split_trip()
Parameters: no parameters
Returns: None

"""
###########################

def split_trip():

    cost_trip = float(input("How much was your trip?"))
    num_friends = int(input("How many friends came with you on the trip?"))
    interest = float(input("What percent interest is the bank charging you?"))

    total_cost = cost_trip * (1 + interest)

    split_pay = total_cost / num_friends
    split_pay = round(split_pay, 2)

    print ("The total cost per a person is $" + str(split_pay) + ".")

###########################

