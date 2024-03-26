#!/usr/bin/env python3

"""
Georgia Institute of Technology - CS1301
HW09 - Recursion

"""

__author__ = """ Madison Schlaff """
__collab__ = """ Your collaboration statement here """




"""
Function name: popular_places
Parameters: list, list
Returns: list

"""

##########################

def popular_places(sites, num):
    if len(sites) == 0:
        return []
    elif len(sites) > 0 and sites[0][1] > num:
        return [sites[0][0]] + popular_places(sites[1:], num)
    else:
        return popular_places(sites[1:], num)
    
##########################





"""
Function name: stone_mountain_r
Parameters: list of tuples
Returns: int

"""

##########################

def stone_mountain_r(route_list):
    if len(route_list) == 0:
        return 0
    elif len(route_list) > 0 and ((route_list[0][0] / route_list[0][1]) * 60) < 20:
        return 1 + stone_mountain_r(route_list[1:])
    else:
        return stone_mountain_r(route_list[1:])
    
##########################





"""
Function name: stone_mountain_i
Parameters: list of tuples
Returns: int

"""

##########################

def stone_mountain_i(route_list):
    count = 0

    for item in range(len(route_list)):
        if ((route_list[item][0] / route_list[item][1]) * 60) < 20:
            count += 1

    return count

##########################





"""
Function name: travel_time
Parameters: dictionary, list
Returns: int

"""

##########################

def travel_time(time_dict, places):
    if len(places) < 2:
        return 0
    elif places[1] in time_dict[places[0]][0][0]:
        return time_dict[places[0]][0][1] + travel_time(time_dict, places[1:])
    elif places[1] in time_dict[places[0]][1][0]:
        return time_dict[places[0]][1][1] + travel_time(time_dict, places[1:])
    elif places[1] in time_dict[places[0]][2][0]:
        return time_dict[places[0]][2][1] + travel_time(time_dict, places[1:])
    
##########################





"""
Function name: fox_theatre_r
Parameters: str
Returns: int

"""

##########################

def fox_theatre_r(astr):
    if len(astr) < 3:
        return 0
    elif "f" in astr[0]:
        if "u" in astr[1]:
            if "n" in astr[2]:
                return 1 + fox_theatre_r(astr[1:])
    else:
        return fox_theatre_r(astr[1:])
    
##########################





"""
Function name: fox_theatre_i
Parameters: str
Returns: int

"""

##########################

def fox_theatre_i(astr):
    count = 0

    for ch in range(len(astr)):
        if "f" in astr[ch]:
            if "u" in astr[ch+1]:
                if "n" in astr[ch+2]:
                    count += 1

    return count

##########################





"""
Function name: fib_dictionary
Parameters: int
Returns: dict

"""

##########################

def fib_dictionary(num):
    if num <= 2:
        return {1:1, 2:1}
    else:
        mydict = fib_dictionary(num-1)
        mydict[num] = fib_dictionary(num-1)[num-1] + fib_dictionary(num-2)[num-2]
        return mydict
    
##########################





"""
Function name: balanced_str
Parameters: str
Returns: bool

"""

##########################

def balanced_str(astr):
    print(astr)
    if len(astr) <= 1:
        return True
    elif (astr[0].islower() == True and astr[-1].islower() == True) or (astr[0].isupper() == True and astr[-1].isupper() == True):
        return True and balanced_str(astr[1:-1])
    else:
        return False
    
##########################

