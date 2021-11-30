#   Brynn Moncur
        #   ​CSCI 102 – Section D
        #   Week 4 - Lab A - Receipt Generator
        #   References: 
        #   Time: 25 minutes

companyName = input("Enter company name: ")
companyCityState = input("Enter company city/state: ")
cashierName = input("Enter cashier name: ")

item1 = input("Purchased item 1 name: ")
price1 = float(input("Purchased item 1 price: "))

item2 = input("Purchased item 2 name: ")
price2 = float(input("Purchased item 2 price: "))

item3 = input("Purchased item 3 name: ")
price3 = float(input("Purchased item 3 price: "))

endingMessage = str(input("Enter your favorite ending message: "))

totalCost = price1 + price2 + price3

# OUTPUT


print("        RECEIPT GENERATOR")
print("-----------------------------------")
print(f"    {companyName}")
print(f"    {companyCityState}")
print("===================================")
print(f"    Your cashier was: {cashierName}")
print("    Welcome Valued Customer")
print("===================================")
print("    Item Name       Item Price")
print(" ")
print(f"    {item1}       ${price1}")
print(f"    {item2}       ${price2:.2f}")
print(f"    {item3}       ${price3}")
print(" ")
print("===================================")
print(f"    Total Cost of Order: {totalCost:.2f}")
print("===================================")
print(f"    {endingMessage}")
print("-----------------------------------")



