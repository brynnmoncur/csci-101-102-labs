 #  Brynn Moncur
        #  CSCI 102 – Section D
        #  Week 11 Lab
        #  References: https://www.kite.com/python/answers/how-to-specify-the-number-of-decimal-places-in-python for decimal places
        #  Time: 25 minutes



def print_output(output_string):
    print(f"OUTPUT {output_string}")

print_output("Hello World")

def triangle_hypotenuse(leg1, leg2):
    hypotenuse = ((float(leg1))**2  + (float(leg2))**2)**(1/2)
    return print_output(f"{hypotenuse:.2f}")

triangle_hypotenuse(3,4)
triangle_hypotenuse(4.2,7.8)


def feet_to_meters(num_feet):
    num_meters = float(num_feet) * 0.3048
    return print_output(f"{num_meters:.4f}")    


feet_to_meters(10)

def polar_coords(x_value, y_value):
    import math
    radius = ((x_value ** 2) + (y_value ** 2)) ** (1/2)
    theta = math.degrees(math.atan(y_value/x_value))
    return print_output(f"r: {radius:.2f}"), print_output(f"theta: {theta:.2f}")

polar_coords(12,5)

def dollars_to_euros(cost_dollars):
    import math
    cost_euros = float(cost_dollars) * 0.86
    rounded_val = round(cost_euros, 2)
    return print_output(f"{rounded_val:.2f}")

#ASK ABOUT ROUNDING DOWN IN ALL CASES WITH DECIMAL VALUES

dollars_to_euros(10)
