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

# Asks for height and base
base = num_check("Base: ", int)
height = num_check("Height: ", int)
# Asks for area
area = base * height
print("Area: ", area)
# Asks for 3 sides
side_one = num_check("Side: ", int)
side_two = num_check("Side: ", int)
side_three = num_check("Side: ", int)
# Asks for perimeter
perimeter = side_one + side_two + side_three
print("Perimeter: ", perimeter)
