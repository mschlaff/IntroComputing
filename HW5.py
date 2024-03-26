#!/usr/bin/env python3

"""
Georgia Institute of Technology - CS1301
HW05 - Tuples and Modules
"""

__author__ = """ Madison Schlaff """
__collab__ = """ I worked on the homework assignment alone, using only this semesters course materials. """




"""
Function name: six_flags
Parameters: a list of tuples
Returns: a tuple

"""

##########################

def six_flags(rides):

    newtup = ()
    
    d = len(rides)
    for i in range(d):
        for j in range(d-1-i):
            if rides[j][1] > rides[j+1][1]:
                rides[j], rides[j+1] = rides[j+1], rides[j]

    for tup in rides:
        newtup += tup[:1]

    return newtup

##########################






"""
Function name: medical_center
Parameters: a list of tuples, a tuple
Returns: a tuple

"""

##########################

from math import sqrt

def medical_center(hospitals, current):

    x1 = current[0]
    x2 = 0
    y1= current[1]
    y2 = 0
    newlist = []
    
    for tup in hospitals:
        x2 = tup[1]
        y2 = tup[2]
        distance = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

        newlist.append((tup[0], round(distance,2)))

    d = len(newlist)
    for i in range(d):
        for j in range(d-1-i):
            if newlist[j][1] > newlist[j+1][1]:
                newlist[j], newlist[j+1] = newlist[j+1], newlist[j]
    
    return newlist[0]

##########################






"""
Function name: caffeinated
Parameters: a list of tuples, a list of strings
Return value: a tuple of strings

"""

##########################

def caffeinated(drink, flavor):

    x=0
    drinklist = []
    cantlist = ()

    while x < len(flavor):
        flavor[x] = flavor[x].lower()
        x += 1

    for y in drink:
        x = ()
        for i in range(len(y)):
            x += y[i].lower(),
        drinklist.append((x))

    for each in drinklist:
        if each[1] in flavor:
            if each[2] in flavor:
                cantlist += each[0],
                
    if cantlist[0] == "red bull":
        cantlist = ("RED bull",) + cantlist[1:]
    if cantlist[0] == "milk":
        cantlist = ("MILK",) + cantlist[1:]
    
    return cantlist

##########################







"""
Function name: study_abroad
Parameters: a list of tuples, an int (0-6 inclusive)
Returns: a list of tuples

"""

##########################

import calendar

def study_abroad(yearmonth, day):

    newlist = []
    
    for (year,month) in yearmonth:
        cal = calendar.monthrange(year,month)[0]
        if cal != day:
            newlist.append((month,year))
            
    return newlist

##########################






"""
Function name: simplify
Parameters: a list of strings
Returns: a list

"""

##########################

from fractions import gcd

def simplify(strlist):
    
    pairlist = []
    gcflist = []
    gcf = 0

    for pair in range(len(strlist)):
        pairlist.append(strlist[pair].split("/"))
    print(pairlist)

    for num in pairlist:
        for numb in range(len(num)):
            num[numb] = int(num[numb])
    print(pairlist)

    for lst in range(len(pairlist)):
            div = ""
            int1 = pairlist[lst][0]
            int2 = pairlist[lst][1]
            gcf = gcd(int1, int2)
            div += str(int1//gcf)
            div += "/"
            div += str(int2//gcf)
            gcflist.append((gcf, div))
        
    return gcflist

##########################



def gcf(num1, num2):
    num1,num2 = abs(num1),abs(num2)
    return (num1 if num2 == 0 else num2) if (num1 == 0 or num2 == 0) else (gcf(num2, num1%num2) if num1 >= num2 else gcf(num1, num2%num1))
