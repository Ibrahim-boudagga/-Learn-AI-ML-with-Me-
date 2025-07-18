# List Comprehension

print("=== LIST COMPREHENSION ===\n")

# Basic comprehension
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Filtering with comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
odds = [x for x in numbers if x % 2 != 0]
print(f"Numbers: {numbers}")
print(f"Evens: {evens}")
print(f"Odds: {odds}")

# String manipulation
words = ["hello", "world", "python", "programming"]
upper_words = [word.upper() for word in words]
lengths = [len(word) for word in words]
print(f"Words: {words}")
print(f"Upper case: {upper_words}")
print(f"Lengths: {lengths}")

# Nested comprehension
matrix = [[i + j for j in range(3)] for i in range(3)]
print(f"\nMatrix: {matrix}")

# Flattening nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested for item in sublist]
print(f"Nested: {nested}")
print(f"Flattened: {flattened}")

# Dictionary comprehension
word_lengths = {word: len(word) for word in ["apple", "banana", "orange"]}
print(f"\nWord lengths: {word_lengths}")

# Set comprehension
vowels = {char for char in "hello world" if char in "aeiou"}
print(f"Vowels in 'hello world': {vowels}")

# Conditional expressions in comprehension
numbers = [-2, -1, 0, 1, 2, 3]
abs_values = [x if x >= 0 else -x for x in numbers]
print(f"\nNumbers: {numbers}")
print(f"Absolute values: {abs_values}")

print("\n=== END ===")
