# Tuple Operations

print("=== TUPLE OPERATIONS ===\n")

# 4. Tuple Operations
print("4. Tuple Operations:")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print(f"Combined: {combined}")

# Repetition
repeated = tuple1 * 3
print(f"Repeated: {repeated}")

# Comparison
print(f"tuple1 == tuple2: {tuple1 == tuple2}")
print(f"tuple1 < tuple2: {tuple1 < tuple2}")  # type: ignore
print()

# Additional operation examples
print("More operation examples:")

# Multiple concatenation
tuple3 = (7, 8, 9)
all_combined = tuple1 + tuple2 + tuple3
print(f"All combined: {all_combined}")

# Mixed repetition
mixed_repeat = (1, 2) * 4
print(f"Mixed repeat: {mixed_repeat}")

# Comparison with different lengths
short = (1, 2)
long = (1, 2, 3)
print(f"short < long: {short < long}")
print(f"long > short: {long > short}")

# Element-wise comparison
tuple_a = (1, 2, 3)
tuple_b = (1, 2, 4)
print(f"tuple_a < tuple_b: {tuple_a < tuple_b}")  # type: ignore

# Identity and equality
print(f"\nIdentity and equality:")
print(f"tuple1 is tuple1: {tuple1 is tuple1}")
print(f"tuple1 == (1, 2, 3): {tuple1 == (1, 2, 3)}")

print("\n=== END ===")
