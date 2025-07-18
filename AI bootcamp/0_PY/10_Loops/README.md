# Python Loops

## Overview
Loops in Python allow you to execute a block of code multiple times. Python has two main types of loops: `for` loops and `while` loops.

## For Loops

### Basic For Loop
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

### Iterating Over Different Data Types
```python
# Lists
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num * 2)

# Tuples
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"Point: ({x}, {y})")

# Dictionaries
person = {"name": "Alice", "age": 25, "city": "New York"}
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key}: {value}")

# Sets
unique_numbers = {1, 2, 3, 4, 5}
for num in unique_numbers:
    print(num)
```

## While Loops

### Basic While Loop
```python
# Simple counter
count = 0
while count < 5:
    print(count)
    count += 1

# User input loop
password = "secret123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Access granted!")
        break
    else:
        attempts += 1
        print(f"Wrong password. {max_attempts - attempts} attempts left")
```

### Infinite Loops
```python
# Intentional infinite loop with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
    print(f"You entered: {user_input}")

# Infinite loop with continue
count = 0
while True:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    if count > 10:
        break
    print(count)
```

## Loop Control Statements

### Break Statement
```python
# Break out of loop
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# Break in nested loops
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            break  # Breaks inner loop only
        print(f"({i}, {j})")
```

### Continue Statement
```python
# Skip current iteration
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # 1, 3, 5, 7, 9

# Continue in while loop
count = 0
while count < 10:
    count += 1
    if count == 5:
        continue  # Skip 5
    print(count)
```

### Pass Statement
```python
# Placeholder for future code
for i in range(5):
    if i < 3:
        pass  # Do nothing for now
    else:
        print(i)
```

## Enumerate Function
```python
# Get both index and value
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Start enumeration from different number
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
```

## Zip Function
```python
# Combine multiple lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old from {city}")

# Different length lists
list1 = [1, 2, 3]
list2 = ["a", "b"]
for item1, item2 in zip(list1, list2):
    print(f"{item1} - {item2}")  # Stops at shorter list
```

## List Comprehension
```python
# Basic list comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Nested comprehension
matrix = [[i + j for j in range(3)] for i in range(3)]

# Dictionary comprehension
word_lengths = {word: len(word) for word in ["apple", "banana", "orange"]}
```

## Common Loop Patterns

### Accumulator Pattern
```python
# Sum numbers
total = 0
for num in [1, 2, 3, 4, 5]:
    total += num
print(total)

# Find maximum
numbers = [3, 7, 2, 9, 1]
max_num = numbers[0]
for num in numbers[1:]:
    if num > max_num:
        max_num = num
print(max_num)
```

### Counter Pattern
```python
# Count occurrences
text = "hello world"
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)
```

### Filter Pattern
```python
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)
```

### Map Pattern
```python
# Double all numbers
numbers = [1, 2, 3, 4, 5]
doubled = []
for num in numbers:
    doubled.append(num * 2)
print(doubled)
```

## Nested Loops
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

## Loop Performance Tips

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

# Process CSV-like data
data = "name,age,city\nAlice,25,NY\nBob,30,LA"
for line in data.split('\n')[1:]:  # Skip header
    name, age, city = line.split(',')
    print(f"{name} is {age} from {city}")
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

### Keep loops simple
```python
# Good - simple loop
for num in numbers:
    if num > 0:
        print(num)

# Bad - complex logic in loop
for num in numbers:
    if num > 0:
        if num % 2 == 0:
            if num < 100:
                print(num)
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

## Practice Examples
See `practice.py` for hands-on exercises with loops! 