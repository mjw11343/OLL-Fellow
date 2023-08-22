'''COMPARE
'''
import os
import csv
from dataclasses import dataclass, astuple

@dataclass
class Tribe():
    name: str = ''
    basicApplied: bool = False
    basicYears: str = ''
    enhancedApplied: bool = False
    enhancedYears: str = ''
    basic2023: bool = False
    basic2022: bool = False
    basic2021: bool = False
    basic2020: bool = False
    basic2019: bool = False
    basic2018: bool = False
    enhanced2023: bool = False
    enhanced2022: bool = False
    enhanced2021: bool = False
    enhanced2020: bool = False
    enhanced2019: bool = False
    enhanced2018: bool = False
    numBasicYearsApplied: int = 0
    numEnhancedYearsApplied: int = 0
    canApplyEnhanced2023: bool = True

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

def establishClass(totalTribes, data, basicOenhanced):
    """
    Organize basic and enhanced

    Returns:
        data (dict) = Dictionary of all unique tribes .
    """
    for row in data:
        print(row) #debugging
        currLib = totalTribes.setdefault(row['Institution'], Tribe(name=row['Institution']))
        #tracking basicApplied, enhancedApplied
        setattr(currLib, basicOenhanced + 'Applied', True)
        #tracking basicYears and enhancedYears
        if(getattr(currLib, basicOenhanced + 'Years') == ""):
            setattr(currLib, basicOenhanced + 'Years', row['Fiscal Year'])
        elif(row['Fiscal Year'] not in getattr(currLib, basicOenhanced + 'Years')):
            setattr(currLib, basicOenhanced + 'Years', getattr(currLib, basicOenhanced + 'Years') + ', ' + row['Fiscal Year'])
        #tracking specific years for the past six years
        if(row['Fiscal Year'] in ('2023', '2022', '2021', '2020', '2019', '2018')):
            setattr(currLib, basicOenhanced + row['Fiscal Year'], True)
        #tracking canApplyEnhanced2023
        if('2022' in getattr(currLib, 'enhancedYears')):
            setattr(currLib, 'canApplyEnhanced2023', False)
        #tracking numBasicYearsApplied and numEnhancedYearsApplied
        setattr(currLib, 'numBasicYearsApplied', len(getattr(currLib, 'basicYears').split()))
        setattr(currLib, 'numEnhancedYearsApplied', len(getattr(currLib, 'enhancedYears').split()))
    return totalTribes

def organize(tribes):
    #make a list of tuples, each tribe is one row
    list = []
    for tribe in tribes:
        list.append(astuple(tribes[tribe]))
    #sort the tribes by basic2022, then basic2021, then basic2020, then whether they applied to 
    list = sorted(list, key=lambda tribe: (tribe[19], tribe[2], tribe[4]), reverse=True)
    return list

tribes = {}

basic = importCSV(r"C:\Users\Slewe\OneDrive - UW-Madison\Open Law Library Fellowship\IMLS Grant Comparison\basicGrants.csv")
print(basic)

enhanced = importCSV(r"C:\Users\Slewe\OneDrive - UW-Madison\Open Law Library Fellowship\IMLS Grant Comparison\EnhancementGrants.csv")
print(enhanced)

tribes = establishClass(tribes, basic, 'basic')
tribes = establishClass(tribes, enhanced, 'enhanced')
print(len(tribes))

tribes = organize(tribes)

tribes.insert(0, ('Tribe Name', 'Applied to Basic Grant?', 'Years applied to Basic Grant', 'Applied to Enhancement Grant?', 'Years applied to Enhancement Grant', '2023 Basic Grant', '2022 Basic Grant', '2021 Basic Grant', '2020 Basic Grant', '2019 Basic Grant', '2018 Basic Grant', '2023 Enhancement Grant', '2022 Enhancement Grant', '2021 Enhancement Grant', '2020 Enhancement Grant', '2019 Enhancement Grant', '2018 Enhancement Grant', '# of Applications to Basic Grant', '# of Applications to Enhancement Grant', 'Can Apply in 2023'))
export_to_csv(tribes, "sorted_tribes.csv")