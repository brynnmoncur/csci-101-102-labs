#   Brynn Moncur
        #   CSCI 102 – Section D
        #   Week 8 - Lab B - Coming Through a Haystack
        #   References: None
        #   Time: 25 minutes

print("Enter a DNA string s:")
s = str(input("s> "))
print("Enter a substring t:")
t = str(input("t> "))

if len(s) > 1000:
    print("Error: String is longer than 1000 characters")
    print("OUTPUT ERROR")
elif len(t) > 1000:
    print("Error: Substring is longer than 1000 characters")
    print("OUTPUT ERROR")
elif len(t) > len(s):
    print("Error: Substring is longer than DNA string")
    print("OUTPUT ERROR")
else:
    #ALL CODE BELOW HERE NOW

    substring_count = int(0)
    location_list = []
    deletedIndices = 0
    i=0

    while s.find(t) != -1:
        substring_count += 1
        location_list.append(s.find(t)+deletedIndices)
        s = s[s.find(t)+1:]
        deletedIndices = location_list[i]+1
        i+=1

    final_string = str()
    print(f"The total number of substrings found is {substring_count}")
    print(f"OUTPUT {substring_count}")
    print(f"The location of these substrings in s are:", end=" ")
    for j in location_list:
        if j != location_list[-1]:
            final_string += (str(j + 1) + " ")
        else:
            final_string += str(j + 1)
    print(final_string)
    print(f"OUTPUT {final_string}")

        
    
        

    
   
    

        
    
