# Type Checking

print("=== TYPE CHECKING ===\n")

test_values = [42, 3.14, "Hello", True, [1, 2, 3], {"a": 1}]

for value in test_values:
    print(f"Value: {value} -> Type: {type(value).__name__}")

# Using isinstance()
print("\nUsing isinstance():")
for value in test_values:
    if isinstance(value, int):
        print(f"{value} is an integer")
    elif isinstance(value, float):
        print(f"{value} is a float")
    elif isinstance(value, str):
        print(f"{value} is a string")
    elif isinstance(value, bool):
        print(f"{value} is a boolean")
    elif isinstance(value, list):
        print(f"{value} is a list")
    elif isinstance(value, dict):
        print(f"{value} is a dictionary")
print()

# type() function returns the type of an object
# isinstance() checks if an object is an instance of a specific type
# Use isinstance() for type checking (more flexible than type() == type)
