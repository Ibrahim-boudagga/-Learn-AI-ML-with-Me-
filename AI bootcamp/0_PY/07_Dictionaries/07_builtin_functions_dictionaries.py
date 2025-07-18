# Built-in Functions with Dictionaries

print("=== BUILT-IN FUNCTIONS WITH DICTIONARIES ===\n")

# 7. Built-in Functions with Dictionaries
print("7. Built-in Functions with Dictionaries:")
person = {"name": "Alice", "age": 25, "city": "New York"}

print(f"Length: {len(person)}")
print(f"Maximum key: {max(person)}")
print(f"Minimum key: {min(person)}")
print(f"Any key: {any(person)}")
print(f"All keys: {all(person)}")

# sorted() with dictionaries
print(f"Sorted keys: {sorted(person)}")
print(f"Sorted items: {sorted(person.items())}")
print(f"Sorted by values: {sorted(person.items(), key=lambda x: x[1])}")
print()

# Additional built-in function examples
print("More built-in function examples:")

# sum() with dictionary values
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
total_score = sum(scores.values())
average_score = total_score / len(scores)
print(f"Total score: {total_score}")
print(f"Average score: {average_score:.1f}")

# max() and min() with key function
print(f"Highest scorer: {max(scores.items(), key=lambda x: x[1])}")
print(f"Lowest scorer: {min(scores.items(), key=lambda x: x[1])}")

# any() and all() with conditions
ages = {"Alice": 25, "Bob": 30, "Charlie": 35, "Diana": 28}
print(f"Any over 30: {any(age > 30 for age in ages.values())}")
print(f"All over 20: {all(age > 20 for age in ages.values())}")

# enumerate() with dictionary
print("\nEnumerate with dictionary:")
for i, (key, value) in enumerate(person.items()):
    print(f"  {i}: {key} = {value}")

# zip() with dictionaries
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "Boston", "Chicago"]

people = dict(zip(names, zip(ages, cities)))
print(f"People from zip: {people}")

# map() with dictionaries
doubled_values = dict(map(lambda item: (item[0], item[1] * 2), scores.items()))
print(f"Doubled scores: {doubled_values}")

# filter() with dictionaries
high_scores = dict(filter(lambda item: item[1] >= 85, scores.items()))
print(f"High scores (>=85): {high_scores}")

print("\n=== END ===")
