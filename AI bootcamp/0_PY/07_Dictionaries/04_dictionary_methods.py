# Dictionary Methods

print("=== DICTIONARY METHODS ===\n")

# 4. Dictionary Methods
print("4. Dictionary Methods:")
person = {"name": "Alice", "age": 25}

# setdefault()
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
print()

# Additional method examples
print("More method examples:")

# fromkeys() - creates dictionary from keys
keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys, "Unknown")
print(f"From keys with default: {default_dict}")

# get() with different defaults
person = {"name": "Alice", "age": 25}
print(f"Name: {person.get('name', 'Unknown')}")
print(f"Job: {person.get('job', 'Unemployed')}")
print(f"Salary: {person.get('salary', 0)}")

# items(), keys(), values()
print(f"Items: {list(person.items())}")
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")

# update() with multiple dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5}

dict1.update(dict2)
dict1.update(dict3)
print(f"After multiple updates: {dict1}")

print("\n=== END ===")
