# Brynn Moncur
#  CSCI 101 – Section C
#  Python Lab 5
#  References: looked up how to use a try/except statement
#  Time: 90 minutes


# present menu, have user select one of 5 options
print("Welcome to the Binary-Decimal Converter")
#while bool = true, make an infinite loop and then break it if they say no
while True:
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print("Enter an option:")
    print("1. Binary-Decimal Conversion")
    print("2. Decimal-Binary Conversion")
    print("3. Quit")
    option_chose = int(input("OPTION> "))
#CHECKED, WORKS

# IF ELSE STATEMENT 1:
# if number not within 1-3, print error message
# if number in one of these options, do the option:
    if option_chose != 1 and option_chose != 2 and option_chose !=3:
        print("ERROR: Please choose from [1-3]")
        print("OUTPUT ERROR")
    #Continue option: break the massive while true loop, or continue
        print("Would you like to continue (y/n)?")
        continue_option = str(input("CONTINUE> "))
        if continue_option.lower()  == "yes" or continue_option.lower() == "y":
            continue
        elif continue_option.lower() == "no" or continue_option.lower() == "n":
            print("OUTPUT Goodbye!")
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            break
    
# OPTION 1: binary-decimal
#Input the binary number.
    elif option_chose == 1:
        binary_str= str(input("BINARY-STR> "))
#Set a decimal number variable to zero.
        decimal_variable = 0
#Starting with the least significant digit (the rightmost one), multiply the digit by the value of the position (i.e., 2^0 for rightmost bit, 2^1 for bit next to rightmost bit, 2^2 for bit next to that, etc.).
        i = len(binary_str) - 1
        j = 0
        try:
            while i >= 0:
                binary_num = binary_str[i]
                integer_binary_num = int(binary_num) #BREAKS HERE
                position_value = integer_binary_num * (2**j)
#Add the result to your decimal number.
                decimal_variable = decimal_variable + position_value
#Continue doing the previous step until you reach the most significant digit (the leftmost one).
                i -= 1
                j += 1
       
#Output the decimal equivalent of the given binary number.
            print(f"Binary {binary_str} is Decimal {decimal_variable}")
            print(f"OUTPUT {decimal_variable}")
            
        except:
            print("ERROR: Input X is NOT a binary number")
            print("OUTPUT ERROR")

#Continue option: break the massive while true loop, or continue
        print("Would you like to continue (y/n)?")
        continue_option = str(input("CONTINUE> "))
        if continue_option.lower()  == "yes" or continue_option.lower() == "y":
            continue
        elif continue_option.lower() == "no" or continue_option.lower() == "n":
            print("OUTPUT Goodbye!")
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            break
        else:
            break
    

# OPTION 2: decimal-binary
#Input the decimal number.
    elif option_chose == 2:
        try:
            decimal_num = int(input("DECIMAL-STR> "))
#Create an empty string.#Store the remainder when the input number is divided by 2.
            empty_str = str()
#The remainder will be one bit in your binary number. (HINT: use the python operator modulo % to get the remainder.)
            while decimal_num > 0:
                remainder_num = decimal_num % 2 # 6 % 2 = 0
                remainder_num_str = str(remainder_num) # 0 but make it a string yuh
                decimal_num = int(decimal_num / 2)
#Concatenate the remainder value to your string.
                empty_str = empty_str + remainder_num_str #get concenated
#Output the string in reverse order for the binary equivalent of the given decimal number.
            i = len(empty_str) - 1
            reversed_str = str()
            while i >= 0:
                reversed_str += empty_str[i]
                i = i - 1
            print(f"Decimal {decimal_num} is Binary {reversed_str}")
            print(f"OUTPUT {reversed_str}")
        except:
            print("ERROR: Input X is NOT a decimal number")
            print("OUTPUT ERROR")
#Continue option: break the massive while true loop, or continue
        print("Would you like to continue (y/n)?")
        continue_option = str(input("CONTINUE> "))
        if continue_option.lower()  == "yes" or continue_option.lower() == "y":
            continue
        elif continue_option.lower() == "no" or continue_option.lower() == "n":
            print("OUTPUT Goodbye!")
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            break
        else:
            break
#OPTION 3: quit
    elif option_chose == 3:
        print("OUTPUT Goodbye!")
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        break
    
        



        
