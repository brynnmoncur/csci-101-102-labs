   #   Brynn Moncur
        #   CSCI 102 – Section D
        #   Week 8 - Lab A - Rolling a Die
        #   References: Class video on random number generation
        #   Time: 25 minutes

print("Input the number of sides of the die:")
sides = int(input("SIDES> "))
print("Input the number of rolls to make:")
rolls = int(input("ROLLS> "))
print("Input the seed for the random number generator:")
die_seed = int(input("SEED> "))
print(" ")
print(f"Your {rolls} rolls of a {sides}-sided die follow:")

#now we make the random number generator

import random
random.seed(die_seed)

i = int(0)
roll_list = []
while i < rolls:
    rand_num = random.randint(1, sides)
    roll_list.append(rand_num)
    i += 1

#print(roll_list) #works

for j in range(sides):
    counter = roll_list.count(j + 1)
    print(f"OUTPUT {j+1} occurred {counter} times")
    
    
            
    
    
