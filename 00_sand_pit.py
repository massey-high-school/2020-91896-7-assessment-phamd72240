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
length = num_check("Length: ", float)
width = num_check("Width: ", float)
# Find area
area = length * width
print("Area:", area)
# Find perimeter
perimeter = (length + width) * 2
print("Perimeter: ", perimeter)

# Initialise Lists
shape_size = []
measurement = []

# Get inputs and add to item_cost list
shape = ""
shape_size = []
shape = area

# Get the cost
size = perimeter

# Add item name and cost to the 'item' list
shape_size.append(shape)
shape_size.append(size)

# Add item to the expense list
measurement.append(shape_size)

print(measurement)

# Calculation History
calculation_history = [['Area', shape], ['Perimeter', size]]

# Sort by measurement...
calculation_history.sort(key=lambda x: x[1], reverse=1)

# Output
print("**** Items by measurement <highest to lowest> *******")
for item in calculation_history:
    print("{}: {:.2f} ".format(item[0], item[1]))

print()

# sort alphabetically
calculation_history.sort(key=lambda x: x[0])

print("***** Items <Alphabetical> *******")
for item in calculation_history:
    print("{}: {:.2f} ".format(item[0], item[1]))

