 #  Brynn Moncur
        #  CSCI 101 - Section C
        #  Python Lab 8
        #  References: https://www.w3schools.com/python/ref_random_choice.asp
        #  Time: 45 minutes

import random

allList = []
nonuniqueList = []
kevinList = []
stacyList = []
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

print("Welcome to String Game!")
print("Would you like to provide your own string or generate a random one? (1 or 2)")
userChoice = int(input())
if userChoice != 1 and userChoice != 2:
    print("Error! Try again with a valid number")

elif userChoice == 1:
    print("Enter a string for the game:")
    chosenString = str(input("STRING> "))

elif userChoice == 2:
    i = 0
    chosenString = str()
    randomChar = ''
    print("Enter a number to initialize the random generator:")
    inputSeed = str(input("SEED> "))
    rando = random.Random(inputSeed)
    while i < 6:
        randomChar = (rando.choice(alphabet))
        chosenString += randomChar
        i += 1
    print(chosenString)

    
for i in range(len(chosenString)+1):
    for j in range(i+1, len(chosenString)+1):
        if chosenString[i:j] not in allList:
            allList.append(chosenString[i:j])
        nonuniqueList.append(chosenString[i:j])

for b in allList:
    if (b[0] != 'A' and b[0] != 'E' and b[0] != 'I' and b[0] != 'O' and b[0] != 'U'):
        kevinList.append(b)
    else:
        stacyList.append(b)

kevinPoints = 0
stacyPoints = 0
winner = str()

for k in kevinList:
    kevinPoints += nonuniqueList.count(k)
for s in stacyList:
    stacyPoints += nonuniqueList.count(s)

print(f"With the string {chosenString}, Kevin's score is {kevinPoints} and Stacy's score is {stacyPoints}")
if kevinPoints > stacyPoints:
    print("Kevin wins!")
    winner = "Kevin"
elif stacyPoints > kevinPoints:
    print("Stacy wins!")
    winner = "Stacy"
elif stacyPoints == kevinPoints:
    print("It's a tie!")
    winner = "Draw"

print(f"OUTPUT {kevinPoints}")
print(f"OUTPUT {stacyPoints}")
print(f"OUTPUT {winner}")
