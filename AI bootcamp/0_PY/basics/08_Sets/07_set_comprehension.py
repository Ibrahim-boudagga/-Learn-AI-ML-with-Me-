# Set Comprehension

print("=== SET COMPREHENSION ===\n")

# 7. Set Comprehension
print("7. Set Comprehension:")
# Basic comprehension
squares = {x**2 for x in range(5)}
print(f"Basic comprehension: {squares}")

# With condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"With condition: {even_squares}")

# From existing set
fruits = {"apple", "banana", "orange"}
upper_fruits = {fruit.upper() for fruit in fruits}
print(f"From existing set: {upper_fruits}")

# Complex comprehension
vowels = {"a", "e", "i", "o", "u"}
text = "hello world"
consonants = {char for char in text if char.isalpha() and char not in vowels}
print(f"Complex comprehension (consonants): {consonants}")
print()

# Additional comprehension examples
print("More comprehension examples:")

# From list
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_numbers = {x for x in numbers}
print(f"Unique numbers from list: {unique_numbers}")

# From string with filtering
text = "Python Programming"
letters = {char.lower() for char in text if char.isalpha()}
print(f"Unique letters: {letters}")

# Nested comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
all_numbers = {num for row in matrix for num in row}
print(f"All numbers from matrix: {all_numbers}")

# Conditional with multiple conditions
numbers = range(20)
filtered = {x for x in numbers if x % 2 == 0 and x % 3 == 0}
print(f"Numbers divisible by both 2 and 3: {filtered}")

# From dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
keys_set = {key.upper() for key in person.keys()}
print(f"Uppercase keys: {keys_set}")

print("\n=== END ===")
