# Python Dictionaries

## Overview
Dictionaries in Python are unordered collections of key-value pairs. They are mutable, fast for lookups, and are one of the most versatile data structures in Python.

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
    {"name": "Diana", "grade": "C"}
]

grades = {}
for student in students:
    grade = student["grade"]
    if grade not in grades:
        grades[grade] = []
    grades[grade].append(student["name"])

# Using defaultdict
from collections import defaultdict
grades = defaultdict(list)
for student in students:
    grades[student["grade"]].append(student["name"])
```

### Counting Items
```python
from collections import Counter

# Using Counter
words = ["apple", "banana", "apple", "cherry", "banana"]
word_counts = Counter(words)

# Manual counting
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
```

## Built-in Functions with Dictionaries
```python
person = {"name": "Alice", "age": 25, "city": "New York"}

len(person)      # 3
max(person)      # 'name' (alphabetical)
min(person)      # 'age'
any(person)      # True (any key is truthy)
all(person)      # True (all keys are truthy)

# sorted() with dictionaries
sorted(person)                    # ['age', 'city', 'name']
sorted(person.items())            # [('age', 25), ('city', 'New York'), ('name', 'Alice')]
sorted(person.items(), key=lambda x: x[1])  # Sort by values
```

## Dictionary Views
```python
person = {"name": "Alice", "age": 25, "city": "New York"}

# Views are dynamic
keys_view = person.keys()
values_view = person.values()
items_view = person.items()

# Views update when dictionary changes
person["job"] = "Engineer"
print(list(keys_view))  # ['name', 'age', 'city', 'job']

# Converting to list (static snapshot)
keys_list = list(person.keys())
```

## Performance Considerations
```python
# Dictionary lookups are O(1) - very fast
large_dict = {i: i**2 for i in range(1000000)}
# large_dict[500000]  # Very fast lookup

# Key considerations
# 1. Keys should be hashable (immutable)
# 2. Dictionary order is preserved (Python 3.7+)
# 3. Memory usage increases with size
# 4. Use .get() for safe access
# 5. Use .setdefault() for conditional updates
```

## Common Use Cases

### Configuration Storage
```python
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp"
    },
    "api": {
        "base_url": "https://api.example.com",
        "timeout": 30
    }
}

# Accessing nested values
db_host = config["database"]["host"]
api_timeout = config["api"]["timeout"]
```

### Caching/Memoization
```python
def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    return cache[n]
```

### JSON-like Data
```python
# API response simulation
api_response = {
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ],
        "total": 2
    },
    "timestamp": "2024-01-01T12:00:00Z"
}

# Accessing nested data
users = api_response["data"]["users"]
total_users = api_response["data"]["total"]
```

## Best Practices
```python
# 1. Use descriptive key names
good = {"user_name": "Alice", "user_age": 25}
bad = {"n": "Alice", "a": 25}

# 2. Use .get() for safe access
age = person.get("age", 0)  # Instead of person["age"]

# 3. Use .setdefault() for conditional updates
person.setdefault("scores", []).append(85)

# 4. Use dict comprehension for transformations
upper_person = {k.upper(): v for k, v in person.items()}

# 5. Use defaultdict for counting/grouping
from collections import defaultdict
counts = defaultdict(int)
```

## Practice Examples
See `practice.py` for hands-on exercises with dictionaries! 