# Common Dictionary Patterns

print("=== COMMON DICTIONARY PATTERNS ===\n")

# 6. Common Dictionary Patterns
print("6. Common Dictionary Patterns:")

# Counting items
words = ["apple", "banana", "apple", "cherry", "banana"]
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(f"Word counts: {counts}")

# Grouping data
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "Diana", "grade": "C"},
]

grades = {}
for student in students:
    grade = student["grade"]
    if grade not in grades:
        grades[grade] = []
    grades[grade].append(student["name"])

print(f"Students by grade: {grades}")

# Using defaultdict
from collections import defaultdict

grades_dd = defaultdict(list)
for student in students:
    grades_dd[student["grade"]].append(student["name"])
print(f"Using defaultdict: {dict(grades_dd)}")
print()

# Additional pattern examples
print("More pattern examples:")

# Frequency counter
from collections import Counter

text = "hello world hello python"
char_freq = Counter(text)
print(f"Character frequency: {dict(char_freq)}")


# Dictionary as switch/case
def get_operation(operation):
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "Error",
    }
    return operations.get(operation, lambda x, y: "Unknown operation")


print(f"Add: {get_operation('add')(5, 3)}")
print(f"Multiply: {get_operation('multiply')(4, 7)}")
print(f"Unknown: {get_operation('power')(2, 3)}")

# Caching/memoization
cache = {}


def fibonacci(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = result
    return result


print(f"Fibonacci(10): {fibonacci(10)}")
print(f"Cache: {cache}")

print("\n=== END ===")
