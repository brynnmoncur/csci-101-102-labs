#   Brynn Moncur
        #   ​CSCI 102 – Section D
        #   Week 2 - Lab A - Simple Calculator
        #   References: N/A
        #   Time: 15 minutes

operand_one = 0.0
operand_two = 0.0
sum = 0.0
difference = 0.0
quotient = 0.0
product = 0.0
remainder = 0.0

print("Input the first operand.")
operand_one = float(input("FIRST>"))
print("Input the second operand.")
operand_two = float(input("SECOND>"))

sum = operand_one + operand_two
difference = operand_one - operand_two
quotient = int(operand_one / operand_two)
product = operand_one * operand_two
remainder = operand_one % operand_two

print(f'The sum of {operand_one} and {operand_two} is {sum:.1f}')
print(f'OUTPUT {sum:.1f}')

print(f'The difference of {operand_one} and {operand_two} is {difference:.1f}')
print(f'OUTPUT {difference:.1f}')

print(f'The product of {operand_one} and {operand_two} is {product:.1f}')
print(f'OUTPUT {product:.1f}')

print(f'The quotient of {operand_one} and {operand_two} is {quotient}')
print(f'OUTPUT {quotient}')

print(f'The remainder of {operand_one} and {operand_two} is {remainder:.2f}')
print(f'OUTPUT {remainder:.2f}')




      


