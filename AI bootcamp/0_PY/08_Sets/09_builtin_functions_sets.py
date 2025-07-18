# Built-in Functions with Sets

print("=== BUILT-IN FUNCTIONS WITH SETS ===\n")

# 9. Built-in Functions with Sets
print("9. Built-in Functions with Sets:")
fruits = {"apple", "banana", "orange"}

print(f"Length: {len(fruits)}")
print(f"Maximum: {max(fruits)}")
print(f"Minimum: {min(fruits)}")
print(f"Any: {any(fruits)}")
print(f"All: {all(fruits)}")

# sorted() with sets
sorted_fruits = sorted(fruits)
print(f"Sorted fruits: {sorted_fruits}")
print()

# Additional built-in function examples
print("More built-in function examples:")

# sum() with numeric sets
numbers = {1, 2, 3, 4, 5}
total = sum(numbers)
average = total / len(numbers)
print(f"Sum: {total}")
print(f"Average: {average}")

# any() and all() with conditions
even_numbers = {2, 4, 6, 8, 10}
print(f"Any even > 5: {any(x > 5 for x in even_numbers)}")
print(f"All even > 5: {all(x > 5 for x in even_numbers)}")

# enumerate() with sets
print("\nEnumerate with set:")
for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")

# map() with sets
doubled = set(map(lambda x: x * 2, numbers))
print(f"Doubled numbers: {doubled}")

# filter() with sets
filtered = set(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {filtered}")

# zip() with sets
set1 = {1, 2, 3}
set2 = {"a", "b", "c"}
zipped = list(zip(set1, set2))
print(f"Zipped sets: {zipped}")

# set() constructor with different iterables
from_list = set([1, 2, 3])
from_tuple = set((1, 2, 3))
from_string = set("hello")
from_range = set(range(5))

print(f"From list: {from_list}")
print(f"From tuple: {from_tuple}")
print(f"From string: {from_string}")
print(f"From range: {from_range}")

print("\n=== END ===")
