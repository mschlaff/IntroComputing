#!/usr/bin/env python3

"""
Georgia Institute of Technology
CS1301HW04
Lists

"""

__author__ = """Madison Schlaff"""
__collab__ = """I worked on the homework assignment alone, using only this semesters course materials."""




"""
Function name: str_to_list
Parameters: list or string
Return value: string or list

"""

##########################

def str_to_list(ints_or_string):
    list1 = []
    str1 = "["


    if isinstance(ints_or_string, list):
        if ints_or_string == []:
            ints_or_string = str1
            str1 += "]"
            return str1
        else:
            for x in range(len(ints_or_string)):
                str1 += str(ints_or_string[x])
                if x < len(ints_or_string)-1:
                    str1+= ", "
                if x == len(ints_or_string)-1:
                    str1 += "]"
            return str1

    if isinstance(ints_or_string, str):
        if ints_or_string == []:
            ints_or_string = list1
            return list1
        else:
            for y in range(len(ints_or_string)):
                if ints_or_string[y].isdigit():
                    list1 += ints_or_string[y]
                elif ints_or_string[y].isalpha():
                    list1 += str(ints_or_string[y])
            return list1
    
##########################





"""Function name: list_to_int
Parameters: list
Return value: int or None

"""

##########################

def list_to_int(list_ints):
    int1 = 0

    if list_ints == []:
        return None
    
    elif type(list_ints) == list:
        list_ints.sort(reverse = False)
        x = 0
        while x < len(list_ints):
            if x == 0:
                int1 += list_ints[x]
            elif x > 0:
                list_ints[x] = list_ints[x] * (10 ** x)
                int1 += list_ints[x]
            x += 1
        return int1
                
    else:
        return None

##########################






"""
Function name: compound_word
Parameters: list
Return value: list

"""

##########################

def compound_word(words):
    x = 0
    list1 = []
    if words == []:
        return list1
    
    elif len(words) == 1:
        return list1
    
    elif type(words) == list:
        for i in range(len(words)):
            if x < len(words) // 2:
                words[x] += words[len(words) - x - 1]
                list1.append(words[x])
                x += 1
            else:
                break
        return list1
    
    else:
        return None
    
##########################





"""Function name: swap_strings
Parameters: list
Return value: None

"""

##########################

def swap_strings(list1):
    
    for x in range(len(list1)):
        if x % 2 == 0 and x < len(list1) - 1:
            a = list1[x]
            b = list1[x+1]
            list1[x] = b
            list1[x+1] = a
            
    for x in range(len(list1)):
        str1 = ""
        for u in range(len(list1[x])):
            if list1[x][u].isdigit():
                str1 += list1[x][u]
        list1[x] = str1
    return list1

##########################





"""
Function name: continuous_sum
Parameters: list
Return value: int

"""

##########################

def continuous_sum(list_ints, target):
    sumnums = 0
    targetsum = 0
    
    if list_ints == []:
        return sumnums

    elif type(list_ints) == list:
        for x in range(len(list_ints)):
            if targetsum == target:
                sumnums += 1
                
            if list_ints[x] == target:
                sumnums += 1

            elif list_ints[x] > target:
                sumnums += list_ints[x]

    return sumnums

##########################
