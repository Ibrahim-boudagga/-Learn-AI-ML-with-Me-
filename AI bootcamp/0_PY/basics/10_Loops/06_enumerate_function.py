# Enumerate Function

print("=== ENUMERATE FUNCTION ===\n")

# Basic enumerate
print("1. Basic enumerate:")
fruits = ["apple", "banana", "orange"]
print("Fruits with index:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# Enumerate with custom start
print("\n2. Enumerate with custom start:")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}: {fruit}")

# Enumerate with negative start
print("\n3. Enumerate with negative start:")
for index, fruit in enumerate(fruits, start=-2):
    print(f"  {index}: {fruit}")

# Enumerate with strings
print("\n4. Enumerate with strings:")
text = "Python"
for index, char in enumerate(text):
    print(f"  {index}: '{char}'")

# Enumerate with tuples
print("\n5. Enumerate with tuples:")
coordinates = [(1, 2), (3, 4), (5, 6)]
for index, (x, y) in enumerate(coordinates):
    print(f"  {index}: ({x}, {y})")

# Converting enumerate to list
print("\n6. Converting enumerate to list:")
enumerated_list = list(enumerate(fruits))
print(f"  Enumerated list: {enumerated_list}")

# Enumerate with dictionary
print("\n7. Enumerate with dictionary:")
person = {"name": "Alice", "age": 25, "city": "New York"}
for index, (key, value) in enumerate(person.items()):
    print(f"  {index}: {key} = {value}")

print("\n=== END OF ENUMERATE FUNCTION ===")
