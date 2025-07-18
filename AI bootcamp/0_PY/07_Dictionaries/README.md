# Python Dictionaries

## Overview
Dictionaries in Python are unordered collections of key-value pairs. They are mutable, fast for lookups, and are one of the most versatile data structures in Python.

## Course Structure

This course is organized into focused modules for better learning:

### 1. Basic Operations
- **`01_dictionary_creation.py`** - Creating dictionaries using various methods
- **`02_accessing_dictionary_elements.py`** - Accessing and retrieving dictionary data
- **`03_modifying_dictionaries.py`** - Adding, updating, and removing dictionary items

### 2. Advanced Operations
- **`04_dictionary_methods.py`** - Dictionary methods like setdefault(), pop(), copy()
- **`05_dictionary_operations.py`** - Merging, comprehension, and transformation operations
- **`06_common_dictionary_patterns.py`** - Common patterns like counting, grouping, caching

### 3. Special Features
- **`07_builtin_functions_dictionaries.py`** - Built-in functions working with dictionaries
- **`08_dictionary_views.py`** - Dictionary views (keys, values, items)

### 4. Practice Problems
- **`09_practice_problems_1.py`** - Basic practice problems with dictionaries
- **`10_practice_problems_2.py`** - Advanced problems including caching and configuration

## How to Use This Course

### Running Individual Files
Each file can be run independently to focus on specific concepts:

```bash
# Run dictionary creation
python 01_dictionary_creation.py

# Run accessing elements
python 02_accessing_dictionary_elements.py

# Run modification methods
python 03_modifying_dictionaries.py

# And so on for each file...
```

### Learning Path
1. Start with `01_dictionary_creation.py` to understand dictionary basics
2. Move to `02_accessing_dictionary_elements.py` and `03_modifying_dictionaries.py` for core operations
3. Study `04_dictionary_methods.py` and `05_dictionary_operations.py` for advanced usage
4. Learn about `06_common_dictionary_patterns.py` for practical patterns
5. Explore `07_builtin_functions_dictionaries.py` for built-in function usage
6. Understand `08_dictionary_views.py` for view objects
7. Practice with `09_practice_problems_1.py` and `10_practice_problems_2.py`

## Dictionary Creation
```python
# Empty dictionary
empty_dict = {}

# Dictionary with key-value pairs
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Using dict() constructor
person = dict(name="Alice", age=25, city="New York")

# From list of tuples
items = [("name", "Alice"), ("age", 25), ("city", "New York")]
person = dict(items)

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## Dictionary Keys and Values
```python
# Keys must be immutable (strings, numbers, tuples)
valid_keys = {
    "name": "Alice",           # String key
    42: "Answer",              # Integer key
    (1, 2): "Tuple key",      # Tuple key
    True: "Boolean key"        # Boolean key
}

# Invalid keys (will raise error)
# invalid_dict = {
#     [1, 2]: "List key",     # Lists are mutable
#     {1, 2}: "Set key"       # Sets are mutable
# }

# Values can be any type
mixed_values = {
    "string": "Hello",
    "number": 42,
    "list": [1, 2, 3],
    "dict": {"nested": "value"},
    "function": len
}
```

## Accessing Dictionary Elements
```python
person = {"name": "Alice", "age": 25, "city": "New York"}

# Using square brackets
name = person["name"]  # "Alice"

# Using get() method (safer)
age = person.get("age")           # 25
job = person.get("job")           # None
job = person.get("job", "Unknown")  # "Unknown" (default value)

# Checking if key exists
if "name" in person:
    print("Name exists")

# Getting all keys, values, and items
keys = person.keys()      # dict_keys(['name', 'age', 'city'])
values = person.values()  # dict_values(['Alice', 25, 'New York'])
items = person.items()    # dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])
```

## Modifying Dictionaries
```python
person = {"name": "Alice", "age": 25}

# Adding new key-value pairs
person["city"] = "New York"
person["job"] = "Engineer"

# Updating existing values
person["age"] = 26

# Using update() method
person.update({"city": "Boston", "salary": 75000})

# Removing items
del person["job"]                    # Raises KeyError if key doesn't exist
removed = person.pop("age")          # Returns value and removes key
person.pop("nonexistent", "default") # Returns default if key doesn't exist
person.clear()                       # Removes all items
```

## Dictionary Methods

### Adding and Updating
```python
person = {"name": "Alice"}

