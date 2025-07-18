# Built-in Functions with Tuples

print("=== BUILT-IN FUNCTIONS WITH TUPLES ===\n")

# 8. Built-in Functions with Tuples
print("8. Built-in Functions with Tuples:")
numbers = (1, 2, 3, 4, 5)
print(f"Numbers: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Any non-zero: {any(numbers)}")
print(f"All non-zero: {all(numbers)}")

# enumerate()
print("\nEnumerate:")
for index, value in enumerate(numbers):
    print(f"  Index {index}: {value}")

# zip()
names = ("Alice", "Bob", "Charlie")
ages = (25, 30, 35)
print("\nZip:")
for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")
print()

# Additional built-in function examples
print("More built-in function examples:")

# sorted() - returns a list
mixed = (3, 1, 4, 1, 5, 9, 2, 6)
sorted_numbers = sorted(mixed)
print(f"Original: {mixed}")
print(f"Sorted: {sorted_numbers}")
print(f"Reverse sorted: {sorted(mixed, reverse=True)}")

# reversed()
reversed_numbers = tuple(reversed(numbers))
print(f"Reversed: {reversed_numbers}")

# sum() with start value
total = sum(numbers, 10)
print(f"Sum with start value 10: {total}")

# any() and all() with conditions
test_tuple = (0, 1, 2, 3, 4)
print(f"Any greater than 3: {any(x > 3 for x in test_tuple)}")
print(f"All greater than 0: {all(x > 0 for x in test_tuple)}")

# map() with tuples
squared = tuple(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared}")

# filter() with tuples
even_numbers = tuple(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# zip() with more than two iterables
cities = ("New York", "London", "Paris")
countries = ("USA", "UK", "France")
populations = (8.4, 8.9, 2.1)

print("\nMultiple zip:")
for city, country, pop in zip(cities, countries, populations):
    print(f"  {city}, {country}: {pop} million")

print("\n=== END ===")
