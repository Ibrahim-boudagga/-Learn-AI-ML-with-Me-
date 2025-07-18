# Mutable vs Immutable

print("=== MUTABLE VS IMMUTABLE ===\n")

# Immutable example
name = "Alice"
print(f"Original name: '{name}'")
# name[0] = "B"  # This would raise an error

# Mutable example
numbers = [1, 2, 3]
print(f"Original numbers: {numbers}")
numbers[0] = 10
print(f"After modification: {numbers}")
print()

# Immutable types: int, float, str, tuple, bool
# Mutable types: list, dict, set
# Immutable objects cannot be changed after creation
# Mutable objects can be modified in place
