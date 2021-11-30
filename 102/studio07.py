
string1 = str(input())

evenlist = []
oddlist =[]

list1 = string1.split(",")


for i in list1:
    if int(i) % 2 == 0:
        evenlist.append(int(i))
    elif int(i) % 2 == 1:
        oddlist.append(int(i))

complete_list = evenlist + oddlist
print(complete_list)
        
