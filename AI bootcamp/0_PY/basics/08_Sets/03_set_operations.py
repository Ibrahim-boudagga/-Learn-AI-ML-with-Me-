# Set Operations

print("=== SET OPERATIONS ===\n")

# 3. Set Operations
print("3. Set Operations:")
fruits = {"apple", "banana"}

# Adding elements
fruits.add("orange")
print(f"After add('orange'): {fruits}")

fruits.add("apple")  # No effect (already exists)
print(f"After add('apple') again: {fruits}")

# Adding multiple elements
fruits.update(["grape", "kiwi"])
print(f"After update(['grape', 'kiwi']): {fruits}")

# Removing elements
fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

fruits.discard("kiwi")
print(f"After discard('kiwi'): {fruits}")

popped = fruits.pop()
print(f"Popped element: {popped}")
print(f"After pop(): {fruits}")

fruits.clear()
print(f"After clear(): {fruits}")
print()

# Additional operation examples
print("More operation examples:")

# Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2
print(f"Union: {union}")

# Intersection
intersection = set1 & set2
print(f"Intersection: {intersection}")

# Difference
difference = set1 - set2
print(f"Difference: {difference}")

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

# Set comparison
print(f"set1 <= set2: {set1 <= set2}")
print(f"set1 >= set2: {set1 >= set2}")

print("\n=== END ===")
