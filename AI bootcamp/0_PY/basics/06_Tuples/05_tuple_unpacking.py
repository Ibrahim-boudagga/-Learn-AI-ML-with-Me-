# Tuple Unpacking

print("=== TUPLE UNPACKING ===\n")

# 5. Tuple Unpacking
print("5. Tuple Unpacking:")
coordinates = (10, 20)
x, y = coordinates
print(f"Coordinates: x={x}, y={y}")

# Multiple assignment
a, b, c = (1, 2, 3)
print(f"Multiple assignment: a={a}, b={b}, c={c}")

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
print(f"Extended unpacking: first={first}, middle={middle}, last={last}")

# Ignoring values with underscore
name, age, _ = ("Alice", 25, "Engineer")
print(f"Ignoring values: name={name}, age={age}")
print()

# Additional unpacking examples
print("More unpacking examples:")

# Unpacking in loops
points = [(1, 2), (3, 4), (5, 6)]
print("Unpacking in loops:")
for x, y in points:
    print(f"  Point: ({x}, {y})")

# Nested unpacking
nested = ((1, 2), (3, 4), (5, 6))
print(f"\nNested unpacking:")
for (a, b), (c, d) in zip(nested, nested[1:]):
    print(f"  ({a}, {b}) and ({c}, {d})")

# Unpacking with default values (Python 3.10+)
# Note: This requires Python 3.10+
try:
    a, b, c = (1, 2)  # type: ignore # This would raise ValueError
except ValueError:
    print("Cannot unpack 2 values into 3 variables")

# Using extended unpacking for defaults
values = (1, 2)
a, b, *rest = values + (None,) * 3
print(f"With defaults: a={a}, b={b}, rest={rest}")

print("\n=== END ===")
