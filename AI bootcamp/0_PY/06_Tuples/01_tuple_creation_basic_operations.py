# Tuple Creation and Basic Operations

print("=== TUPLE CREATION AND BASIC OPERATIONS ===\n")

# 1. Tuple Creation and Basic Operations
print("1. Tuple Creation and Basic Operations:")
numbers = (1, 2, 3, 4, 5)
names = ("Alice", "Bob", "Charlie")
mixed = (1, "hello", 3.14, True)

print(f"Numbers: {numbers}")
print(f"Names: {names}")
print(f"Mixed: {mixed}")
print(f"Length of numbers: {len(numbers)}")
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
print()

# Additional examples
empty_tuple = ()
single_element = (42,)  # Note the comma
print(f"Empty tuple: {empty_tuple}")
print(f"Single element tuple: {single_element}")

# Tuple from other sequences
list_to_tuple = tuple([1, 2, 3, 4, 5])
string_to_tuple = tuple("hello")
print(f"From list: {list_to_tuple}")
print(f"From string: {string_to_tuple}")

print("\n=== END ===")
