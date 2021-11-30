  #   Brynn Moncur
        #   ​CSCI 102 – Section D
        #   Week 5 - Lab A - Tally for Kids
        #   References: looked up how to typecast
        #   Time: 30 minutes


print("Enter values to add. Enter quit when done.")

num = input("NUMBER> ")
numSum = 0
numInputs = 0

while num != 'quit':
    numSum = int(numSum) + int(num)
    num = input("NUMBER> ")
    numInputs = numInputs + 1

print(f"The addition of the {numInputs} numbers entered is:")
print(f"OUTPUT {numInputs} numbers")
print(f"OUTPUT {numSum} total")





    
