# List Comprehension

print("=== LIST COMPREHENSION ===\n")

# Basic list comprehension
print("1. Basic list comprehension:")
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# List comprehension with condition
print("\n2. List comprehension with condition:")
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# List comprehension with multiple conditions
print("\n3. List comprehension with multiple conditions:")
filtered_numbers = [x for x in range(20) if x % 2 == 0 and x % 3 == 0]
print(f"Numbers divisible by both 2 and 3: {filtered_numbers}")

# Nested comprehension
print("\n4. Nested comprehension:")
matrix = [[i + j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# Dictionary comprehension
print("\n5. Dictionary comprehension:")
word_lengths = {word: len(word) for word in ["apple", "banana", "orange"]}
print(f"Word lengths: {word_lengths}")

# Set comprehension
print("\n6. Set comprehension:")
unique_squares = {x**2 for x in range(10)}
print(f"Unique squares: {unique_squares}")

# List comprehension with enumerate
print("\n7. List comprehension with enumerate:")
fruits = ["apple", "banana", "orange"]
indexed_fruits = [f"{i}: {fruit}" for i, fruit in enumerate(fruits)]
print(f"Indexed fruits: {indexed_fruits}")

# List comprehension with zip
print("\n8. List comprehension with zip:")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = [f"{name} ({age})" for name, age in zip(names, ages)]
print(f"People: {people}")

# Conditional expression in comprehension
print("\n9. Conditional expression in comprehension:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parity = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(f"Parity: {parity}")

# List comprehension with string operations
print("\n10. List comprehension with string operations:")
words = ["python", "programming", "language"]
capitalized = [word.upper() for word in words]
print(f"Capitalized: {capitalized}")

print("\n=== END OF LIST COMPREHENSION ===")
