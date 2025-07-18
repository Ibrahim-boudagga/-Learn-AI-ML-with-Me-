# Frozen Sets

print("=== FROZEN SETS ===\n")

# 8. Frozen Sets
print("8. Frozen Sets:")
# Frozen sets are immutable
frozen_fruits = frozenset(["apple", "banana", "orange"])
print(f"Frozen set: {frozen_fruits}")

# Frozen sets can be used as dictionary keys
set_dict = {frozen_fruits: "fruit set"}
print(f"Dictionary with frozen set key: {set_dict}")

# Frozen sets support set operations
set1 = frozenset([1, 2, 3])
set2 = frozenset([3, 4, 5])
union = set1 | set2
print(f"Frozen set union: {union}")
print(f"Type of result: {type(union)}")
print()

# Additional frozen set examples
print("More frozen set examples:")

# Creating frozen sets from different sources
frozen_from_list = frozenset([1, 2, 3, 4])
frozen_from_string = frozenset("hello")
frozen_from_range = frozenset(range(5))

print(f"From list: {frozen_from_list}")
print(f"From string: {frozen_from_string}")
print(f"From range: {frozen_from_range}")

# Frozen set operations
set_a = frozenset([1, 2, 3])
set_b = frozenset([2, 3, 4])

intersection = set_a & set_b
difference = set_a - set_b
symmetric_diff = set_a ^ set_b

print(f"Intersection: {intersection}")
print(f"Difference: {difference}")
print(f"Symmetric difference: {symmetric_diff}")

# Frozen sets in sets
nested_set = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Nested set with frozen sets: {nested_set}")

# Frozen sets as dictionary keys
config = {
    frozenset(["read", "write"]): "admin",
    frozenset(["read"]): "user",
    frozenset([]): "guest",
}
print(f"Config with frozen set keys: {config}")

# Immutability test
try:
    frozen_fruits.add("grape")  # type: ignore # This will raise AttributeError
except AttributeError:
    print("Frozen sets are immutable - cannot add elements")

print("\n=== END ===")
