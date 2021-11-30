#   Brynn Moncur
        #   ​CSCI 102 – Section D
        #   Week 3 - Lab B - Enhanced Calcuator
        #   References: None
        #   Time: 35 minutes

operand_one = float(0.0)
operand_two = float(0.0)
sum_num = float(0.0)
difference = float(0.0)
product = float(0.0)
quotient = float(0.0)
remainder = float(0.0)


print("Welcome to our Enhanced Calculator!")

print("Input the first operand.")
operand_one = float(input("FIRST>"))
print("Input the second operand.")
operand_two = float(input("SECOND>"))

print("Choose one of the following operations:")
print("1 - addition")
print("2 - subtraction")
print("3 - multiplication")
print("4 - division")
choice = int(input("OPERATION>"))

if choice == 1:
    sum_num = operand_one + operand_two
    print(f'The result of the addition is: {sum_num:.6f}')
    print(f'OUTPUT {sum_num:.6f}')
elif choice == 2:
    difference = operand_one - operand_two
    print(f'The result of the subtraction is: {difference:.6f}')
    print(f'OUTPUT {difference:.6f}')
elif choice == 3:
    product = operand_one * operand_two
    print(f'The result of the multiplication is: {product:.6f}')
    print(f'OUTPUT {product:.6f}')
elif choice == 4:
    quotient = int(operand_one / operand_two)
    remainder = int(operand_one % operand_two)
    print(f'The result of the division is: {quotient} (quotient) and {remainder} (remainder)')
    print(f'OUTPUT {quotient}')
    print(f'OUTPUT {remainder}')

print("Thank you for using our calculator.")
    
    
