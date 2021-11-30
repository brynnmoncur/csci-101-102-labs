# Brynn
# CSCI102 - Section D
# Python-CountSymbolsAndChars

string = str(input())

letter_count = int()
number_count = int()
symbol_count = int()

for i in string:
    if i.isalpha():
        letter_count += 1
    elif i.isdigit():
        number_count += 1
    else:
        symbol_count += 1

print(f"Total counts of chars, digits, and symbols are {letter_count}, {number_count}, and {symbol_count}")    
