# Get the number of people from the user
n = int(input("Enter the number of people: "))

# Create an empty list to store people's details
people = []

# Get each person's name and age from the user
for i in range(n):
    print(f"\nEnter details for person {i + 1}")

    # Get the person's name
    name = input("Enter name: ")

    # Get the person's age
    age = int(input("Enter age: "))

    # Store the person's details in a dictionary
    people.append({"name": name, "age": age})

# Filter people whose age is 18 or above using lambda
adults = list(filter(lambda person: person["age"] >= 18, people))

# Extract the names of adults using map and lambda
names = list(map(lambda person: person["name"], adults))

# Display the final list of names
print("\nNames of people aged 18 or above:", names)
