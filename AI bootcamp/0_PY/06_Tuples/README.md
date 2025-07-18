# Python Tuples

## Overview
Tuples in Python are ordered, immutable collections of items. They are similar to lists but cannot be modified after creation. Tuples are often used for data that shouldn't change.

## Course Structure

This course is organized into focused modules for better learning:

### 1. Basic Operations
- **`01_tuple_creation_basic_operations.py`** - Creating tuples, accessing elements, basic operations
- **`02_tuple_slicing.py`** - Slicing tuples with different patterns
- **`03_tuple_methods.py`** - Tuple methods like count(), index(), membership testing

### 2. Advanced Operations
- **`04_tuple_operations.py`** - Concatenation, repetition, comparison operations
- **`05_tuple_unpacking.py`** - Unpacking techniques and extended unpacking
- **`06_tuple_as_return_values.py`** - Using tuples as function return values

### 3. Special Features
- **`07_named_tuples.py`** - Named tuples for structured data
- **`08_builtin_functions_tuples.py`** - Built-in functions working with tuples
- **`09_tuple_vs_list.py`** - Comparison between tuples and lists

### 4. Practice Problems
- **`10_practice_problems_1.py`** - Basic practice problems with tuples
- **`11_practice_problems_2.py`** - Advanced problems including coordinate systems

## How to Use This Course

### Running Individual Files
Each file can be run independently to focus on specific concepts:

```bash
# Run basic tuple creation
python 01_tuple_creation_basic_operations.py

# Run tuple slicing examples
python 02_tuple_slicing.py

# Run tuple methods
python 03_tuple_methods.py

# And so on for each file...
```

### Learning Path
1. Start with `01_tuple_creation_basic_operations.py` to understand tuple basics
2. Move to `02_tuple_slicing.py` and `03_tuple_methods.py` for core operations
3. Study `04_tuple_operations.py` and `05_tuple_unpacking.py` for advanced usage
4. Learn about `06_tuple_as_return_values.py` for function integration
5. Explore `07_named_tuples.py` for structured data
6. Understand `08_builtin_functions_tuples.py` for built-in function usage
7. Compare with `09_tuple_vs_list.py` to understand when to use each
8. Practice with `10_practice_problems_1.py` and `11_practice_problems_2.py`

## Tuple Creation
```python
# Empty tuple
empty_tuple = ()

# Tuple with elements
numbers = (1, 2, 3, 4, 5)
names = ("Alice", "Bob", "Charlie")
mixed = (1, "hello", 3.14, True)

# Single element tuple (note the comma)
single = (42,)

# Tuple from list
list_data = [1, 2, 3]
tuple_from_list = tuple(list_data)

# Tuple from string
tuple_from_string = tuple("Python")  # ('P', 'y', 't', 'h', 'o', 'n')
```

## Tuple Indexing and Slicing
```python
coordinates = (10, 20, 30, 40, 50)

# Indexing (starts from 0)
first_coord = coordinates[0]      # 10
last_coord = coordinates[-1]      # 50
second_coord = coordinates[1]     # 20

# Slicing [start:end:step]
first_two = coordinates[0:2]      # (10, 20)
last_three = coordinates[-3:]     # (30, 40, 50)
every_second = coordinates[::2]   # (10, 30, 50)
reverse = coordinates[::-1]       # (50, 40, 30, 20, 10)
```

## Tuple Immutability
```python
# Tuples are immutable - you cannot modify them
coordinates = (10, 20, 30)

# This will raise an error:
# coordinates[0] = 100  # TypeError: 'tuple' object does not support item assignment

# This will raise an error:
# coordinates.append(40)  # AttributeError: 'tuple' object has no attribute 'append'

# But you can create a new tuple
new_coordinates = coordinates + (40, 50)  # (10, 20, 30, 40, 50)
```

## Tuple Methods
```python
fruits = ("apple", "banana", "orange", "apple", "grape")

# count() - counts occurrences
apple_count = fruits.count("apple")  # 2

# index() - returns index of first occurrence
banana_index = fruits.index("banana")  # 1

# in operator - checks if element exists
has_orange = "orange" in fruits  # True
has_kiwi = "kiwi" in fruits      # False
```

## Tuple Operations

### Concatenation
```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Using + operator
combined = tuple1 + tuple2  # (1, 2, 3, 4, 5, 6)
```

