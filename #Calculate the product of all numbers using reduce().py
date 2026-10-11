# Import reduce from the functools module
from functools import reduce

# Get numbers from the user, separated by spaces
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Multiply all numbers using reduce and lambda
product = reduce(lambda a, b: a * b, numbers)

# Display the product of all numbers
print("Product of all numbers:", product)