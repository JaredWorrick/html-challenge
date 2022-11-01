# Creates a variable with a string "Frankfurter"
title = "Frankfurter"

# Creates a variable with an integer 80
years = 80

# Creates a variable with the boolean value of True
expert_status = True

# Prints a statement adding the variable
print("Nick is a professional " + title)

# Convert the integer years into a string and prints
print("He has been coding for " + str(years) + " years")

# Converts a boolean into a string and prints
print("Expert status: " + str(expert_status))

# An f-string accepts all data types without conversion
print(f"Expert status: {expert_status}")

### Instructor: str.format(*args) creates a easily readable template into which words are injected:
### I find this syntax, personally, to be a lot more readable than f-strings, but both are widely used
print("Nick is a professional {} who has been coding for {} years and his expert status is {}".format(title,years,expert_status))