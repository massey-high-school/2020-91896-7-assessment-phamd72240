# Import goes here...
import math
# Number Checking Function
def num_check(question, type):
    if type == int:
        err_type = "an integer"
    else:
        err_type = "a number"

    error = "Please enter {} that is more than zero".format(err_type)

    valid = False
    while not valid:
        try:
            response = type(input(question))

            if response <= 0:
                print(error)
            else:

                return response

        except ValueError:
            print(error)

# Main Function goes here...

# Asks for Radius and diameter
radius = num_check("Radius: ", int)
diameter = num_check("Diameter: ", int)
radius = diameter / 2
diameter = radius * 2


# Find area
area = radius * radius * math.pi
print("Area:", area)
# Find Circumference/Perimeter
circumference = radius * 2 * math.pi
print("Circumference: ", circumference)