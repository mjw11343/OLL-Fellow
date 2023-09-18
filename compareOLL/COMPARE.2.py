import csv
from dataclasses import dataclass, astuple
from pathlib import Path

# Data class to represent a tribe's information
@dataclass
class Tribe():
    name: str = ''
    basic_applied: bool = False
    basic_years_applied: str = ''
    enhanced_applied: bool = False
    enhanced_years_applied: str = ''
    basic_2023: bool = False
    basic_2022: bool = False
    basic_2021: bool = False
    basic_2020: bool = False
    basic_2019: bool = False
    basic_2018: bool = False
    enhanced_2023: bool = False
    enhanced_2022: bool = False
    enhanced_2021: bool = False
    enhanced_2020: bool = False
    enhanced_2019: bool = False
    enhanced_2018: bool = False
    num_basic_years_applied: int = 0
    num_enhanced_years_applied: int = 0
    can_apply_enhanced_2024: bool = True

def export_to_csv(data: list[Tribe], file_name: str):
    """
    Export a 2-dimensional list to a CSV file.

    Parameters:
        data (list): A 2-dimensional list to be exported.
        file_name (str): The name of the CSV file to be created.

    Returns:
        None
    """
    #conve
    try:
        # Get the current working directory as a Path object
        DIR = Path(__file__).parent

        # Construct the full path to the CSV file in the current directory
        full_path = DIR / file_name

        with open(full_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
            csv_writer = csv.writer(csvfile)
            for tribe in data:
                csv_writer.writerow(astuple(tribe))
        print(f"Data successfully exported to '{full_path}'.")
    except IOError as e:
        print(f"Error while exporting to '{full_path}': {e}")

def import_csv(path: str) -> csv.DictReader:
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

def transform_dictreader_to_dict(totalTribes: dict[str, Tribe], data: csv.DictReader, basic_o_enhanced: str) -> dict[str,Tribe]:
    """
    Organize basic and enhanced grant information for each tribe.

    Parameters:
        totalTribes (dict): Dictionary containing all unique tribes.
        data (csv.DictReader): DictReader (Iterable dictionary of csv lines) imported from a CSV file.
        basic_o_enhanced (str): 'basic' or 'enhanced' to indicate the type of grant.

    Returns:
        totalTribes (dict): Updated dictionary of tribes with grant information.
    """
    for row in data:
        currLib = totalTribes.setdefault(row['Institution'], Tribe(name=row['Institution']))
        # Track basic_applied, enhanced_applied
        setattr(currLib, basic_o_enhanced + '_applied', True)
        # Track basic_years_applied and enhanced_years_applied
        if row['Fiscal Year'] not in getattr(currLib, basic_o_enhanced + '_years_applied'):
            setattr(currLib, basic_o_enhanced + '_years_applied', getattr(currLib, basic_o_enhanced + '_years_applied') + ' ' + row['Fiscal Year'])
            setattr(currLib, f'num_{basic_o_enhanced}_years_applied', getattr(currLib, f'num_{basic_o_enhanced}_years_applied') + 1)
            #Tracking can_apply_enhanced_2024
            if('2023' in getattr(currLib, 'enhanced_years_applied')):
                setattr(currLib, 'can_apply_enhanced_2024', False)
            # Track specific years for the past six years
            if row['Fiscal Year'] in ('2023', '2022', '2021', '2020', '2019', '2018'):
                setattr(currLib, basic_o_enhanced + "_" + row['Fiscal Year'], True)
    return totalTribes

def organize(tribes_dict: dict[str, Tribe]) -> list[Tribe]:
    """
    Organize and sort tribe data for exporting.

    Parameters:
        tribes (dict): Dictionary containing tribe information.

    Returns:
        list (tuple): List of tuples representing sorted tribe information.
    """
    #convert to list of tribes
    tribes_list = list(tribes_dict.values())
    #then sort tribes
    tribes_list = sorted(tribes_list, key=lambda tribe: (tribe.can_apply_enhanced_2024, tribe.basic_years_applied), reverse=True)
    return tribes_list

# Initialize dictionary to store tribe data
tribes = {}

# Import basic grant data from CSV
DIR = Path(__file__).parent
file_path = DIR / "basicGrants.csv"
basic = import_csv(file_path)

# Import enhanced grant data from CSV
file_path = DIR / "EnhancementGrants.csv"
enhanced = import_csv(file_path)

# Organize basic grant information
tribes = transform_dictreader_to_dict(tribes, basic, 'basic')

# Organize enhanced grant information
tribes = transform_dictreader_to_dict(tribes, enhanced, 'enhanced')

# Organize and sort tribe data
tribes = organize(tribes)

# Insert headers and export sorted tribe data to CSV
tribes.insert(0, Tribe(name='Tribe Name', basic_applied='Applied to Basic Grant?', basic_years_applied='Years applied to Basic Grant', enhanced_applied='Applied to Enhancement Grant?', enhanced_years_applied='Years applied to Enhancement Grant', basic_2023='2023 Basic Grant', basic_2022='2022 Basic Grant', basic_2021='2021 Basic Grant', basic_2020='2020 Basic Grant', basic_2019='2019 Basic Grant', basic_2018='2018 Basic Grant', enhanced_2023='2023 Enhancement Grant', enhanced_2022='2022 Enhancement Grant', enhanced_2021='2021 Enhancement Grant', enhanced_2020='2020 Enhancement Grant', enhanced_2019='2019 Enhancement Grant', enhanced_2018='2018 Enhancement Grant', num_basic_years_applied='# of Applications to Basic Grant', num_enhanced_years_applied='# of Applications to Enhancement Grant', can_apply_enhanced_2024='Can Apply in 2024'))
export_to_csv(tribes, "sorted_tribes.csv")