 # Brynn Moncur
        # CSCI 101 – Section B
        # Python Lab 6: Timber Regrowth
        # References:N/A
        # Time: 30 minutes

print("Input the number of years to print in the reforestation table:")
years = int(input("YEARS>"))
print("The reforestation table is then")
print("Year, # Acres, % of Forest")

uncut_land = int(3000)
reforestation_rate = 1.03
available_land = int(12000)

# pseudo: continuous loop where you multiply acres by 1.03
# then find out what percentage of the forest that is

forest_percentage = uncut_land / available_land * 100
print(f"OUTPUT 0, {uncut_land:.1f}, {forest_percentage:.2f}%")

i = 1
new_acres = 3000.0
while i <= years:
    new_acres = (new_acres * reforestation_rate)
    forest_percentage = (new_acres / 12000 * 100)
    print(f"OUTPUT {i}, {new_acres:.1f}, {forest_percentage:.2f}%")
    i += 1
