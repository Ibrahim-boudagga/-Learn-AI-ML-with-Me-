# Tuple vs List

print("=== TUPLE VS LIST ===\n")

# 9. Tuple vs List
print("9. Tuple vs List:")
# Tuples are immutable
coordinates = (10, 20)
print(f"Original coordinates: {coordinates}")

# This would raise an error:
# coordinates[0] = 100  # TypeError

# But we can create a new tuple
new_coordinates = coordinates + (30,)
print(f"New coordinates: {new_coordinates}")

# Lists are mutable
coordinates_list = [10, 20]
coordinates_list[0] = 100
print(f"Modified list: {coordinates_list}")
print()

# Additional comparison examples
print("More comparison examples:")

# Memory efficiency
import sys

tuple_example = (1, 2, 3, 4, 5)
list_example = [1, 2, 3, 4, 5]
print(f"Tuple memory: {sys.getsizeof(tuple_example)} bytes")
print(f"List memory: {sys.getsizeof(list_example)} bytes")

# Performance comparison
import time

# Creating many small tuples vs lists
start_time = time.time()
for i in range(1000000):
    t = (i, i + 1, i + 2)
end_time = time.time()
tuple_time = end_time - start_time

start_time = time.time()
for i in range(1000000):
    l = [i, i + 1, i + 2]
end_time = time.time()
list_time = end_time - start_time

print(f"Creating 1M tuples: {tuple_time:.4f} seconds")
print(f"Creating 1M lists: {list_time:.4f} seconds")

# Use cases
print("\nUse cases:")
print("Tuples are better for:")
print("  - Fixed data (coordinates, RGB colors)")
print("  - Dictionary keys")
print("  - Return values from functions")
print("  - Data that shouldn't change")

print("\nLists are better for:")
print("  - Collections that need to change")
print("  - Building data incrementally")
print("  - When you need to modify elements")

# Dictionary keys
point_dict = {(0, 0): "origin", (1, 1): "diagonal"}
print(f"Dictionary with tuple keys: {point_dict}")

# This would work:
# point_dict[(0, 0)] = "new value"

# This would NOT work with lists:
# point_dict[[0, 0]] = "origin"  # TypeError: unhashable type

print("\n=== END ===")
