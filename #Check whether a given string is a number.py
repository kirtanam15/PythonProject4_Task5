#Check whether a given string is a number
# Create a lambda function to check whether a string contains digits only
is_number = lambda text: text.isdigit()

# Get input from the user
value = input("Enter a string: ")

# Check and display the result
if is_number(value):
    print("The string contains only numbers")
else:
    print("The string is not a number")


