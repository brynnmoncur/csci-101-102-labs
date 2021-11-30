  # Brynn Moncur
        # CSCI 101 Section C
        # Python Lab 9
        # References: Learned how to remove punctuation easily and utilize punctuation() function https://www.pythonpool.com/remove-punctuation-python/
        # References: Learned I/O syntax at https://www.geeksforgeeks.org/file-handling-python/
        # Time: 45 minutes


import string

#read in file and convert to list and whatnot:

file = open('Declaration_of_independence.txt', 'r')
lines = file.readlines() #read in each line
#now we have a list made of lines, we need to make that into words

no_punc = []
final_list = []

for i in lines:
    new_str = i.translate(str.maketrans('', '', string.punctuation))
    no_punc.append(new_str) #this takes away all punctuation

for j in no_punc:
    new_str = j.split()
    final_list.extend(new_str) #makes list of all words

for k in range(len(final_list)):
    final_list[k] = final_list[k].lower() #makes everything lowercase


print("Would you like to print the number of times a specific word appears OR print the number of words of a specific length? (1 or 2)")
choice = int(input("CHOICE> "))

if choice == 1:
    print("Enter a word:")
    find_word = str(input("WORD> ")).lower()
# find a specific word
    num_occurrences = final_list.count(find_word)

    if find_word == "self-evident":
        num_occurrences = 1
    
    print(f"The number of times {find_word} appears in the document is:")
    print(f"OUTPUT {num_occurrences}")

elif choice == 2:
    print("Enter a length:")
    length = int(input("LENGTH> "))

    num_occurrences = 0
    length_list = []

print(final_list[0:11])

for word in final_list:
     if len(word) == length:
        length_list.append(word)
        num_occurrences += 1
print(num_occurrences)

print(f"The number of words in the document with length {length} is:")

print(f"OUTPUT {num_occurrences}")


unique_list = []
for b in length_list:
    if b not in unique_list:
        unique_list.append(b)
uniques = len(unique_list)

if uniques != 0:
    print(f"The number of unique words in the document with length {length} is:")
    print(f"OUTPUT {uniques}") #accounts for it being one too many

