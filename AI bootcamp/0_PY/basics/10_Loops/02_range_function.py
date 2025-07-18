# Range Function

print("=== RANGE FUNCTION ===\n")

# range(stop)
print("1. range(stop):")
for i in range(5):
    print(f"  {i}")

# range(start, stop)
print("\n2. range(start, stop):")
for i in range(1, 6):
    print(f"  {i}")

# range(start, stop, step)
print("\n3. range(start, stop, step):")
for i in range(0, 10, 2):
    print(f"  {i}")

# Negative step
print("\n4. range with negative step:")
for i in range(5, 0, -1):
    print(f"  {i}")

# Converting range to list
print("\n5. Converting range to list:")
range_list = list(range(1, 6))
print(f"  range(1, 6) as list: {range_list}")

# Range with different step values
print("\n6. Different step values:")
for i in range(0, 20, 3):
    print(f"  {i}")

print("\n=== END OF RANGE FUNCTION ===")
