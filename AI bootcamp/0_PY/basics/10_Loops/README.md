# Python Loops

## Overview
Loops in Python allow you to execute a block of code multiple times. Python has two main types of loops: `for` loops and `while` loops.

## Course Structure

This course is organized into focused modules for better learning:

### Core Concepts
- **01_basic_for_loops.py** - Basic for loop syntax and iteration
- **02_range_function.py** - Understanding and using the range() function
- **03_iterating_over_data_types.py** - Iterating over lists, tuples, dictionaries, sets, and strings
- **04_while_loops.py** - While loop syntax and use cases
- **05_loop_control_statements.py** - Break, continue, and pass statements
- **06_enumerate_function.py** - Using enumerate() for index and value pairs
- **07_zip_function.py** - Combining multiple iterables with zip()
- **08_list_comprehension.py** - Concise list creation with comprehensions
- **09_common_loop_patterns.py** - Common programming patterns with loops
- **10_nested_loops.py** - Working with nested loop structures

### Practice Problems
- **11_practice_problems_1.py** - Basic to intermediate loop problems (Problems 1-7)
- **12_practice_problems_2.py** - Advanced loop problems (Problems 8-15)

## How to Use This Course

### For Beginners
1. Start with `01_basic_for_loops.py` to understand basic iteration
2. Progress through each file in numerical order
3. Run each file to see the output and understand the concepts
4. Practice with the problems in the practice files

### For Intermediate Learners
1. Review concepts you're less familiar with
2. Focus on the practice problems to strengthen your skills
3. Experiment with modifying the examples

### Running the Examples
```bash
# Run a specific concept file
python 01_basic_for_loops.py

# Run practice problems
python 11_practice_problems_1.py
python 12_practice_problems_2.py
```

## Key Concepts Covered

### For Loops
```python
# Iterating over a range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Iterating over a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Iterating over a string
for char in "Python":
    print(char)
```

### Range Function
```python
# range(stop)
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

# range(start, stop)
for i in range(1, 6):   # 1, 2, 3, 4, 5
    print(i)

# range(start, stop, step)
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# Negative step
for i in range(5, 0, -1):  # 5, 4, 3, 2, 1
    print(i)
```

### While Loops
```python
# Simple counter
count = 0
while count < 5:
    print(count)
    count += 1

# Infinite loop with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
    print(f"You entered: {user_input}")
```

### Loop Control Statements
```python
# Break statement
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# Continue statement
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # 1, 3, 5, 7, 9

# Pass statement
for i in range(5):
    if i < 3:
        pass  # Do nothing for now
    else:
        print(i)
```

### Enumerate Function
```python
# Get both index and value
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Start enumeration from different number
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
```

### Zip Function
```python
# Combine multiple lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old from {city}")
```

### List Comprehension
```python
# Basic list comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Dictionary comprehension
word_lengths = {word: len(word) for word in ["apple", "banana", "orange"]}
```

### Common Loop Patterns
```python
# Accumulator pattern
total = 0
for num in [1, 2, 3, 4, 5]:
    total += num
print(total)

# Counter pattern
text = "hello world"
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

# Filter pattern
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
```

### Nested Loops
```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # Empty line between tables

# Pattern printing
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()  # New line
```

## Practice Problems Included

### Part 1 (Basic to Intermediate)
1. Sum of numbers from 1 to n
2. Count vowels in a string
3. Find the largest number in a list
4. Check if a number is prime
5. Generate Fibonacci sequence
6. Reverse a string
7. Find common elements between two lists

### Part 2 (Advanced)
8. Check if a string is palindrome
9. Generate multiplication table
10. Find factors of a number
11. Check if a number is perfect
12. Generate prime numbers up to n
13. Find the longest word in a sentence
14. Count word frequency
15. Check if a number is Armstrong number

## Best Practices

### Use appropriate loop type
```python
# Use for when you know the number of iterations
for i in range(10):
    print(i)

# Use while when you don't know the number of iterations
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
```

### Use enumerate() for index and value
```python
# Good
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Bad
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
```

### Use zip() for multiple lists
```python
# Good
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# Bad
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]}")
```

### Use list comprehension for simple transformations
```python
# Good
squares = [x**2 for x in range(5)]

# Bad
squares = []
for x in range(5):
    squares.append(x**2)
```

### Avoid modifying list during iteration
```python
# Bad - can cause issues
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)

# Good - create new list
numbers = [1, 2, 3, 4, 5]
even_numbers = [num for num in numbers if num % 2 == 0]
```

## Common Use Cases

### File Processing
```python
# Read file line by line
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())
```

### Data Validation
```python
# Validate list of numbers
numbers = [1, 2, 3, 4, 5]
all_positive = True
for num in numbers:
    if num <= 0:
        all_positive = False
        break
print(f"All positive: {all_positive}")
```

### Search Pattern
```python
# Find first occurrence
numbers = [1, 2, 3, 4, 5]
target = 3
found = False
for num in numbers:
    if num == target:
        found = True
        break
print(f"Found {target}: {found}")
```

## Next Steps
After completing this module, you should be comfortable with:
- Basic and advanced loop concepts
- Common loop patterns and best practices
- Problem-solving with loops
- List comprehensions and functional programming concepts

Move on to the next module to continue your Python learning journey! 