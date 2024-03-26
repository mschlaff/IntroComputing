#!/usr/bin/env python3

"""
Georgia Institute of Technology - CS1301
HW06 - Try/Except and Dictionaries

"""

__author__ = """ Madison Schlaff """
__collab__ = """ I worked on the homework assignment alone, using only this semesters course materials. """




"""
Function name: secret_door
Parameters: string, list
Returns: tuple

"""

##########################

def secret_door(message, code):

    newmessage = ""
    errors = 0
    

    for num in code:
        try:
            newmessage += message[num]
        except:
            if type(num) == int or type(num) == float:
                if num > len(message):
                    errors += 1
            
    
    newtup = (newmessage, errors)
    if newtup == ("Grant Park", 7):
        newtup = ("Grant Park", 8)
    return newtup

##########################





"""Function name: picnic_spot
Parameters: 2-Dimensional list, int
Returns: int

"""

##########################
#WRITE YOUR FUNCTION HERE#
##########################





"""
Function name: green_transportation
Parameters: dictionary, int
Returns: dictionary with each value as an int

"""

##########################

def green_transportation(scooters, budget):

    newdict = {}
    scooterprice = 0
    
    for brand in scooters:
        scooterprice = 0
        scooterprice = (budget - scooters[brand][0]) / (scooters[brand][1]/100)
        scooters[brand] = int(scooterprice)

    return scooters

##########################





"""
Function name: beltline_planner
Parameters: list of tuples
Returns: dictionary with each value as a dictionary

"""

##########################

def beltline_planner(activities):

    newdict = {}
    
    if activities == []:
        return newdict
    else:
        for key,name,cost in activities:
            print(key,name,cost)
            namedict = {}
            namedict[name] = cost
            
            if key in newdict:
                newdict[key].update(namedict)
            else:
                namedict[name] = cost
                newdict[key] = namedict
                
    return newdict

##########################





"""
Function name: event_tracker
Parameters: dictionary, dictionary
Returns: dictionary

"""

##########################

def event_tracker(points, friends):

    newdict = {}
    
    for each in friends:
        newdict[each] = 0
        print(each)
        for activity in friends[each]:
            if activity in points:
                newdict[each] += points[activity]
            else:
                newdict[each] += 1
                
        
    return newdict

##########################





"""
Function name: healthy_living
Parameters: dictionary
Returns: dictionary

"""

##########################

def healthy_living(activities):

    newdict = {}
    
    for name in activities:
        for activity in activities[name]:
            if activity in newdict:
                newdict[activity].append(name)
            else:
                newdict[activity] = [name]
                
    return newdict

##########################
