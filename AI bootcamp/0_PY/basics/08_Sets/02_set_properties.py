# Set Properties

print("=== SET PROPERTIES ===\n")

# 2. Set Properties
print("2. Set Properties:")
# Sets only contain unique elements
duplicate_set = {1, 2, 2, 3, 3, 4}
print(f"Duplicate set: {duplicate_set}")

# Sets are unordered
set1 = {3, 1, 4, 1, 5, 9, 2, 6}
print(f"Unordered set: {set1}")

# Sets can contain different types
mixed_set = {1, "hello", 3.14, True}
print(f"Mixed set: {mixed_set}")

# Sets cannot contain mutable elements
valid_set = {1, (2, 3), frozenset([4, 5])}
print(f"Valid set with immutable elements: {valid_set}")
print()

# Additional property examples
print("More property examples:")

# Sets are mutable
fruits = {"apple", "banana"}
print(f"Original: {fruits}")
fruits.add("orange")
print(f"After adding: {fruits}")

# Sets are hashable (can be used as dictionary keys)
set_dict = {frozenset([1, 2, 3]): "set1", frozenset([4, 5, 6]): "set2"}
print(f"Dictionary with frozen set keys: {set_dict}")

# Sets support iteration
print("Iterating through set:")
for item in fruits:
    print(f"  {item}")

# Sets have no indexing
try:
    first_item = fruits[0]  # type: ignore # This will raise TypeError
except TypeError:
    print("Sets don't support indexing")

# Sets can be converted to other types
fruits_list = list(fruits)
fruits_tuple = tuple(fruits)
print(f"As list: {fruits_list}")
print(f"As tuple: {fruits_tuple}")

print("\n=== END ===")