# setdefault() - adds key only if it doesn't exist
person.setdefault("age", 25)  # Adds age: 25
person.setdefault("name", "Bob")  # Doesn't change existing name

# update() - merges dictionaries
person.update({"city": "New York", "job": "Engineer"})
```

### Removing Items
```python
person = {"name": "Alice", "age": 25, "city": "New York"}

# pop() - removes and returns value
age = person.pop("age")  # age = 25, person = {"name": "Alice", "city": "New York"}

# popitem() - removes and returns last item (Python 3.7+)
last_item = person.popitem()  # ("city", "New York")

# clear() - removes all items
person.clear()  # person = {}
```

### Copying Dictionaries
```python
original = {"name": "Alice", "scores": [85, 90, 78]}

# Shallow copy
shallow_copy = original.copy()
shallow_copy = dict(original)

# Deep copy
import copy
deep_copy = copy.deepcopy(original)

# Difference between shallow and deep copy
shallow_copy["scores"][0] = 100  # Affects original
deep_copy["scores"][0] = 100     # Doesn't affect original
```

## Dictionary Operations

### Merging Dictionaries
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Using update()
merged = dict1.copy()
merged.update(dict2)

# Using | operator (Python 3.9+)
merged = dict1 | dict2

# Using ** unpacking
merged = {**dict1, **dict2}
```

### Dictionary Comprehension
```python
# Basic comprehension
squares = {x: x**2 for x in range(5)}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

# From existing dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
upper_person = {k.upper(): v for k, v in person.items()}

# Nested comprehension
matrix = {(i, j): i + j for i in range(3) for j in range(3)}
```

## Common Dictionary Patterns

### Default Values
```python
from collections import defaultdict

# Using defaultdict
word_count = defaultdict(int)
words = ["apple", "banana", "apple", "cherry"]
for word in words:
    word_count[word] += 1  # No need to check if key exists

# Using dict.get() with default
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
```

### Grouping Data
```python
# Group by category
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

# Using defaultdict
from collections import defaultdict
grades_dd = defaultdict(list)
for student in students:
    grades_dd[student["grade"]].append(student["name"])
```

## Built-in Functions with Dictionaries
```python
person = {"name": "Alice", "age": 25, "city": "New York"}

len(person)      # 3
max(person)      # 'name' (lexicographic)
min(person)      # 'age'
any(person)      # True
all(person)      # True

# sorted()
sorted(person)                    # ['age', 'city', 'name']
sorted(person.items())            # [('age', 25), ('city', 'New York'), ('name', 'Alice')]
sorted(person.items(), key=lambda x: x[1])  # Sort by values
```

## Dictionary Views
```python
person = {"name": "Alice", "age": 25, "city": "New York"}

keys_view = person.keys()
values_view = person.values()
items_view = person.items()

# Views are dynamic
person["job"] = "Engineer"
print(list(keys_view))  # ['name', 'age', 'city', 'job']

# Views support set operations
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

keys1 = dict1.keys()
keys2 = dict2.keys()

keys1 & keys2  # {'b'} (intersection)
keys1 | keys2  # {'a', 'b', 'c'} (union)
keys1 - keys2  # {'a'} (difference)
```

## Performance Considerations
```python
# Dictionaries are very fast for lookups
import time

# Creating large dictionary
large_dict = {i: i**2 for i in range(1000000)}

# Lookup time
start = time.time()
for i in range(1000):
    _ = large_dict.get(i)
end = time.time()
print(f"Lookup time: {end - start:.6f} seconds")

# Memory usage
import sys
print(f"Dictionary size: {sys.getsizeof(large_dict)} bytes")
```

## Common Use Cases

### Configuration
```python
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp"
    },
    "api": {
        "timeout": 30,
        "retries": 3
    }
}

# Accessing nested values
db_host = config["database"]["host"]
api_timeout = config["api"]["timeout"]
```

### Caching
```python
cache = {}

def expensive_function(n):
    if n in cache:
        return cache[n]
    
    result = n ** 2  # Expensive calculation
    cache[n] = result
    return result
```

### Data Transformation
```python
# Converting between formats
users = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
    {"id": 3, "name": "Charlie", "age": 35},
]

# Convert to dictionary with id as key
user_dict = {user["id"]: user for user in users}
print(user_dict)
```

## Practice Examples
Each file contains hands-on exercises with dictionaries! Start with the basic files and work your way up to the practice problems. 