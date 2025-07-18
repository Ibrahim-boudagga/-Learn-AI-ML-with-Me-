# Set Creation

print("=== SET CREATION ===\n")

# 1. Set Creation
print("1. Set Creation:")
# Empty set
empty_set = set()
print(f"Empty set: {empty_set}")

# Set with elements
fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}
print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")

# From list (removes duplicates)
numbers_from_list = set([1, 2, 2, 3, 3, 4])
print(f"From list (removes duplicates): {numbers_from_list}")

# From string (creates set of characters)
char_set = set("hello")
print(f"From string 'hello': {char_set}")

# Set comprehension
squares = {x**2 for x in range(5)}
print(f"Set comprehension (squares): {squares}")
print()

# Additional creation methods
print("More creation methods:")

# From tuple
tuple_set = set((1, 2, 3, 2, 4))
print(f"From tuple: {tuple_set}")

# From range
range_set = set(range(5))
print(f"From range: {range_set}")

# From dictionary (gets keys)
dict_set = set({"a": 1, "b": 2, "c": 3})
print(f"From dictionary (keys): {dict_set}")

# Mixed types
mixed_set = {1, "hello", 3.14, True, (1, 2)}
print(f"Mixed types: {mixed_set}")

# Nested sets (using frozenset)
nested_set = {1, 2, frozenset([3, 4])}
print(f"Nested set: {nested_set}")

print("\n=== END ===")
