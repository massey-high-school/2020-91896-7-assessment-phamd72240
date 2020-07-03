calculation_history = [['Area', 1.0], ['Perimeter', 0.75]]

# Sort by measurement...
calculation_history.sort(key=lambda x: x[1], reverse=1)

# Output
print("**** Items by measurement <highest to lowest> *******")
for item in calculation_history:
    print("{}: {:.2f} m".format(item[0], item[1]))

print()

# sort alphabetically
calculation_history.sort(key=lambda x: x[0])

print("***** Items <Alphabetical> *******")
for item in calculation_history:
    print("{}: {:.2f} m".format(item[0], item[1]))

