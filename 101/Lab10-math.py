#  Brynn Moncur
        #  CSCI 101 – Section C
        #  Python Lab 10
        #  References: Used the following site for reading CSV file syntax
        #  References: https://realpython.com/python-csv/
        #  Time: 45 minutes

import csv

print("Enter the name of the file containing the math problems.")
mathfile = str(input("MATHFILE> "))
print("Enter the name of the file in which to store the results.")
outputfile = str(input("OUTPUTFILE> "))

with open(mathfile, 'r') as mathfile:
    mathfile_reader = csv.reader(mathfile, delimiter=',')

    lines = []
    for j in mathfile_reader:
        lines.append(j)

    results = []
    
    for alist in lines: #for list in list
        num_list = []
        operator_list = []
        for element in alist: #for element in that list
            if element.strip('-').isnumeric() == True:
                num_list.append(int(element))
            else:
                operator_list.append(element)
        #print(num_list) #debug, comment out
        #print(operator_list) #debug, comment out

        #NOW WE DO ALL THE ANSWERS <3
        try:
            if operator_list[0] == '+':
                result = (num_list[0] + num_list[1])
            elif operator_list[0] == '-':
                result = (num_list[0] - num_list[1])
            elif operator_list[0] == '*':
                result = (num_list[0] * num_list[1])
            elif operator_list[0] == '/':
                result = (num_list[0] / num_list[1])
        except IndexError as error:
            result = round(num_list[0])
        #print(result) #works yuh #comment out

        for i in range(1, len(operator_list)):
            if operator_list[i] == '+':
                result += num_list[i+1]
            elif operator_list[i] == '-':
                result -= num_list[i+1]
            elif operator_list[i] == '*':
                result *= num_list[i+1]
            elif operator_list[i] == '/':
                result /= num_list[i+1]
        result = round(result)
        results.append(result)

    #print(results)

#would need to do:
#numlist(0) operator(0) numlist(1)
#                   operator(1) numlist(2) operator = i, num = i+1
#                   operator(2) numlist(3)
#                   operator(3) numlist(4)

with open(outputfile, 'w', newline = "") as outputfile:
    csvwriter = csv.writer(outputfile, delimiter = ",")
    csvwriter.writerow(results)
                
            

        
