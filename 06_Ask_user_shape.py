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

        print("sorry that is not a valid response")

# Asks user for prefered shape
prefered_shape = ["rectangle","triangle","circle","square"]
shape = string_checker("What shape do you want? ", prefered_shape)
print(shape)

