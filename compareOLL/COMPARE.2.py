'''COMPARE
'''
import os
from tkinter import filedialog
import csv

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
        with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            for row in data:
                csv_writer.writerow(row)
        print(f"Data successfully exported to '{file_name}'.")
    except IOError as e:
        print(f"Error while exporting to '{file_name}': {e}")


#this functions imports the CSV and puts it in a two dimensional
#array
def importCSV():
    #This allows you to choose 
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r', encoding="utf-8-sig") as f:
        linesOneD = f.readlines()
    x=0
    linesTwoD = []
    #If there are commas in the cell contents
    #there will be problems
    while(x < len(linesOneD)):
        linesOneD[x] = linesOneD[x].strip()
        linesTwoD.append(linesOneD[x].split(','))
        x = x + 1
    return linesTwoD

#list for tracks tribes: 1) name, 2) applied to basic, 3) years to basic, 4) applied to enhanced, 5) years to enhanced, 6) applied to both
theList = []
#theList 1st dimension is for each tribe
#   theList[x], x = each different tribe
#
#theList[x][0] = tribe name
#theList[x][1] = t/f applied to basic
#theList[x][2] = years applied to basic
#theList[x][3] = t/f applied to enhanced
#theList[x][4] = years applied to enhanced
#theList[x][5] = t/f applied to both
#theList[x][6] = '2023'
#theList[x][7] = '2022'
#theList[x][8] = '2021'
#theList[x][9] = '2020'
#theList[x][10] = '2019'
#theList[x][11] = '2018'
#theList[x][12] = '2023'
#theList[x][13] = '2022'
#theList[x][14] = '2021'
#theList[x][15] = '2020'
#theList[x][16] = '2019'
#theList[x][17] = '2018'

basic = importCSV()
#basic[x][0] = name
#basic[x][1] = year
#basic[x][2] = city
#basic[x][3] = state
#print(len(basic))
#print(basic)
enhanced = importCSV()
#enhanced[x][0] = name
#enhanced[x][1] = year
#enhanced[x][2] = city
#enhanced[x][3] = state
#print(enhanced)

x = 0
while(x < len(basic)):
    z = 0
    #print(x)
    while(z < len(theList)):
        if(basic[x][0] == theList[z][0]):
            theList[z][2] = theList[z][2] + '; ' + basic[x][1] #add the current duplicates year to the previous instance
            x = x + 1
            z = -1
        if(x >= len(basic)):
            break
        z = z + 1
    if(x >= len(basic)):
        break
    #print(basic[x][0])
    theList.append(['', False, '', False, '', False, '', '', '', '', '', '', '', '', '', '', '', ''])
    theList[len(theList) - 1][0] = basic[x][0] #makes [x][0] = name
    theList[len(theList) - 1][1] = True # makes [x][1] = True; because applied for basic
    theList[len(theList) - 1][2] = basic[x][1] #makes [x][2] = year; bc add year 
    x = x + 1

y = 0
while(y < len(enhanced)):
    z = 0
    #print(y)
    while(z < len(theList)):
        #print(len(theList))
        #print(enhanced[y][0] + z.__str__())
        if(enhanced[y][0] == theList[z][0]):
            theList[z][3] = True
            if(theList[z][4] == ''):
                theList[z][4] = enhanced[y][1]
            else:
                theList[z][4] = theList[z][4] + '; ' + enhanced[y][1]
            y = y + 1
            z = -1
        if(y >= len(enhanced)):
            break
        z = z + 1
    if(y >= len(enhanced)):
        break
    #print(enhanced[y][0])
    theList.append(['', False, '', False, '', False, '', '', '', '', '', '', '', '', '', '', '', ''])
    theList[len(theList) - 1][0] = enhanced[y][0] #makes [x][0] = name
    theList[len(theList) - 1][3] = True # makes [x][3] = True; because applied for enhanced
    theList[z][4] = enhanced[y][1]
    y = y + 1

print(theList)
#TXT file for list of all tribes applying to basic and enhanced
totalTribes = open("totalTribes.txt", "w")

#printing names of all tribes to totalTribes.txt
z = 0
while(z < len(theList)):
    totalTribes.write(theList[z][0] + "\n")
    z = z + 1


#TXT file for list of all tribes applying to basic and enhanced
totalTribes = open("totalTribes.txt", "w")

#printing names of all tribes to totalTribes.txt
z = 0
while(z < len(theList)):
    totalTribes.write(theList[z][0] + "\n")
    z = z + 1

#calculating applied to both grants
z = 0
while(z < len(theList)):
    if(theList[z][1] & theList[z][3]):
        theList[z][5] = True
    z = z + 1

#comparing the years
z = 0
while(z < len(theList)):
    if(theList[z][1]):
        if('2023' in theList[z][2]):
            theList[z][6] = 'X'
        if('2022' in theList[z][2]):
            theList[z][7] = 'X'
        if('2021' in theList[z][2]):
            theList[z][8] = 'X'
        if('2020' in theList[z][2]):
            theList[z][9] = 'X'
        if('2019' in theList[z][2]):
            theList[z][10] = 'X'
        if('2018' in theList[z][2]):
            theList[z][11] = 'X'
    if(theList[z][3]):
        if('2023' in theList[z][4]):
            theList[z][12] = 'X'
        if('2022' in theList[z][4]):
            theList[z][13] = 'X'
        if('2021' in theList[z][4]):
            theList[z][14] = 'X'
        if('2020' in theList[z][4]):
            theList[z][15] = 'X'
        if('2019' in theList[z][4]):
            theList[z][16] = 'X'
        if('2018' in theList[z][4]):
            theList[z][17] = 'X'
    z = z + 1

#ordering the tribes
theListNew = []

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

#exporting
export_to_csv(theListNew, 'fullData.csv')