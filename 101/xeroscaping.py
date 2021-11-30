#  Brynn Moncur
        #  CSCI 101 – Section C
        #  Create Project
        #  References: https://www.programiz.com/python-programming/methods/string/center for centering strings
        # References: https://www.delftstack.com/howto/python/python-bold-text/ for bold text and other text
        #  Time:

import csv

def user_questions():
    #this function gets all the user info, which is used in determining what wildflowers match the elevation as well as making the usercard.txt
    userinfo = []
    print("What is your name?")
    username = str(input("NAME> "))
    userinfo.append(username)
    print("What elevation do you live at? (Must be >3499 ft)")
    userzone = int(input("ELEVATION> "))
    userinfo.append(userzone)
    print("What is your favorite color? (ROYGBIV please!)")
    usercolor = str(input("COLOR> "))
    userinfo.append(usercolor)
    return userinfo

def continuemenu():
    #this function streamlines the "would you like to continue" process into 3 lines
    print(" ")
    print("❀✿❀✿❀✿ would you like to continue? (Y/N) ❀✿❀✿❀✿")
    continue_choice = str(input("your choice: "))
    if continue_choice == "Y" or continue_choice == "y":
        print(" ")
        print("please select an option from the following menu:".center(18, ' '))
        return True
    else:
        print("❀✿❀✿❀✿ goodbye! ❀✿❀✿❀✿")
        return False
            
############################################################################################### 

#header and menu
print("❀✿❀✿❀✿ welcome to the xeriscape handbook! ❀✿❀✿❀✿ ".center(27, ' '))
print(" ")
print("please select an option from the following menu:".center(18, ' '))
print(" ")
#BUG: centering isn't working. find out why

while True: #this makes the program ongoing until the user specifically chooses to end it

    #BIG MENU LOOP
    print("❀ 1. what is xeriscaping? ❀")
    print("✿ 2. what are the best wildflowers for my location? ✿")
    print("❀ 3. wildflower dictionary ❀")
    print("✿ 4. sources ✿")
    print("❀ 5. end program ❀")

    print(" ")

    user_choice = int(input("your choice: "))
    print(" ")

################################################################################################

    if user_choice == 1: #"what is xeriscaping?" choice
        print(" ")
        print("Xeriscaping is the practice of designing landscapes to reduce or eliminate the need for irrigation [1].")
        print("Xeriscaping has a wide variety of benefits!")
        print("First of all, it helps you AND the environment by conserving water. You save money on irrigation, and help alleviate drought conditions!")
        print("Secondly, there is little to no upkeep required! Xeriscaped lawns are designed to be low maintenance, and beautiful!")
        print("Finally, xeriscaped lawns allow you to do your part in preserving your environment. By using native plants, you support the local ecosystem!")
        print("Explore the rest of this program to find out the best plants in your area to xeriscape your lawn with!")
        print(" ")
#continue menu, copy and paste this for all choices :)
        choice = continuemenu()
        if choice == False:
            break
        continue
        

