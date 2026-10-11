#Extract year, month, and day from a datetime object
# Import datetime from the datetime module
from datetime import datetime

# Create a datetime object
date = datetime(2026, 10, 9)

# Use a lambda function to extract year, month, and day
get_date = lambda d: (d.year, d.month, d.day)

# Store the extracted values
year, month, day = get_date(date)

# Display the result
print("Year:", year)
print("Month:", month)
print("Day:", day)