# Built-in Functions

print("=== BUILT-IN FUNCTIONS ===\n")

numbers = [1, -5, 10, -3, 8]

print(f"Numbers: {numbers}")
print(f"Absolute values: {[abs(n) for n in numbers]}")
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")
print()

# Built-in functions for numbers:
# abs() : Absolute value
# min() : Minimum value
# max() : Maximum value
# sum() : Sum of all values
# len() : Length of sequence
# round() : Round to nearest integer
