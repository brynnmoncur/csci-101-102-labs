  #   Brynn Moncur
        #   ​CSCI 102 – Section D
        #   Week 6 - Lab B - Estimating Square Roots
        #   References: Hunter Belcher helped fix bugs
        #   Time: 50 minutes


print("How many numbers am I estimating John?")
num_count = int(input("COUNT> "))
print("Input each number to estimate.")

num_list = []
new_num = 0

for i in range(num_count):
    new_num = float(input("NUMBER> "))
    num_list.append(new_num)
    i += 1

print("The square roots are as follows:")

# NOW WE GET TO THE ACTUAL CALCULATIONS

initial_guess = 10
iteration_count = 1
better_guess = 0
for num in num_list:
    while True:
        better_guess = (initial_guess + num / initial_guess)/2
        if initial_guess == better_guess:
            break
        iteration_count += 1
        initial_guess = (initial_guess + num / initial_guess)/2
    print(f"OUTPUT After {iteration_count} iterations, {num}^0.5 = {initial_guess:.03f}")
    initial_guess = 10
    iteration_count = 1

