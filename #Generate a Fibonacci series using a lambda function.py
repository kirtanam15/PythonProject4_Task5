#Generate a Fibonacci series using a lambda function
# Create a lambda function to generate Fibonacci numbers
fibonacci = lambda n: (
    lambda f: f(f, n, 0, 1, [])
)(
    lambda f, n, a, b, result:
        result if n == 0 else f(f, n - 1, b, a + b, result + [a])
)

# Get the number of terms
n = int(input("Enter the number of terms: "))

# Generate the series
series = fibonacci(n)

# Display the result
print("Fibonacci series:", series)