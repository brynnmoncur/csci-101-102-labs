 #  Brynn Moncur
        #  CSCI 101 – SectionC
        #  Week 11 Lab
        #  References:
        #  Time: 25 minutes

import csv

def read_csv(csv_name):
    with open(csv_name, 'r', encoding='utf-8') as csv_file:
        csv_file_reader = csv.reader(csv_file, delimiter=',')
        csv_rows = []
        for x in csv_file_reader:
            csv_rows.append(x)
        return csv_rows

def stops_by_race(csv_rows, race):
    counter = int(0)
    if race == "ALL":
        counter = -1
        for a in csv_rows:
            counter += 1
            
    elif race == "white":
        for a in csv_rows:
            if a[8] == "white":
                counter += 1

    elif race ==  "asian/pacific islander":
        for a in csv_rows:
            if a[8] == "asian/pacific islander":
                counter += 1

    elif race == "hispanic":
        for a in csv_rows:
            if a[8] == "hispanic":
                counter += 1

    elif race == "black":
        for a in csv_rows:
            if a[8] == "black":
                counter += 1

    return counter



def stops_by_sex(csv_rows, gender):
    counter = int(0)
    counter = int(0)
    if gender == "ALL":
        counter = -1
        for a in csv_rows:
            counter += 1
            
    elif gender == "female":
        for a in csv_rows:
            if a[9] == "female":
                counter += 1

    elif gender ==  "male":
        for a in csv_rows:
            if a[9] == "male":
                counter += 1

    elif gender ==  "NA":
        for a in csv_rows:
            if a[9] == "NA":
                counter += 1

    return counter


rows = read_csv("aurora_police.csv")
print(stops_by_race(rows, "white"))
print(stops_by_race(rows, "black"))
print(stops_by_race(rows, "ALL"))


