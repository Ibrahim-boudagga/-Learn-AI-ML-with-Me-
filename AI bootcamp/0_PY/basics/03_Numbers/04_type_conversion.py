# Type Conversion

print("=== TYPE CONVERSION ===\n")

float_num = 3.14
int_num = 42
string_num = "123"

print(f"Converting {float_num} to int: {int(float_num)}")
print(f"Converting {int_num} to float: {float(int_num)}")
print(f"Converting '{string_num}' to int: {int(string_num)}")
print(f"Converting '{string_num}' to float: {float(string_num)}")
print()

# Type conversion functions for numbers:
# int() : Convert to integer (truncates decimal part)
# float() : Convert to float
# str() : Convert to string
# Be careful with string to number conversion - may raise ValueError