### Repetition
```python
numbers = (1, 2, 3)

# Using * operator
repeated = numbers * 3  # (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

### Comparison
```python
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (1, 2, 4)

tuple1 == tuple2  # True
tuple1 == tuple3  # False
tuple1 < tuple3   # True (lexicographic comparison)
```

## Tuple Unpacking
```python
# Basic unpacking
coordinates = (10, 20)
x, y = coordinates
print(f"x: {x}, y: {y}")  # x: 10, y: 20

# Multiple assignment
a, b, c = (1, 2, 3)
print(f"a: {a}, b: {b}, c: {c}")  # a: 1, b: 2, c: 3

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
print(f"first: {first}, middle: {middle}, last: {last}")  # first: 1, middle: [2, 3, 4], last: 5

# Ignoring values with underscore
name, age, _ = ("Alice", 25, "Engineer")
print(f"name: {name}, age: {age}")  # name: Alice, age: 25
```

## Tuple as Return Values
```python
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print(f"Coordinates: ({x}, {y})")

def get_person_info():
    return ("Alice", 25, "Engineer")

name, age, job = get_person_info()
print(f"Name: {name}, Age: {age}, Job: {job}")
```

## Named Tuples
```python
from collections import namedtuple

# Creating a named tuple
Person = namedtuple('Person', ['name', 'age', 'city'])

# Creating instances
person1 = Person("Alice", 25, "New York")
person2 = Person("Bob", 30, "London")

# Accessing by name
print(f"{person1.name} is {person1.age} years old from {person1.city}")

# Accessing by index
print(f"{person1[0]} is {person1[1]} years old from {person1[2]}")

# Converting to dictionary
person_dict = person1._asdict()
print(f"Dictionary: {person_dict}")
```

## Tuple vs List
```python
# When to use tuples:
# 1. Data that shouldn't change
coordinates = (10, 20)
rgb_color = (255, 128, 0)

# 2. Dictionary keys (tuples are hashable, lists are not)
valid_key = (1, 2, 3)  # Can be used as dictionary key
# invalid_key = [1, 2, 3]  # Cannot be used as dictionary key

# 3. Return multiple values from functions
def get_min_max(numbers):
    return (min(numbers), max(numbers))

# When to use lists:
# 1. Data that needs to be modified
shopping_list = ["apple", "banana", "orange"]
shopping_list.append("grape")

# 2. When you need list methods
numbers = [1, 2, 3, 4, 5]
numbers.sort()
numbers.reverse()
```

## Built-in Functions with Tuples
```python
numbers = (1, 2, 3, 4, 5)

len(numbers)      # 5
max(numbers)      # 5
min(numbers)      # 1
sum(numbers)      # 15
any(numbers)      # True
all(numbers)      # True

# enumerate()
for index, value in enumerate(numbers):
    print(f"Index {index}: {value}")

# zip()
names = ("Alice", "Bob", "Charlie")
ages = (25, 30, 35)
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

## Common Use Cases

### Coordinates and Points
```python
# 2D coordinates
point = (10, 20)
x, y = point

# 3D coordinates
point_3d = (10, 20, 30)
x, y, z = point_3d

# RGB colors
color = (255, 128, 0)  # Orange
red, green, blue = color
```

### Database Records
```python
# Simulating database records
users = [
    ("Alice", 25, "Engineer"),
    ("Bob", 30, "Designer"),
    ("Charlie", 35, "Manager"),
]

for name, age, job in users:
    print(f"{name} ({age}) - {job}")
```

### Function Arguments
```python
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

p1 = (0, 0)
p2 = (3, 4)
distance = calculate_distance(p1, p2)
print(f"Distance: {distance}")
```

### Dictionary Items
```python
person = {"name": "Alice", "age": 25, "city": "New York"}

# Iterating over dictionary items (tuples)
for key, value in person.items():
    print(f"{key}: {value}")

# Converting to list of tuples
items_list = list(person.items())
print(f"Items as list: {items_list}")
```

## Performance Considerations
```python
# Tuples are generally faster than lists for iteration
import time

# Creating large collections
large_tuple = tuple(range(1000000))
large_list = list(range(1000000))

# Tuples use less memory than lists
import sys
print(f"Tuple size: {sys.getsizeof(large_tuple)} bytes")
print(f"List size: {sys.getsizeof(large_list)} bytes")
```

## Practice Examples
Each file contains hands-on exercises with tuples! Start with the basic files and work your way up to the practice problems. 