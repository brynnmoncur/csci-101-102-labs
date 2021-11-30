   #   Brynn Moncur
        #   ​CSCI 102 – Section D
        #   Week 6 - Lab A - List of Multiples
        #   References: N/A
        #   Time: 20 minutes

print("Enter the number to create multiples for.")
multiplier = int(input("NUMBER> ")) #number to find multiples of
print("Enter the maximum index of the list.")
index = int(input("INDEX> "))

multiples_list = []
new_multiplier = 0
i = 0

while i <= index: #gets list of the multipliers
    new_multiplier = (new_multiplier + multiplier)
    multiples_list.append(new_multiplier)
    i = i + 1

print("Your list of multiples is as follows:")
print("OUTPUT", multiples_list)
    
    



