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

# Asks user for prefered shape
keep_going = ""
while keep_going == "":

    question = input("What shape? ").lower()

    if question == "xxx":
         break
    elif question == "rectangle" or question == "r":
        pass
        # Asks for height and width
        length = num_check("Length: ", int)
        width = num_check("Width: ", int)
        # Find area
        area = length * width
        print("Area:", area)
        # Find perimeter
        perimeter = (length + width) * 2
        print("Perimeter: ", perimeter)

