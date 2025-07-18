# List Slicing

print("=== LIST SLICING ===\n")

# Sample data
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"Original list: {data}")

# Basic slicing
print(f"\nFirst 3 elements: {data[:3]}")
print(f"Last 3 elements: {data[-3:]}")
print(f"Middle elements (3-7): {data[3:7]}")

# Step slicing
print(f"\nEvery second element: {data[::2]}")
print(f"Every third element: {data[::3]}")

# Reverse slicing
print(f"\nReverse: {data[::-1]}")
print(f"Reverse every second: {data[::-2]}")

# Negative indices
print(f"\nFrom index 2 to end: {data[2:]}")
print(f"From start to index -3: {data[:-3]}")

# Complex slicing
print(f"\nElements 2 to 7, step 2: {data[2:7:2]}")
print(f"Last 5 elements, reverse: {data[-5:][::-1]}")

print("\n=== END ===")
