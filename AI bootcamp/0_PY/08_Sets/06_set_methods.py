# Set Methods

print("=== SET METHODS ===\n")

# 6. Set Methods
print("6. Set Methods:")
fruits = {"apple", "banana", "orange", "grape"}

# Set comparison
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4}
set_c = {1, 2, 3}

print(f"set_a.issubset(set_b): {set_a.issubset(set_b)}")
print(f"set_b.issuperset(set_a): {set_b.issuperset(set_a)}")
print(f"set_a.isdisjoint({4, 5, 6}): {set_a.isdisjoint({4, 5, 6})}")

# Using operators
print(f"set_a <= set_b: {set_a <= set_b}")
print(f"set_b >= set_a: {set_b >= set_a}")
print()

# Additional method examples
print("More method examples:")

# copy() method
original = {1, 2, 3}
copied = original.copy()
print(f"Original: {original}")
print(f"Copied: {copied}")

# difference_update() method
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
set1.difference_update(set2)
print(f"After difference_update: {set1}")

# intersection_update() method
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6}
set1.intersection_update(set2)
print(f"After intersection_update: {set1}")

# symmetric_difference_update() method
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.symmetric_difference_update(set2)
print(f"After symmetric_difference_update: {set1}")

# remove() vs discard()
test_set = {1, 2, 3, 4}
print(f"Original: {test_set}")

# discard() - doesn't raise error if element doesn't exist
test_set.discard(5)  # No error
print(f"After discard(5): {test_set}")

# remove() - raises error if element doesn't exist
try:
    test_set.remove(5)  # This will raise KeyError
except KeyError:
    print("KeyError: 5 not in set")

print("\n=== END ===")
