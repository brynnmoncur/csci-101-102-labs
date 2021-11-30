     #  Brynn Moncur
        #  CSCI 102 – Section C
        #  Week 7 - Lab A - Checkerboard
        #  References: Used website to get more familiar with 2D lists
        #  References: https://snakify.org/en/lessons/two_dimensional_lists_arrays/
        #  Time: 45 minutes

# get rows and columns
print("How many rows does the checkerboard have?")
rows = int(input("ROWS>"))
print("How many columns does the checkerboard have?")
columns = int(input("COLUMNS>"))

#get strings to pattern
print("What are the strings with which to pattern it?")
string1 = str(input("FIRST>"))
string2 = str(input("SECOND>"))

print(f"A checkerboard with {rows} rows, {columns} columns, first string is {string1}, and second string is {string2} is:")

board = []
flatboard = []
# this loop determines the pattern of the two strings
for i in range(rows):
    for j in range(columns):
        if (i+j) % 2 == 0:
            board.append(string1)
        else:
                board.append(string2)
    print(f"OUTPUT {board}")
    #appending the list to the "flat" array variable
    flatboard.append(board)
    #reset board so we maintain the dimensions
    board = []

print("And the 2D array representation is:")
print(f"OUTPUT {flatboard}")
            



      
