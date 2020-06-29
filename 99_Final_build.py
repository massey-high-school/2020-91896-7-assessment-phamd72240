# Import goes here...
import math
# Number Checking Function
def num_check(question, type):
    if type == float:
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

# String Checking Function
def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("sorry that is not a valid response. Please choose"
              " triangle, square, circle, rectangle or parallelogram.")

# Asks user for prefered shape
prefered_shape = ["rectangle","triangle","circle","square","parallelogram"]
shape = string_checker("Please choose between: rectangle, triangle, circle, square, parallelogram.", prefered_shape)
print(shape)

# Main Routine goes here...
if shape == "rectangle":
    # Asks for height and width
    length = num_check("Length: ", float)
    width = num_check("Width: ", float)
    # Find area
    area = length * width
    print("Area:", area)
    # Find perimeter
    perimeter = (length + width) * 2
    print("Perimeter: ", perimeter)

if shape == "triangle":
    # Asks for height and base
    base = num_check("Base: ", float)
    height = num_check("Height: ", float)
    # Asks for area
    area = (base * height) / 2
    print("Area: ", area)
    # Asks for 3 sides
    side_one = num_check("Side: ", float)
    side_two = num_check("Side: ", float)
    side_three = num_check("Side: ", float)
    # Asks for perimeter
    perimeter = side_one + side_two + side_three
    print("Perimeter: ", perimeter)

if shape == "circle":
    # Asks for Radius and diameter
    radius = num_check("Radius: ", float)
    # Find area
    area = radius * radius * math.pi
    print("Area:", area)
    # Find Circumference/Perimeter
    circumference = radius * 2 * math.pi
    print("Circumference: ", circumference)

if shape == "square":
    # Asks for side
    side = num_check("Side: ", float)
    # Find area
    area = side * side
    print("Area:", area)
    # Find perimeter
    perimeter = side * 4
    print("Perimeter: ", perimeter)

if shape == "parallelogram":
    # Asks for height and width
    base = num_check("Base: ", float)
    height = num_check("Height: ", float)
    length = num_check("Length: ", float)
    width = num_check("Width: ", float)
    # Find area
    area = base * height
    print("Area:", area)
    # Find perimeter
    perimeter = (length + width) * 2
    print("Perimeter: ", perimeter)
