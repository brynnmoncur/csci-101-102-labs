# Brynn Moncur, Katie Greene, Callie McCaffery
# CSCI102 - Section D
# Python-CatYears

human_age = int(input())
cat_age = 0

if human_age < 0:
    print("Age must be a positive number.")
elif human_age <= 2:
    cat_age = 11 * human_age
elif human_age > 2:
    cat_age = (human_age - 2)*4 + 22

print(f"Cat's age is {cat_age} in cat years.")


    
