# Iterating Over Different Data Types

print("=== ITERATING OVER DIFFERENT DATA TYPES ===\n")

# Lists
print("1. Iterating over Lists:")
numbers = [1, 2, 3, 4, 5]
print("Doubling numbers:")
for num in numbers:
    print(f"  {num} * 2 = {num * 2}")

# Tuples
print("\n2. Iterating over Tuples:")
coordinates = [(1, 2), (3, 4), (5, 6)]
print("Coordinates:")
for x, y in coordinates:
    print(f"  Point: ({x}, {y})")

# Dictionaries
print("\n3. Iterating over Dictionaries:")
person = {"name": "Alice", "age": 25, "city": "New York"}

print("Keys only:")
for key in person:
    print(f"  {key}: {person[key]}")

print("\nKeys and values:")
for key, value in person.items():
    print(f"  {key}: {value}")

print("\nValues only:")
for value in person.values():
    print(f"  {value}")

# Sets
print("\n4. Iterating over Sets:")
unique_numbers = {1, 2, 3, 4, 5}
print("Unique numbers:")
for num in unique_numbers:
    print(f"  {num}")

# Strings (already covered in basic for loops)
print("\n5. Iterating over Strings:")
text = "Python"
print("Characters with index:")
for i, char in enumerate(text):
    print(f"  {i}: {char}")

print("\n=== END OF ITERATING OVER DATA TYPES ===")
