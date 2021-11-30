 #   Brynn Moncur
        #   ​CSCI 101 – Section D
        #   Python Lab 3
        #   References: researched how to add leading zeroes using dot operator
        #   Time: 25 minutes

hourTime = int(input("HOURS> "))
minuteTime = int(input("MINUTES> "))

newMinute = minuteTime - 40
if newMinute < 0:
    newMinute = 60 + newMinute
    hourTime = hourTime - 1
    if hourTime < 0:
        hourTime = 24 + hourTime

hourTime2 = str(hourTime).zfill(2)
newMinute2 = str(newMinute).zfill(2)

print(f"OUTPUT {hourTime2} {newMinute2}")
                   
