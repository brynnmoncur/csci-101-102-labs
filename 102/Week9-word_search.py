    # Brynn Moncur
        # CSCI 102 – Section D
        # Week 9A - Word Search
        # References:
        # Time: 25 minutes

dictionaryFile = open('dictionary.txt')
dictionaryList = dictionaryFile.readlines()
dictionaryFile.close()

print("Enter the length of the words to find:")
wordLength = int(input("LENGTH>"))
print("Enter the seed to use:")
seed = input("SEED>")

#making a list of words of the specific length we want:
wordCounter = 0
wordLengthList = []

for word in dictionaryList:
    if len(word) == wordLength+1:
        wordLengthList.append(word)
        wordCounter += 1

#do word length
print(f"The number of words with length {wordLength} is:")
print(f"OUTPUT {wordCounter}")

#account for 0 case
if wordCounter == 0:
    print(f"There are no words of length {wordLength} in the dictionary.")
    print("OUTPUT None")
    
#all non-zero cases
else:
    print(f"Here is one random word with length {wordLength}:")

#random word generator: generate a random number, pick the word at that index
    import random
    random.seed(seed)
    for j in range(0,1):
        randomWord = random.choice(wordLengthList)
    print(f"OUTPUT {randomWord}")

