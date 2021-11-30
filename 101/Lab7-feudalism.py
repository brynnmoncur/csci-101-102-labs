 # Brynn Moncur
        # CSCI 101 – Section B
        # Python Lab 7: Feudalism
        # References: Looked up what a lambda function was
        # References: Used zybooks for list splitting
        # References: Nested list formatting
        # References: researching more detail on sorting because I couldn't figure out how to use the one in the hints
        # Time: 4 hours

#input number of people to sort, p<=100

print("Input number of people to sort:")
num_people = int(input("NUM_PEOPLE> "))

#now check to make sure that they have entered a valid value

if num_people > 100:
    print("Sorry, that is an invalid value. Please restart the program and try again with a valid value.")

#now make a for loop to read in the information

i = int(0)
person_list = []
person_info = str()

while i < num_people:
    person_info = str(input(f"PERSON{i}> "))
    person_list.append(person_info)
    i += 1

#we now have our list of information
#DEBUG CHECK: print the list
#print(person_list)
#DEBUG CHECK PASSED

#now we need to split the list into names and classes
    #NOTE: might be beneficial to use .count to count the amount of uppers/middles/lowers

#split the list into names and classes

split_list = []
for i in person_list:
    split_list.append(i.split(': '))

#print(f"split list: {split_list}") #comment this out later
#print(f"person list: {person_list}") #comment this out later

#the list is split into nested lists with the name and class in each sub-list

#first let's count how many elements there are in each classification:
#the list is sorted like [[NAME, CLASS], [NAME, CLASS]], so we need to isolate class
#and count the terms that are separated by '-'

name_list = []
class_list = []
class_list = [i[1] for i in split_list]
name_list = [i[0] for i in split_list]

#print(f"name list: {name_list}") #comment this out later
#print(f"class list: {class_list}") #comment this out later

base_counter = 0
new_counter = 0
purgatory_list = []
counter_list = []

for i in class_list:
    purgatory_list.append(i.split(' '))
    
for k in purgatory_list:
    k.pop(1)
    counter_list.append(k[0].split('-'))

for j in counter_list:
        new_counter = len(j)
        if new_counter >= base_counter:
            base_counter = new_counter

#print(f"counter list: {counter_list}") #comment this out later
#print(base_counter) #comment this out later

#now we know the amount of terms so we can fill in with "middle"s where necessary

#what we need to do now: we need to find the length of each person's class, we need to determine if it is less than or equal to the max number we just determined, we need to convert the number
#into the integer values written on my pseudocode paper, and then we need to add middle(or 2) for each space that the term is less than the max.
#we need to work with counterlist

length_difference = int()


for i in range(len(counter_list)):
    if len(counter_list[i]) < base_counter:
        length_difference = base_counter - len(counter_list[i])
        for k in range(length_difference):
            counter_list[i].insert(0, 'middle')
            
#print(f"updated counter list: {counter_list}") #comment out later
#MIGHT NEED TO CHANGE ORDER OF MIDDLE AND ORIGINAL STATEMENT IF GRADESCOPE GETS PISSY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#we now have our lists of equal length
#now we need to take each list and convert each term into an integer and add them

upper_counter = int(0)
middle_counter = int(0)
lower_counter = int(0)
points_list = []
points = int(0)


for f in counter_list:
    #print(f)
    for k in f:
        if k == "upper":
            upper_counter += 1
        elif k == "middle":
            middle_counter += 1
        elif k == "lower":
            lower_counter += 1
        points = (upper_counter * 3) + (middle_counter * 2) + (lower_counter)
        #replace all the uppers and middles and lowers with the points count now
    points_list.append(points)
    upper_counter = middle_counter = lower_counter = 0

#print(f"points list: {points_list}") #comment this out later

#now we need to combine points list and names list!!!

final_list = []
for i in range(len(name_list)):
    final_list.append([name_list[i], points_list[i]])

#print(f"final list: {final_list}") #comment this out later

#sorted_by_class_then_name = sorted(final_list, key=lambda person: (person[1], person[0]), reverse=True)
#print("")
#print(sorted_by_class_then_name) #comment this out later
# this didn't work. we goin rogue


final_list = sorted(final_list, key=lambda person: (person[0]))
final_list = sorted(final_list, key=lambda person: (person[1]), reverse=True)

#sorted_points = sorted(final_list, key=lambda person: (person[1]), reverse=True)
#print("") #comment this out later
#print(sorted_points) #comment this out later

print(" ")
print("After sorting, the list from highest to lowest is as follows:")

for i in final_list:
    print(f"OUTPUT> {i[0]}")
    

            
        
        







                
        
    

