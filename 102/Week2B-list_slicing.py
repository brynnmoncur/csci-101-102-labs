#   Brynn Moncur
        #   ​CSCI 102 – Section D
        #   Week 2 - Lab B - List Slicing
        #   References: N/A
        #   Time: 15 minutes

the_str = input("Enter your string:")
print(f'STRING> {the_str}')

print("Enter four numbers to slice the string")
numA = int(input('A>'))
numA = numA + 1
numB = int(input('B>'))
numC = int(input('C>'))
numC = numC + 1
numD = int(input('D>'))

print("OUTPUT", the_str[numA:numB], the_str[numC:numD])


