# Set Membership

print("=== SET MEMBERSHIP ===\n")

# 4. Set Membership
print("4. Set Membership:")
fruits = {"apple", "banana", "orange"}

print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
print(f"'apple' not in fruits: {'apple' not in fruits}")

print(f"Length: {len(fruits)}")
print(f"Boolean value: {bool(fruits)}")
print()

# Additional membership examples
print("More membership examples:")

# Empty set membership
empty_set = set()
print(f"Empty set boolean: {bool(empty_set)}")
print(f"Length of empty set: {len(empty_set)}")

# Membership with different types
mixed_set = {1, "hello", 3.14, True}
print(f"1 in mixed_set: {1 in mixed_set}")
print(f"'hello' in mixed_set: {'hello' in mixed_set}")
print(f"False in mixed_set: {False in mixed_set}")

# Membership testing with sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(f"set1.issubset(set2): {set1.issubset(set2)}")
print(f"set1.issuperset(set2): {set1.issuperset(set2)}")
print(f"set1.isdisjoint(set2): {set1.isdisjoint(set2)}")

# Using operators for membership
print(f"set1 <= set2: {set1 <= set2}")
print(f"set1 >= set2: {set1 >= set2}")

# Membership with frozen sets
frozen_set = frozenset([1, 2, 3])
print(f"1 in frozen_set: {1 in frozen_set}")
print(f"4 in frozen_set: {4 in frozen_set}")

print("\n=== END ===")
