# Get numbers from the user, separated by spaces
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Create a lambda function to check whether a number is even
is_even = lambda num: num % 2 == 0

# Select even numbers and calculate their squares using list comprehension
squares = [num * num for num in numbers if is_even(num)]

# Display the squares of even numbers
print("Squares of even numbers:", squares)