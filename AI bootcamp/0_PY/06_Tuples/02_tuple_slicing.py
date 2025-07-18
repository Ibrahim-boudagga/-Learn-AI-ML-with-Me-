# Tuple Slicing

print("=== TUPLE SLICING ===\n")

# 2. Tuple Slicing
print("2. Tuple Slicing:")
data = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(f"Original tuple: {data}")
print(f"First 3 elements: {data[:3]}")
print(f"Last 3 elements: {data[-3:]}")
print(f"Middle elements (3-7): {data[3:7]}")
print(f"Every second element: {data[::2]}")
print(f"Reverse: {data[::-1]}")
print()

# Additional slicing examples
print("More slicing examples:")
print(f"Elements from index 2 to end: {data[2:]}")
print(f"Elements from start to index 5: {data[:5]}")
print(f"Every third element: {data[::3]}")
print(f"Reverse every second element: {data[::-2]}")

# Negative indexing
print(f"\nNegative indexing:")
print(f"Last element: {data[-1]}")
print(f"Second to last: {data[-2]}")
print(f"Last 4 elements: {data[-4:]}")

print("\n=== END ===")
