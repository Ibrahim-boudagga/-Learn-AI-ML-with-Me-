# Dictionary Views

print("=== DICTIONARY VIEWS ===\n")

# 8. Dictionary Views
print("8. Dictionary Views:")
person = {"name": "Alice", "age": 25, "city": "New York"}

keys_view = person.keys()
values_view = person.values()
items_view = person.items()

print(f"Keys view: {keys_view}")
print(f"Values view: {values_view}")
print(f"Items view: {items_view}")

# Views are dynamic
person["job"] = "Engineer"
print(f"Keys view after adding job: {list(keys_view)}")
print()

# Additional view examples
print("More view examples:")

# Views are iterable
print("Iterating through keys:")
for key in keys_view:
    print(f"  {key}")

print("\nIterating through values:")
for value in values_view:
    print(f"  {value}")

print("\nIterating through items:")
for key, value in items_view:
    print(f"  {key}: {value}")

# Views support set operations
person1 = {"name": "Alice", "age": 25, "city": "New York"}
person2 = {"name": "Bob", "age": 30, "city": "Boston"}

keys1 = person1.keys()
keys2 = person2.keys()

print(f"\nKeys from person1: {keys1}")
print(f"Keys from person2: {keys2}")
print(f"Common keys: {keys1 & keys2}")
print(f"All keys: {keys1 | keys2}")
print(f"Keys only in person1: {keys1 - keys2}")

# Views are not lists
print(f"\nType of keys view: {type(keys_view)}")
print(f"Is keys view a list? {isinstance(keys_view, list)}")

# Converting views to lists
keys_list = list(keys_view)
values_list = list(values_view)
items_list = list(items_view)

print(f"Keys as list: {keys_list}")
print(f"Values as list: {values_list}")
print(f"Items as list: {items_list}")

# Views reflect changes
person["salary"] = 75000
print(f"\nAfter adding salary:")
print(f"Keys view: {list(keys_view)}")
print(f"Values view: {list(values_view)}")
print(f"Items view: {list(items_view)}")

print("\n=== END ===")