##############################################################################################


    elif user_choice == 2:
        userinfo = user_questions() #this will ask all of the necessary questions
        print(" ")
        elevation_num = userinfo[1] #second question asked to user
        user_elevation_zone = 'yuh' #initialize to random string
        user_flowers = []
        if elevation_num < 3500:
            print("Sorry, we can't help you!")
            break;

        #the following elif statements determine the elevation and read in the corresponding file with those particular plants
        
        elif elevation_num >= 3500 and elevation_num < 6500:
            user_elevation_zone = 'Plains'
            userinfo.append(user_elevation_zone)

            with open('plains_wildflowers.csv', 'r') as plains:
                plains_reader = csv.reader(plains, delimiter=',')
                plains_wildflowers = []
                for x in plains_reader:
                    plains_wildflowers.append(x)

            print("Here are the best wildflowers for your location: ")
            for a in plains_wildflowers:
                print(a[0]) #only print the first index as that is the name of the wildflower. we don't need all the other info just yet
                user_flowers.append(a)

        #everything below this is the exact same as the one above, just copied
        
            
        elif elevation_num >= 6500 and elevation_num < 8000:
            user_elevation_zone = 'Foothills'
            userinfo.append(user_elevation_zone)

            with open('foothills_wildflowers.csv', 'r') as foothills:
                foothills_reader = csv.reader(foothills, delimiter=',')
                foothills_wildflowers = []
                for x in foothills_reader:
                    foothills_wildflowers.append(x)

            print("Here are the best wildflowers for your location: ")
            for a in foothills_wildflowers:
                print(a[0])
                user_flowers.append(a)
                    
        elif elevation_num >= 8000 and elevation_num < 10000:
            user_elevation_zone = 'Montane'
            userinfo.append(user_elevation_zone)

            with open('montane_wildflowers.csv', 'r') as montane:
                montane_reader = csv.reader(montane, delimiter=',')
                montane_wildflowers = []
                for x in montane_reader:
                    montane_wildflowers.append(x)

            print("Here are the best wildflowers for your location: ")
            for a in montane_wildflowers:
                print(a[0])
                user_flowers.append(a)
            
        elif elevation_num >= 10000 and elevation_num < 11500:
            user_elevation_zone = 'Subalpine'
            userinfo.append(user_elevation_zone)

            with open('subalpine_wildflowers.csv', 'r') as subalpine:
                subalpine_reader = csv.reader(subalpine, delimiter=',')
                subalpine_wildflowers = []
                for x in subalpine_reader:
                    subalpine_wildflowers.append(x)

            print("Here are the best wildflowers for your location: ")
            for a in subalpine_wildflowers:
                print(a[0])
                user_flowers.append(a)
            
        elif elevation_num >= 11500:
            user_elevation_zone = 'Alpine'
            userinfo.append(user_elevation_zone)

            with open('alpine_wildflowers.csv', 'r') as alpine:
                alpine_reader = csv.reader(alpine, delimiter=',')
                alpine_wildflowers = []
                for x in alpine_reader:
                    alpine_wildflowers.append(x)

            print("Here are the best wildflowers for your location: ")
            for a in alpine_wildflowers:
                print(a[0])
                user_flowers.append(a)


        #now we will create usercard.txt

        is_fav_color = False #this boolean will be used for personalization later on
        fav_color_index = int(0)
        b = int(0)
        f = open('usercard.txt', 'w')  # Open file
        f.write(f"your name: {userinfo[0]}\n")
        f.write(f"your elevation zone: {userinfo[3]}\n")
        f.write(f"your favorite color: {userinfo[2]}\n")
        f.write("the best plants for you: \n")
        for a in user_flowers:
            
            f.write(f"  {a[0]}\n")
            f.write(f"     SCIENTIFIC NAME> {a[1]}\n")
            f.write(f"     COLOR> {a[2]}\n")
            f.write(f"     SUN OR SHADE?> {a[3]}\n")
            fav_color = userinfo[2].lower() #make lowercase to check
            flower_color = a[2].lower() #same as above
            if fav_color[0] == flower_color[0]: #compare the lowercase first characters of each -- this assumes if something is misspelled that at least the first letter will be correct. if it is not, no personalization will occur)
                is_fav_color = True
                fav_color_index = b
            b += 1
        if is_fav_color == True:
            f.write(f"based on the information you gave us, we think your favorite flower will be: {user_flowers[fav_color_index][0]}\n") #this only runs if fav color is one of the options and contains the correct first character
        f.close()  # Close the file
            
        print(" ")

        print("Want to know more detail? We just made you a personalized reference card with all of the wildflower's information!")
        print("Check your files for 'usercard.txt'. Bring it with you next time you go to the garden center!")
        print("All of the information found in the card is also in the dictionary menu option!")
    
        
        choice = continuemenu()
        
        if choice == False:
            break

################################################################################################

    elif user_choice == 3:
        with open('wildflower_dictionary.csv', 'r') as dictionary: #open up the csv file that contains ALL the flowers in alphabetical order
            dictionary_reader = csv.reader(dictionary, delimiter=',')
            dictionary_list = []
            for x in dictionary_reader:
                dictionary_list.append(x)

            print("❀✿❀✿❀✿ wildflower dictionary ❀✿❀✿❀✿")
            print(" ")

            a = int(1)
            for b in dictionary_list: #prints out all of the wildflowers and their information
                print(f"{a}. {b[0]}")
                print(f"   SCIENTIFIC NAME > {b[1]}")
                print(f"   COLOR> {b[2]}")
                print(f"   SUN OR SHADE?> {b[3]}")
                print(" ")
                a += 1

        choice = continuemenu()
        if choice == False:
            break
                

################################################################################################


    elif user_choice == 4:
        print("[1] “Xeriscaping,” National Geographic Society, 09-Oct-2012. [Online]. Available: https://www.nationalgeographic.org/encyclopedia/xeriscaping/. [Accessed: 06-Nov-2021]. ")
        print("[2] “Plants & Habitats,” Colorado Native Plant Society, 02-Oct-2021. [Online]. Available: https://conps.org/plants-habitats/. [Accessed: 28-Nov-2021].")

        choice = continuemenu()
        if choice == False:
            break
    

#################################################################################################


    elif user_choice == 5:
        break


##################################################################################################

print(" ")



    
