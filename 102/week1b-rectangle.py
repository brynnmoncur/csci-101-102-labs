#   Brynn
#   ​CSCI 102 – Section D
#   Week 1 - Part B
#   References:  googling python math functions
#   Time: 60 minutes

print("Input the total length of fencing available (in yards.)")
a = int(input())
print("LENGTH>", a)
print("The maximum rectangular area that can be bound (in feet) is:")
b = int(a * 3)
c = float(b/4)
d = c**2
d = round(d, 1)
print("OUTPUT", d)

