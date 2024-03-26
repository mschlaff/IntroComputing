#!/usr/bin/env python3

"""Georgia Institute of Technology - CS1301
HW02 - Returns and Conditionals"""

__author__ = """Madison Schlaff"""
__collab__ = """I worked on the homework assignment alone, using only this semesters course materials."""




"""Function name: goingToTheMovies()
Parameters: age (int), popcorn buckets (int), sodas (int)
Return value: a float"""

##########################

def goingToTheMovies(age, num_popcorn, num_sodas):

    ticket = 9.75
    popcorn = 4.99
    soda = 2.99
    
    if age >= 65:
        ticket = 7.50

    total =  (num_popcorn * popcorn) + (num_sodas * soda) + ticket
    total = round(total, 2)
    
    return total

##########################




"""Function name: minimumTestGrade()
Parameters: current grade (float), weight of exam (float), desired letter grade (string)
Return value: a float"""

##########################

def minimumTestGrade(current_grade, exam_weight, desired_letter):

    desired_grade = 100.0
    
    if desired_letter == "A":
        desired_grade = 90.0

    elif desired_letter == "B":
        desired_grade = 80.0

    elif desired_letter == "C":
        desired_grade = 70.0

    grade_needed = (desired_grade - ((1 - exam_weight) * current_grade)) / exam_weight

    print(grade_needed)

    grade_needed = round(grade_needed, 2)
    
    if grade_needed <= 100:
        return grade_needed
    else:
        return "Not possible."
    
##########################




"""Function name: isTestSuccessful()
Parameters: hours of sleep (int), current grade (float),
weight of exam (float),desired letter grade (string)
Return value: a boolean"""

##########################

def isTestSuccessful(hours_sleep, current_grade, exam_weight, desired_letter):

    if minimumTestGrade(current_grade, exam_weight, desired_letter) == "Not possible.":
        return False
    elif minimumTestGrade(current_grade, exam_weight, desired_letter) <= 80 and hours_sleep >= 7:
        return True
    else:
        return False
    
##########################




"""Function name: speedingTicket()
Parameters:  speed (int), speed limit (int)
Return value: a string"""

##########################

def speedingTicket(speed, limit):

    points = 0
    
    if ((speed - limit) // 5) == 1:
        points += 1
        
    elif ((speed - limit) // 5) == 2:
        points += 2

    elif((speed - limit) // 5) == 3:
        points += 3

    elif((speed - limit) // 5) == 4:
        points += 4

    elif((speed - limit) // 5) == 5:
        points += 5

    elif((speed - limit) // 5) == 6:
        points += 6

    elif((speed - limit) // 5) == 7:
        points += 7

    elif((speed - limit) // 5) == 8:
        points += 8

    elif((speed - limit) // 5) == 9:
        points += 9

    elif((speed - limit) // 5) ==10:
        points += 10

    elif((speed - limit) // 5) > 10:
        return "License Suspended"

    else:
        return "Continue driving safely"

    return "Points Added: {}".format(points)

##########################




"""Function name: trolleyOrWalk()
Parameters: weather (string), distance (float)
Return value: a string"""

##########################

def trolleyOrWalk(weather, distance):

    if weather == "Drizzle" and distance <= 0.5:
        return "Walk"
    elif weather == "Cloudy" and distance <1.0:
        return "Walk"
    elif weather == "Sunny" and distance < 0.5:
        return "Walk"
    elif weather == "Sunny" and distance >= 0.75:
        return "Walk"
    elif weather == "Thunder" and distance <= 0.1:
        return "Walk"
    elif weather == "Drizzle" and distance > 0.5:
        return "Trolley"
    elif weather == "Thunder" and distance > 0.1:
        return "Trolley"
    elif weather == "Sunny" and distance >= 0.5 and distance < 0.75:
        return "Trolley"
    elif weather == "Cloudy" and distance >= 1.0:
        return "Trolley"
    
##########################




"""Function name: gymMemberships()
Parameters: numberOfMembers (int), months (int),
gymA (string), gymB (string)
Return value: a string"""

##########################

def gymMemberships(num_members, months, gymA, gymB):

    kickboxing = (25 + (65 * months)) * num_members
    if num_members > 3:
        kickboxing = (65 * months) * num_members
        
    yoga = (50 + (70 * months)) * num_members
    
    spinning = (75 * months) * num_members
    if num_members > 2:
        spinning -= 10*num_members

    pilates = (68 * months) * num_members


    if gymA > gymB:
        return gymB
    elif gymA < gymB:
        return gymA
    elif gymA == gymB:
        return gymA
    
##########################
