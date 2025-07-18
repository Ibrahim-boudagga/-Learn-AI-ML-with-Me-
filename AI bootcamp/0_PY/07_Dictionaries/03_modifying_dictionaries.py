# Modifying Dictionaries

print("=== MODIFYING DICTIONARIES ===\n")

# 3. Modifying Dictionaries
print("3. Modifying Dictionaries:")
person = {"name": "Alice", "age": 25}

# Adding new key-value pairs
person["city"] = "New York"
person["job"] = "Engineer"
print(f"After adding: {person}")

# Updating existing values
person["age"] = 26
print(f"After updating age: {person}")

# Using update() method
person.update({"city": "Boston", "salary": 75000})
print(f"After update(): {person}")

# Removing items
removed_age = person.pop("age")
print(f"Removed age: {removed_age}")
print(f"After pop(): {person}")

# Using del
del person["job"]
print(f"After del: {person}")

# clear() method
person.clear()
print(f"After clear(): {person}")
print()

# Additional modification methods
print("More modification methods:")

# setdefault() - adds key if it doesn't exist
person = {"name": "Alice", "age": 25}
person.setdefault("city", "New York")
person.setdefault("name", "Bob")  # Won't change existing value
print(f"After setdefault(): {person}")

# popitem() - removes and returns last item
last_item = person.popitem()
print(f"Last item removed: {last_item}")
print(f"After popitem(): {person}")

# copy() method
original = {"name": "Alice", "scores": [85, 90, 78]}
shallow_copy = original.copy()
print(f"Original: {original}")
print(f"Shallow copy: {shallow_copy}")

# Modifying nested structure affects both
shallow_copy["scores"][0] = 100
print(f"After modifying nested: {original}")
print(f"Shallow copy: {shallow_copy}")

# Deep copy
import copy

deep_copy = copy.deepcopy(original)
deep_copy["scores"][1] = 95
print(f"After deep copy modification: {original}")
print(f"Deep copy: {deep_copy}")

print("\n=== END ===")
