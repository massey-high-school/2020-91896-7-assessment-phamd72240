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

# Asks for height and width
base = num_check("Base: ", float)
height = num_check("Height: ", float)
side = num_check("Side: ", float)
# Find area
area = base * height
print("Area:", area)
# Find perimeter
perimeter = (side + base) * 2
print("Perimeter: ", perimeter)
