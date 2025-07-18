# Dictionary Creation

print("=== DICTIONARY CREATION ===\n")

# 1. Dictionary Creation
print("1. Dictionary Creation:")
# Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")

# Dictionary with key-value pairs
person = {"name": "Alice", "age": 25, "city": "New York"}
print(f"Person dictionary: {person}")

# Using dict() constructor
person2 = dict(name="Bob", age=30, city="Boston")
print(f"Person2 dictionary: {person2}")

# From list of tuples
items = [("name", "Charlie"), ("age", 35), ("city", "Chicago")]
person3 = dict(items)
print(f"Person3 dictionary: {person3}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(f"Squares dictionary: {squares}")
print()

# Additional creation methods
print("More creation methods:")

# From two lists using zip()
keys = ["name", "age", "city"]
values = ["David", 40, "Miami"]
person4 = dict(zip(keys, values))
print(f"From zip(): {person4}")

# Nested dictionaries
nested = {
    "user": {"name": "Alice", "age": 25},
    "settings": {"theme": "dark", "language": "en"},
}
print(f"Nested dictionary: {nested}")

# Dictionary with different value types
mixed = {
    "string": "hello",
    "number": 42,
    "boolean": True,
    "list": [1, 2, 3],
    "tuple": (1, 2),
    "dict": {"nested": "value"},
}
print(f"Mixed types: {mixed}")

print("\n=== END ===")
