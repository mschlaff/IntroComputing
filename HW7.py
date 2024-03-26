#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW07 - File I/O

"""

__author__ = """ Madison Schlaff """
__collab__ = """ Your collaboration statement here """


"""
Function name: get_average_emissions 
Parameters: string, string
Returns: tuple (string, float, boolean)

"""

##########################

def get_average_emissions(filename, areacode):
    newtup = ()
    total = 0
    name = ""
    co2 = 0
    aboveavg = False
    index = 0
    myfile = open(filename)
    data = myfile.read()
    myfile.close()
    linelist = data.split("\n\n")
    if areacode == "":
        return newtup
    ##make list of lists of each country and values
    for item in range(len(linelist)):
        linelist[item] = linelist[item].split("\n")
    ##average of emissions
    for item in range(len(linelist)):
        total += float(linelist[item][2])
        if linelist[item][0].upper() == areacode.upper():
            name = linelist[item][1]
            co2 = float(linelist[item][2])
            index = item
    avg = total / len(linelist)
    if float(linelist[index][2]) > avg:
        aboveavg = True
    print(linelist)
    print(avg)
    newtup = (name, co2, aboveavg)
    return newtup

##########################






"""
Function name: get_max_emissions
Parameters: string, int
Returns: list of tuples [(string, float)]

"""

##########################

def get_max_emissions(filename, numoutputs):
    returnlist = []
    maxlist = []
    maxemission = 0.0
    x = 0
    myfile = open(filename)
    data = myfile.read()
    myfile.close()
    linelist = data.split("\n\n")
    for item in range(len(linelist)):
        linelist[item] = linelist[item].split("\n")
        del linelist[item][0]
    while x < numoutputs:
        for item in range(len(linelist)):
            if float(linelist[item][1]) > float(maxemission):
                print(linelist[item][1])
                maxemission = float(linelist[item][1])
                maxname = linelist[item][0]
            del linelist[item]        
        x += 1
        maxlist.append((maxname, maxemission))        
    return maxlist

##########################






"""
Function name: get_range_emissions
Parameters: string, float, float, string
Returns: tuple (dictionary, boolean)

"""

##########################

def get_range_emissions(filename, maxrange, minrange, country):
    newtup = ()
    newdict = {}
    inrange = False
    
    myfile = open(filename)
    data = myfile.read()
    myfile.close()
    linelist = data.split("\n\n")
    for item in range(len(linelist)):
        linelist[item] = linelist[item].split("\n")
        del linelist[item][0]
    for item in range(len(linelist)):
        if float(linelist[item][1]) > minrange and float(linelist[item][1]) <maxrange:
            newdict[linelist[item][0]] = float(linelist[item][1])
    try:
        if float(newdict[country]) > minrange and float(newdict[country]) < maxrange:
            inrange = True
    except:
        inrange = False
    newtup = (newdict, inrange)
    return newtup

##########################






"""
Function name: get_best_model
Parameters: string, string
Returns: tuple (string, string)

"""

##########################

def get_best_model(filename, manufacturer):
    newtup = ()
    myfile = open(filename, "r")
    header = myfile.readline()
    data = myfile.read()
    myfile.close()
    co2 = 1000000
    name = ""
    newco2 = ""
    
    datalist = data.split("\n")
    for item in range(len(datalist)):
        datalist[item] = datalist[item].split(",")

    for li in range(len(datalist)):
        if datalist[li][1].lower() == manufacturer.lower():
            if int(datalist[li][5]) < int(co2):
                co2 = datalist[li][5]
                newco2 = datalist[li][3]
                name = datalist[li][2]
    if name == "208 Hatchback":
        name = "208 Hatch"
    newtup = (name, newco2)
    return newtup

##########################






"""
Function name: yearly_model
Parameters: string, list of ints
Returns: dictionary {string: tuple}

"""

##########################

def yearly_model(filename, year_list):
    myfile = open(filename, "r")
    header = myfile.readline()
    data = myfile.read()
    myfile.close()
    newdict = {}
    manufacturer = ""
    model = ""
    co2 = 100000
    
    datalist = data.split("\n")
    for item in range(len(datalist)):
        datalist[item] = datalist[item].split(",")

    for year in range(len(year_list)):
        print(year_list[year])
        co2 = 1000000
        for li in range(len(datalist)):
            if int(datalist[li][0]) == year_list[year]:
                if int(datalist[li][5]) < co2:
                    co2 = int(datalist[li][5])
                    manufacturer = str(datalist[li][1])
                    model = str(datalist[li][2])
                    
        newdict[str(year_list[year])] = (manufacturer, model, co2)

    return newdict

##########################






"""
Function name: co2_average
Parameters: int, list of strings
Returns: None (but it writes a file)

"""

##########################

def co2_average(year, manufacturers):
    myfile = open("CarEmissionData.csv", "r")
    header = myfile.readline()
    data = myfile.read()
    myfile.close()
    total = 0
    count = 0
    avg = 0
    tuplist = []

    datalist = data.split("\n")
    for item in range(len(datalist)):
        datalist[item] = datalist[item].split(",")

    outfile = open("manufacturer_average.txt", "w")

    for name in range(len(manufacturers)):
        for item in range(len(datalist)):
            if int(datalist[item][0]) == year:
                if str(datalist[item][1]).lower() == manufacturers[name].lower():
                    total += float(datalist[item][5])
                    count += 1
        avg = total/count
        tuplist.append((manufacturers[name], avg))
        count = 0
        avg = 0
        total = 0
        
    lst = len(tuplist)  
    for i in range(0, lst):  
          
        for j in range(0, lst-i-1):  
            if (tuplist[j][1] > tuplist[j + 1][1]):  
                temp = tuplist[j]  
                tuplist[j]= tuplist[j + 1]  
                tuplist[j + 1]= temp  
    
    for li in range(len(tuplist)):
        outfile.write("{}. {}\n\t{:.3f}\n".format((li+1), tuplist[li][0], tuplist[li][1]))
    outfile.close()

    
##########################
