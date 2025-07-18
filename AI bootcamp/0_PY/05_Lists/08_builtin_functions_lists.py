# Built-in Functions with Lists

print("=== BUILT-IN FUNCTIONS WITH LISTS ===\n")

# Basic list
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# len() - length of list
print(f"Length: {len(numbers)}")

# max() and min() - maximum and minimum values
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")

# sum() - sum of all elements
print(f"Sum: {sum(numbers)}")

# any() and all() - check conditions
print(f"Any non-zero: {any(numbers)}")
print(f"All non-zero: {all(numbers)}")

# any() and all() with conditions
print(f"Any > 3: {any(x > 3 for x in numbers)}")
print(f"All > 0: {all(x > 0 for x in numbers)}")

# enumerate() - iterate with index
print("\nEnumerate:")
for index, value in enumerate(numbers):
    print(f"  Index {index}: {value}")

# enumerate() with start parameter
print("\nEnumerate with start=1:")
for index, value in enumerate(numbers, start=1):
    print(f"  Position {index}: {value}")

# zip() - combine multiple lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

print("\nZip:")
for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")

# zip() with multiple lists
print("\nZip with multiple lists:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name} ({age}) lives in {city}")

# zip() with different lengths
short_list = [1, 2]
long_list = [10, 20, 30, 40]
print(f"\nZip with different lengths:")
for a, b in zip(short_list, long_list):
    print(f"  {a} + {b} = {a + b}")

# sorted() - returns new sorted list
mixed = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nOriginal: {mixed}")
print(f"Sorted: {sorted(mixed)}")
print(f"Reverse sorted: {sorted(mixed, reverse=True)}")

# reversed() - returns iterator
print(f"\nReversed: {list(reversed(mixed))}")

print("\n=== END ===")
