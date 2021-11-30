 #  Brynn Moncur
       #  CSCI 101 – Section D
       #  Python Lab 2
       #  Reference: zyBooks
       #  Time: 45 minutes

print("Input the five lists of characters to be encrypted.")
list1 = str(input("LIST1> "))
list2 = str(input("LIST2> "))
list3 = str(input("LIST3> "))
list4 = str(input("LIST4> "))
list5 = str(input("LIST5> "))

rotated = list1[-2:]+list1[0:-2]

removed = list2[0:-2]

length = len(list3)
halflength = int(length / 2)
halflist = list3[halflength:]

swapped = list4[0:2]+list4[4]+list4[3]+list4[2]+list4[5:]

print("The encrypted message is:")
print(f'OUTPUT {list5[0:2]} {rotated}{removed}{halflist}{swapped} {list5[2:]}')



