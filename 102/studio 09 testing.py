# Brynn Moncur
# CSCI 102 Section D
# Python-BasicFileOutput

input_string = str(input())
tokens = input_string.split(',')
f = open('output.txt', 'w')

i = int()
while i < len(tokens):
    f.write(tokens[i])
