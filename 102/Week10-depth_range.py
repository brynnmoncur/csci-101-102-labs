#  Brynn Moncur
        #  CSCI 102 – Section D
        #  Week 10 Lab
        #  References: TA Seunghoo helped me with writing to a csv file
        #  Time: 60 minutes

import csv

#open the cvs file given
with open('formations.csv', 'r') as formations:
    formations_reader = csv.reader(formations, delimiter=',')

    #debug check real fast
    #gonna keep this in here for reference
    #comment out at end!!!
    lines = []
    for x in formations_reader:
        lines.append(x)
     #passed!
    lines.pop(0)

    #print(lines) #debugging, comment out later

    description_list = ['Depth', 'Start Depth', 'End Depth', 'Difference in Depth', 'Formation']
    #might need this, not sure, but this is the five things we are looking for 
    
    #need to skip the first line and then read only the first element in x and split by -
    big_list = []
    little_list = []
    #put the first description line in the big overall list
    big_list.append(description_list)
    #make little lists for each thing, then append to the big overall list
    #print(big_list) #debug check #passed!

    #print("LOOP TESTING BELOW HERE!") #debugging, comment out later
    
    for y in lines:
            #get original value
            little_list.append(y[0])
            #split the original value around the dash
            #get the two numbers this will yield
            floats_list = y[0].split('-')
            num0 = float(floats_list[0])
            num1 = float(floats_list[1])
            if num0 == int(num0):
                little_list.append(f"{float(num0):.1f}")
            else:
                little_list.append(num0)
            if num1 == int(num1):
                little_list.append(f"{float(num1):.1f}")
            else:
                little_list.append(num1)
            #calculate the difference in depth
            difference = float(floats_list[1]) - float(floats_list[0])
            little_list.append(f"{difference:.2f}")
            #now get the name, which is the second element in the original lists
            little_list.append(y[1])
            #now add everything we have done so far to the big overall list
            big_list.append(little_list)
            #reset the little list so we don't get duplicates
            little_list = []

            #ADD IF ELSE STATEMENT TO GET PROPER DECIMAL PLACES WHEN APPENDING

    #print(big_list) #debugging, comment out

with open('formations_parsed.csv', 'w', newline = "") as outfile:
    csvwriter = csv.writer(outfile, delimiter = ",")
    for b in big_list:
        csvwriter.write(b)

            

    
