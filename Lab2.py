#!/usr/bin/env python3

"""
Georgia Institute of Technology - CS1301
Lab02 - Data Analytics

"""

__author__ = """ Your name here """
__collab__ = """ Your collaboration statement here """"""





Function name: credit_count
Parameters: int
Returns: dictionary

"""

##########################

def credit_count(num):
    myfile = open("data.csv", "r")
    header = myfile.readline()
    data = myfile.readlines()
    myfile.close()
    count = 0
    yearlist = ["1st", "2nd", "3rd", "4th+"]
    newdict = {}

    for year in yearlist:
        count = 0
        for aline in data:
            pieces = aline.split(",")
            if pieces[3] == year:
                if pieces[4] == num:
                    count += 1
        newdict[year] = count

    return newdict

##########################





"""
Function name: new_friends
Parameters: string, int, string
Returns: int

"""

##########################

def new_friends(major, year, residency):
    myfile = open("data.csv", "r")
    header = myfile.readline()
    data = myfile.readlines()
    myfile.close()
    count = 0

    for aline in data:
        pieces = aline.split(",")
        if major in pieces[0]:
            if year in pieces[3]:
                if residency in pieces[2]:
                    count += 1

    return count

##########################





"""
Function name: stay_safe
Parameters: string
Returns: dictionary

"""

##########################

def stay_safe(year):
    myfile = open("data.csv", "r")
    header = myfile.readline()
    data = myfile.readlines()
    myfile.close()
    
    yearcount = 0
    numcount = 0
    lightscount = 0
    appcount = 0
    safe = 1

    for aline in data:
        pieces = aline.split(",")
        if year in pieces[3]:
            yearcount += 1
            if "Yes" in pieces[6]:
                numcount += 1
            elif "Yes" in pieces[12]:
                lightscount += 1
            elif "Yes" in pieces[13]:
                appcount += 1
    
    if (numcount/yearcount >= 0.5):
        safe += 1
    
    elif (lightscount/yearcount >= 0.5):
        safe += 1
    
    elif (appcount/yearcount >= 0.5):
        safe += 1
    
    if safe >= 2:
        return "prepared"
    elif safe == 1:
        return "cautious"
    elif safe == 0:
        return "not prepared"
    
##########################





"""
Function name: east_vs_west
Parameters: string
Returns: tuple

"""

##########################

def east_vs_west(location):
    myfile = open("data.csv", "r")
    header = myfile.readline()
    data = myfile.readlines()
    myfile.close()

    locationcount = 0
    stolencount = 0
    stolenpercent = 0
    newtup = ()

    for aline in data:
        pieces = aline.split(",")
        if location in pieces[5]:
            locationcount += 1
            if "None of the above" not in pieces[8]:
                stolencount += 1

    stolenpercent = round((stolencount/locationcount) * 100, 2)

    newtup = (location, stolenpercent)

    return newtup

##########################





"""
Function name: clumsy_majors
Parameters: list
Returns: dictionary

"""

##########################

def clumsy_majors(majors):
    myfile = open("data.csv", "r")
    header = myfile.readline()
    data = myfile.readlines()
    myfile.close()
    
    newdict = {}

    for item in majors:
        studentcount = 0
        lostcount = 0
        lostpercent = 0
        for aline in data:
            pieces = aline.split(",")
            if item in pieces[0]:
                studentcount += 1
                if "Yes" in pieces[9]:
                    lostcount += 1
        try:
            lostpercent = (lostcount/studentcount) * 100
            if lostpercent >= 40:
                newdict[item] = True
            else:
                newdict[item] = False

        except:
            pass

    return newdict

##########################

