 #   Brynn Moncur
        #   ​CSCI 101 – Section C
        #   Python Lab 4
        #   References: 
        #   Time: 30 minutes

row0 = str(input("ROW0> "))
row1 = str(input("ROW1> "))
row2 = str(input("ROW2> "))
outcome = str()

# HORIZONTAL WINS
if row0 == "XXX":
    outcome = "X"
elif row0 == "OOO":
    outcome = "O" 
elif row1 == "XXX":
    outcome = "X"
elif row1 == "OOO":
    outcome = "O"
elif row2 == "XXX":
    outcome = "X"
elif row2 == "OOO":
    outcome = "O"
# VERTICAL WINS
elif row0[0] == "X" and row1[0] == "X" and row2[0] == "X":
    outcome = "X"
elif row0[1] == "X" and row1[1] == "X" and row2[1] == "X":
    outcome = "X"
elif row0[2] == "X" and row1[2] == "X" and row2[2] == "X":
    outcome = "X"
elif row0[0] == "O" and row1[0] == "O" and row2[0] == "O":
    outcome = "O"
elif row0[1] == "O" and row1[1] == "O" and row2[1] == "O":
    outcome = "O"
elif row0[2] == "O" and row1[2] == "O" and row2[2] == "O":
    outcome = "O"
# DIAGONAL WINS
elif row0[0] == "X" and row1[1] == "X" and row2[2] == "X":
    outcome = "X"
elif row0[2] == "X" and row1[1] == "X" and row2[0] == "X":
    outcome = "X"
elif row0[0] == "O" and row1[1] == "O" and row2[2] == "O":
    outcome = "O"
elif row0[2] == "O" and row1[1] == "O" and row2[0] == "O":
    outcome = "O"
# NO ONE WINS
else:
    outcome = "N"

print(f"OUTPUT {outcome}")
    
    
    
