'''COMPARE
'''
import os
from tkinter import filedialog

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

basic = importCSV()
enhanced = importCSV()
list = []
t = open("removed.txt", "w")
d = open("save.txt", "w")
dNoYear = open("saveNo.txt", "w")
noEnhanced = open("noEnhanced.txt", "w")
noEnhancedYear = open("noEnhancedYear.txt", "w")
#comparing [x][0], is comparing names
x = 0
y = 0
while(x < len(basic)):
    z = 0
    a = 0
    boo = False
    while(z < x):
        if(basic[x][0] == basic[z][0]):
            t.write(basic[x][0] + '\n')
            print('REMOVED ' + a.__str__() + basic[x][0])
            a = a + 1
            x = x + 1
            z = -1
        z = z + 1
    while(y < len(enhanced)):
        if basic[x][0] == enhanced[y][0]:
            print(basic[x][0] + ' ' + enhanced[y][1])
            d.write(basic[x][0] + ' ' + enhanced[y][1].__str__() + '\n')
            dNoYear.write(basic[x][0] + '\n')
            boo = True
        y = y + 1
    if(not boo):
        boo = False
        noEnhanced.write(basic[x][0] + '\n')
        noEnhancedYear.write(basic[x][0] + ' ' + basic[x][1].__str__() + '\n')
    y = 0
    x = x + 1
# comparing [x][1], is comparing years

# comparing [x][2], is comparing city

# comparing [x][3], is comparing State