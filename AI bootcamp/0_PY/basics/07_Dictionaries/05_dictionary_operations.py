# Dictionary Operations

print("=== DICTIONARY OPERATIONS ===\n")

# 5. Dictionary Operations
print("5. Dictionary Operations:")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Merging dictionaries
merged = dict1.copy()
merged.update(dict2)
print(f"Merged: {merged}")

# Dictionary comprehension
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From existing dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
upper_person = {k.upper(): v for k, v in person.items()}
print(f"Upper keys: {upper_person}")
print()

# Additional operation examples
print("More operation examples:")

# Merging with | operator (Python 3.9+)
dict3 = {"e": 5, "f": 6}
merged_pipe = dict1 | dict2 | dict3
print(f"Merged with |: {merged_pipe}")

# Dictionary comprehension with conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_odd = {x: "even" if x % 2 == 0 else "odd" for x in numbers}
print(f"Even/odd mapping: {even_odd}")

# Filtering dictionary
person = {"name": "Alice", "age": 25, "city": "New York", "job": "Engineer"}
string_values = {k: v for k, v in person.items() if isinstance(v, str)}
print(f"String values only: {string_values}")

# Transforming values
person = {"name": "alice", "age": 25, "city": "new york"}
capitalized = {k: v.title() if isinstance(v, str) else v for k, v in person.items()}
print(f"Capitalized strings: {capitalized}")

# Nested dictionary operations
nested = {
    "user1": {"name": "Alice", "scores": [85, 90, 78]},
    "user2": {"name": "Bob", "scores": [92, 88, 95]},
    "user3": {"name": "Charlie", "scores": [78, 85, 80]},
}

# Calculate average scores
averages = {
    name: sum(data["scores"]) / len(data["scores"]) for name, data in nested.items()
}
print(f"Average scores: {averages}")

print("\n=== END ===")
