# List Operations

print("=== LIST OPERATIONS ===\n")

# Sample lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

print(f"List1: {list1}")
print(f"List2: {list2}")
print(f"List3: {list3}")

# Concatenation with +
combined = list1 + list2
print(f"\nCombined (list1 + list2): {combined}")

# Multiple concatenation
all_lists = list1 + list2 + list3
print(f"All lists combined: {all_lists}")

# Repetition with *
repeated = list1 * 3
print(f"\nRepeated (list1 * 3): {repeated}")

# Repetition with different numbers
double_repeat = [1, 2] * 2
print(f"Double repeat: {double_repeat}")

# Comparison operations
print(f"\nComparison:")
print(f"list1 == list2: {list1 == list2}")
print(f"list1 < list2: {list1 < list2}")
print(f"list1 > list2: {list1 > list2}")

# Comparison with different types
list_a = [1, 2, 3]
list_b = [1, 2, 4]
list_c = [1, 2, 3, 4]

print(f"\nMore comparisons:")
print(f"list_a == list_b: {list_a == list_b}")
print(f"list_a < list_b: {list_a < list_b}")
print(f"list_a < list_c: {list_a < list_c}")

# Identity comparison
list_copy = list1.copy()
print(f"\nIdentity:")
print(f"list1 is list_copy: {list1 is list_copy}")
print(f"list1 == list_copy: {list1 == list_copy}")

# Membership testing
print(f"\nMembership:")
print(f"2 in list1: {2 in list1}")
print(f"5 in list1: {5 in list1}")
print(f"[1, 2] in [list1, list2]: {[1, 2] in [list1, list2]}")

# Slicing operations
original = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\nOriginal: {original}")

# Assignment to slice
original[2:5] = [20, 30, 40]
print(f"After slice assignment: {original}")

# Delete slice
del original[1:4]
print(f"After deleting slice: {original}")

# Insert at slice
original[2:2] = [100, 200]
print(f"After inserting at slice: {original}")

print("\n=== END ===")
