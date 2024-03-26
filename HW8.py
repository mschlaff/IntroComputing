#!/usr/bin/env python3

"""
Georgia Institute of Technology - CS1301
HW08 - APIs/JSON

"""

__author__ = """ Madison Schlaff """
__collab__ = """ Your collaboration statement here """




"""
Function name: max_country
Parameters: list
Returns: string

"""

##########################

import requests

def max_country(countrylist):
    baseurl = "https://api.openaq.org/v1/countries/"
    r = requests.get(baseurl)
    data = r.json()
    count = 0
    topcountry = ""
    
    for adict in range(len(data["results"])):
        for country in countrylist:
            try:
                if data["results"][adict]["name"] == country:
                    if data["results"][adict]["count"] > count:
                        count = data["results"][adict]["count"]
                        topcountry = data["results"][adict]["name"]
            except:
                pass
    
    return topcountry

##########################





"""
Function name: chemical_dict
Parameters: string
Returns: dictionary

"""

##########################

import requests

def chemical_dict(locationid):
    url = "https://api.openaq.org/v1/locations/"+ locationid
    fullurl = url + locationid
    r = requests.get(url)
    data = r.json()
    countrydict = {}
    parameterlist = []
    newdict = {}
    
    try:
        for parameter in range(len(data["results"]["countsByMeasurement"])):
            newdict = {}
            newdict[data["results"]["countsByMeasurement"][parameter]["parameter"]] = data["results"]["countsByMeasurement"][parameter]["count"]
            parameterlist.append(newdict)
    except:
        return countrydict
    
    countrydict[data["results"]["sourceName"]] = parameterlist
    
    return countrydict

##########################





"""
Function name: chem_levels
Parameters: list, float
Returns: dictionary

"""

##########################
#WRITE YOUR FUNCTION HERE#
##########################





"""
Function name: get_important_details
Parameters: string
Returns: dictionary

"""

##########################

import requests

def get_important_details(rocketid):
    url = "https://api.spacexdata.com/v3/rockets/"+rocketid
    r = requests.get(url)
    data = r.json()
    newdict = {}

    for adict in data:
        if "rocket_name" in adict:
            newdict["rocket_name"] = data[adict]
        if "cost_per_launch" in adict:
            newdict["cost_per_launch"] = data[adict]
        if "payload_weights" in adict:
            newdict["no_of_payloads"] = len(data[adict])
        if "first_flight" in adict:
            newdict["first_flight"] = data[adict]
            
    return newdict

##########################





"""Function name: energy_consumed
Parameters: string
Returns: string

"""

##########################

import requests

def energy_consumed(rocketid):
    url = "https://api.spacexdata.com/v3/rockets/"+rocketid
    r = requests.get(url)
    data = r.json()
    energy = 0
    joules = 0
    
    for adict in data:
        if "error" in adict:
            returnstatement = "The rocket " + rocketid + " does not exist."
        if "first_stage" in adict:
            energy = data["first_stage"]["thrust_sea_level"]["kN"]
            burntime = data["first_stage"]["burn_time_sec"]
            joules = 1323000 * energy * burntime
            returnstatement = "The rocket " + rocketid + " consumes " + str(joules) + " joules during takeoff."

    return returnstatement

##########################






"""
Function name: space_roadster
Parameters: float, float
Returns: tuple

"""
##########################

import requests

def space_roadster(car1, car2):
    baseurl = "https://api.spacexdata.com/v3/roadster/"
    r = requests.get(baseurl)
    data = r.json()
    newtup = ()

    marsdistance = data["mars_distance_km"]
    car1distance = marsdistance * car1
    car2distance = marsdistance * car2
    newtup = (marsdistance, car1distance, car2distance)
    
    return newtup

##########################
