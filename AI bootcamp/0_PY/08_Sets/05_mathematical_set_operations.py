# Mathematical Set Operations

print("=== MATHEMATICAL SET OPERATIONS ===\n")

# 5. Mathematical Set Operations
print("5. Mathematical Set Operations:")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union = set1 | set2
print(f"Union: {union}")

# Intersection
intersection = set1 & set2
print(f"Intersection: {intersection}")

# Difference
difference = set1 - set2
print(f"Difference (set1 - set2): {difference}")

# Symmetric difference
symmetric_diff = set1 ^ set2
print(f"Symmetric difference: {symmetric_diff}")

# In-place operations
set1_copy = set1.copy()
set1_copy |= set2
print(f"In-place union: {set1_copy}")

set1_copy = set1.copy()
set1_copy &= set2
print(f"In-place intersection: {set1_copy}")
print()

# Additional mathematical operations
print("More mathematical operations:")

# Multiple set operations
set3 = {5, 6, 7, 8}
all_union = set1 | set2 | set3
print(f"Union of all three sets: {all_union}")

# Intersection of multiple sets
all_intersection = set1 & set2 & set3
print(f"Intersection of all three sets: {all_intersection}")

# Cartesian product (using itertools)
from itertools import product

cartesian = set(product(set1, set2))
print(f"Cartesian product (first 5): {set(list(cartesian)[:5])}")


# Power set (all possible subsets)
def power_set(s):
    from itertools import combinations

    result = set()
    for i in range(len(s) + 1):
        for combo in combinations(s, i):
            result.add(frozenset(combo))
    return result


power_set_example = power_set({1, 2, 3})
print(f"Power set of {{1, 2, 3}}: {power_set_example}")

print("\n=== END ===")
