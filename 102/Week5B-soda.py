#   Brynn Moncur
        #   ​CSCI 102 – Section D
        #   Week 5 - Lab B - Soda Sprinter
        #   References:
        #   Time: 25 minutes

print("Enter the number of empty bottles in Blaster's possession at the start of the day.")
emptiesbottles = int(input("EMPTIES> "))
print("Enter the number of empty bottles that Blaster found during the day.")
foundbottles = int(input("FOUND> "))
print("Enter the number of empty soda bottles required to buy a new soda.")
costbottles = int(input("COST> "))

totalbottles = emptiesbottles + foundbottles
bottlesbought = 0

while totalbottles >= costbottles:
    drankbottles = int(totalbottles / costbottles)
    remainder = totalbottles % costbottles
    totalbottles = remainder + drankbottles
    bottlesbought += drankbottles
    

print("The total number of sodas that Blaster drank is:")
print(f"OUTPUT {bottlesbought}")
