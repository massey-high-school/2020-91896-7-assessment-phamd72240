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

# Asks for side
side = num_check("Side: ", float)
# Find area
area = side * side
print("Area:", area)
# Find perimeter
perimeter = side * 4
print("Perimeter: ", perimeter)

