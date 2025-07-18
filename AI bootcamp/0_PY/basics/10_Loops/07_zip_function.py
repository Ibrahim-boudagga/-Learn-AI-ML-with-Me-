# Zip Function

print("=== ZIP FUNCTION ===\n")

# Basic zip with two lists
print("1. Basic zip with two lists:")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")

# Zip with three lists
print("\n2. Zip with three lists:")
cities = ["New York", "London", "Paris"]

for name, age, city in zip(names, ages, cities):
    print(f"  {name} is {age} years old from {city}")

# Different length lists
print("\n3. Different length lists:")
list1 = [1, 2, 3]
list2 = ["a", "b"]
for item1, item2 in zip(list1, list2):
    print(f"  {item1} - {item2}")

# Converting zip to list
print("\n4. Converting zip to list:")
zipped = list(zip(names, ages))
print(f"  Zipped list: {zipped}")

# Zip with enumerate
print("\n5. Zip with enumerate:")
for index, (name, age) in enumerate(zip(names, ages)):
    print(f"  {index}: {name} ({age})")

# Zip with different data types
print("\n6. Zip with different data types:")
numbers = [1, 2, 3, 4, 5]
letters = ["a", "b", "c"]
booleans = [True, False]

for num, letter, boolean in zip(numbers, letters, booleans):
    print(f"  {num} - {letter} - {boolean}")

# Unzipping
print("\n7. Unzipping:")
pairs = [("a", 1), ("b", 2), ("c", 3)]
letters, numbers = zip(*pairs)
print(f"  Letters: {letters}")
print(f"  Numbers: {numbers}")

print("\n=== END OF ZIP FUNCTION ===")
