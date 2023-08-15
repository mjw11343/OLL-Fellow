'''COMPARE
'''
import os
import csv
from dataclasses import dataclass, astuple

@dataclass
class Tribe():
    name: str
    basicApplied: bool
    basicYears: str
    enhancedApplied: bool
    enhancedYears: str
    basic2023: bool
    basic2022: bool
    basic2021: bool
    basic2020: bool
    basic2019: bool
    basic2018: bool
    enhanced2023: bool
    enhanced2022: bool
    enhanced2021: bool
    enhanced2020: bool
    enhanced2019: bool
    enhanced2018: bool


def export_to_csv(data, file_name):
    """
    Export a 2-dimensional list to a CSV file.

    Parameters:
        data (list): A 2-dimensional list to be exported.
        file_name (str): The name of the CSV file to be created.

    Returns:
        None
    """
    try:
        with open(file_name, 'w', newline='', encoding='utf-8-sig') as csvfile:
            csv_writer = csv.writer(csvfile)
            for row in data:
                csv_writer.writerow(row)
        print(f"Data successfully exported to '{file_name}'.")
    except IOError as e:
        print(f"Error while exporting to '{file_name}': {e}")


def importCSV(path):
    """
    Import a CSV file to a Dict.

    Parameters:
        data (str): The path to the CSV file to import.
    
    Returns:
        csv_reader (dict): Iterable dictionary of csv lines.
    """
    csvfile = open(path, newline='', encoding='utf-8-sig')
    csv_reader = csv.DictReader(csvfile)
    return csv_reader

def establishClass(basic, enhanced):
    """
    Organize basic and enhanced

    Returns:
        data (dict) = Dictionary of all unique tribes, with aggregated years.
    """
    data = {}
    print(basic)
    for row in basic:
        currLib = data.setdefault(row['Institution'], Tribe(name="" + row['Institution'], 
                                                          basicApplied=True, 
                                                          basicYears=""+row['Fiscal Year'],
                                                          enhancedApplied=False,
                                                          enhancedYears="",
                                                          basic2023=False,
                                                          basic2022=False,
                                                          basic2021=False,
                                                          basic2020=False,
                                                          basic2019=False,
                                                          basic2018=False,
                                                          enhanced2023=False,
                                                          enhanced2022=False,
                                                          enhanced2021=False,
                                                          enhanced2020=False,
                                                          enhanced2019=False,
                                                          enhanced2018=False))
        #tracking years applied to basic 
        if(row['Fiscal Year'] not in currLib.basicYears):
            currLib.basicYears = currLib.basicYears + ', ' + row['Fiscal Year']
        #tracking specific years
        if('2023' in currLib.basicYears):
            currLib.basic2023 = True
        if('2022' in currLib.basicYears):
            currLib.basic2022 = True
        if('2021' in currLib.basicYears):
            currLib.basic2021 = True
        if('2020' in currLib.basicYears):
            currLib.basic2020 = True
        if('2019' in currLib.basicYears):
            currLib.basic2019 = True
        if('2018' in currLib.basicYears):
            currLib.basic2018 = True
        #add currLib to new library: data
        data[currLib.name] = currLib
        #debug
        print(data[currLib.name])
    #adding enhanced library to data library
    for row in enhanced:
        currLib = data.setdefault(row['Institution'], Tribe(name="" + row['Institution'], 
                                                          basicApplied= False, 
                                                          basicYears="",
                                                          enhancedApplied=False,
                                                          enhancedYears=""+row['Fiscal Year'],
                                                          basic2023=False,
                                                          basic2022=False,
                                                          basic2021=False,
                                                          basic2020=False,
                                                          basic2019=False,
                                                          basic2018=False,
                                                          enhanced2023=False,
                                                          enhanced2022=False,
                                                          enhanced2021=False,
                                                          enhanced2020=False,
                                                          enhanced2019=False,
                                                          enhanced2018=False))
        #tracking years applied to basic 
        if("" == currLib.enhancedYears):
            currLib.enhancedYears = row['Fiscal Year']
        elif(row['Fiscal Year'] not in currLib.enhancedYears):
            currLib.enhancedYears = currLib.enhancedYears + ', ' + row['Fiscal Year']
        #tracking specific years
        if('2023' in currLib.enhancedYears):
            currLib.enhanced2023 = True
        if('2022' in currLib.enhancedYears):
            currLib.enhanced2022 = True
        if('2021' in currLib.enhancedYears):
            currLib.enhanced2021 = True
        if('2020' in currLib.enhancedYears):
            currLib.enhanced2020 = True
        if('2019' in currLib.enhancedYears):
            currLib.enhanced2019 = True
        if('2018' in currLib.enhancedYears):
            currLib.enhanced2018 = True
        #add currLib to new library: data
        data[currLib.name] = currLib
        #debug
        print(data[currLib.name])
    return data

def organize(tribes):
    highTribes = {}
    lowTribes = {}
    for t in tribes:
        if(not (t.basic2023 or t.basic2022 or t.basic2021 or t.basic2020 or t.basic2019 or t.basic2018
                or t.enhanced2023 or t.enhanced2022 or t.enhanced2021 or t.enhanced2020 or t.enhanced2019 or t.enhanced2018)):
            lowTribes[t.name] = t

tribes = {}

basic = importCSV(r"C:\Users\Slewe\OneDrive - UW-Madison\Open Law Library Fellowship\IMLS Grant Comparison\basicGrants.csv")
print(basic)

enhanced = importCSV(r"C:\Users\Slewe\OneDrive - UW-Madison\Open Law Library Fellowship\IMLS Grant Comparison\EnhancementGrants.csv")
print(enhanced)

tribes = establishClass(basic, enhanced)
print(len(tribes))

""" 
old sorting method

z = 0
while(z < len(theList)):
    if(theList[z][5]):
        theListNew.append(theList[z])
    z = z + 1
z = 0
while(z < len(theList)):
    if(not theList[z][5]):
        theListNew.append(theList[z])
    z = z + 1

export_to_csv(theListNew, 'fullData.csv')
"""