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

# Main Function goes here...

# Asks for height and base
base = num_check("Base: ", float)
height = num_check("Height: ", float)
# Asks for area
area = base * height
print("Area: ", area)
# Asks for 3 sides
side_one = num_check("Side: ", float)
side_two = num_check("Side: ", float)
side_three = num_check("Side: ", float)
# Asks for perimeter
perimeter = side_one + side_two + side_three
print("Perimeter: ", perimeter)
