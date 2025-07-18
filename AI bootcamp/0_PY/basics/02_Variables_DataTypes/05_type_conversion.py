# Type Conversion

print("=== TYPE CONVERSION ===\n")

# String to number
number_string = "42"
float_string = "3.14"

number_int = int(number_string)
number_float = float(float_string)

print(f"String '{number_string}' to int: {number_int}")
print(f"String '{float_string}' to float: {number_float}")

# Number to string
int_to_string = str(42)
float_to_string = str(3.14)

print(f"Int {42} to string: '{int_to_string}'")
print(f"Float {3.14} to string: '{float_to_string}'")

# List conversions
string_to_list = list("Python")
tuple_to_list = list((1, 2, 3))

print(f"String 'Python' to list: {string_to_list}")
print(f"Tuple (1, 2, 3) to list: {tuple_to_list}")
print()

# Type conversion functions: int(), float(), str(), list(), tuple(), etc.
# Be careful with conversions that might fail
# Always handle potential conversion errors
