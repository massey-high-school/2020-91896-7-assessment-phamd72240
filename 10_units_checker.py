def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("sorry that is not a valid response. Please units between cm, mm or m")


# Asks user for prefered units
prefered_units = ["cm","m","mm"]
units = string_checker("Please units your units: cm, mm or m", prefered_units)
print(units)


