# Python Sets

## Overview
Sets in Python are unordered collections of unique elements. They are mutable and support mathematical set operations like union, intersection, and difference.

## Set Creation
```python
# Empty set
empty_set = set()

# Set with elements
fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}

# From list (removes duplicates)
numbers_from_list = set([1, 2, 2, 3, 3, 4])

# From string (creates set of characters)
char_set = set("hello")  # {'h', 'e', 'l', 'o'}

# Set comprehension
squares = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}
```

## Set Properties
```python
# Sets only contain unique elements
duplicate_set = {1, 2, 2, 3, 3, 4}  # {1, 2, 3, 4}

# Sets are unordered
set1 = {3, 1, 4, 1, 5, 9, 2, 6}
print(set1)  # Order may vary

# Sets can contain different types
mixed_set = {1, "hello", 3.14, True}

# Sets cannot contain mutable elements
# invalid_set = {1, [2, 3], {4, 5}}  # This would raise an error
valid_set = {1, (2, 3), frozenset([4, 5])}  # This works
```

## Set Operations

### Adding and Removing Elements
```python
fruits = {"apple", "banana"}

# Adding elements
fruits.add("orange")
fruits.add("apple")  # No effect (already exists)

# Adding multiple elements
fruits.update(["grape", "kiwi"])

# Removing elements
fruits.remove("banana")  # Raises KeyError if not found
fruits.discard("kiwi")   # No error if not found
popped = fruits.pop()    # Removes and returns arbitrary element
fruits.clear()           # Removes all elements
```

### Set Membership
```python
fruits = {"apple", "banana", "orange"}

# Checking membership
"apple" in fruits      # True
"grape" in fruits     # False
"apple" not in fruits # False

# Length and emptiness
len(fruits)           # 3
bool(fruits)          # True (non-empty)
```

## Mathematical Set Operations

### Union
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using | operator
union = set1 | set2  # {1, 2, 3, 4, 5}

# Using union() method
union = set1.union(set2)

# In-place union
set1 |= set2  # Modifies set1
```

### Intersection
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using & operator
intersection = set1 & set2  # {3, 4}

# Using intersection() method
intersection = set1.intersection(set2)

# In-place intersection
set1 &= set2  # Modifies set1
```

### Difference
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using - operator
difference = set1 - set2  # {1, 2}

# Using difference() method
difference = set1.difference(set2)

# In-place difference
set1 -= set2  # Modifies set1
```

### Symmetric Difference
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using ^ operator
symmetric_diff = set1 ^ set2  # {1, 2, 5, 6}

# Using symmetric_difference() method
symmetric_diff = set1.symmetric_difference(set2)

# In-place symmetric difference
set1 ^= set2  # Modifies set1
```

## Set Methods

### Adding Elements
```python
fruits = {"apple", "banana"}

# add() - adds single element
fruits.add("orange")

# update() - adds multiple elements
fruits.update(["grape", "kiwi"])
fruits.update({"mango", "pineapple"})
```

### Removing Elements
```python
fruits = {"apple", "banana", "orange", "grape"}

# remove() - removes element (raises KeyError if not found)
fruits.remove("banana")

# discard() - removes element (no error if not found)
fruits.discard("kiwi")

# pop() - removes and returns arbitrary element
popped = fruits.pop()

# clear() - removes all elements
fruits.clear()
```

### Set Comparison
```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4}
set3 = {1, 2, 3}

# issubset() and <=
set1.issubset(set2)  # True
set1 <= set2         # True

# issuperset() and >=
set2.issuperset(set1)  # True
set2 >= set1           # True

# isdisjoint() - no common elements
set1.isdisjoint({4, 5, 6})  # True
```

## Set Comprehension
```python
# Basic comprehension
squares = {x**2 for x in range(5)}

# With condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}

# From existing set
fruits = {"apple", "banana", "orange"}
upper_fruits = {fruit.upper() for fruit in fruits}

# Complex comprehension
vowels = {'a', 'e', 'i', 'o', 'u'}
text = "hello world"
consonants = {char for char in text if char.isalpha() and char not in vowels}
```

## Frozen Sets
```python
# Frozen sets are immutable
frozen_fruits = frozenset(["apple", "banana", "orange"])

# Frozen sets can be used as dictionary keys
set_dict = {frozen_fruits: "fruit set"}

# Frozen sets support set operations
set1 = frozenset([1, 2, 3])
set2 = frozenset([3, 4, 5])
union = set1 | set2  # Returns a frozenset
```

## Common Use Cases

### Removing Duplicates
```python
# From list
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_numbers = list(set(numbers))

# From string
text = "hello world"
unique_chars = set(text)
```

### Finding Common Elements
```python
# Students in both classes
math_students = {"Alice", "Bob", "Charlie", "Diana"}
science_students = {"Bob", "Diana", "Eve", "Frank"}

both_classes = math_students & science_students
print(f"Students in both classes: {both_classes}")
```

### Finding Unique Elements
```python
# Elements in either class but not both
either_class = math_students ^ science_students
print(f"Students in only one class: {either_class}")
```

### Data Validation
```python
# Valid categories
valid_categories = {"electronics", "clothing", "books", "sports"}

def validate_category(category):
    return category in valid_categories

print(validate_category("electronics"))  # True
print(validate_category("food"))        # False
```

## Performance Considerations
```python
# Set membership is O(1) - very fast
large_set = set(range(1000000))
# 500000 in large_set  # Very fast lookup

# Sets use more memory than lists
# But provide faster lookups

# Use cases:
# - When you need unique elements
# - When you need fast membership testing
# - When you need set operations
```

## Built-in Functions with Sets
```python
fruits = {"apple", "banana", "orange"}

len(fruits)      # 3
max(fruits)      # 'orange' (alphabetical)
min(fruits)      # 'apple'
any(fruits)      # True
all(fruits)      # True

# sorted() with sets
sorted_fruits = sorted(fruits)  # Returns list
```

## Set vs List vs Tuple
```python
# When to use sets:
# - Need unique elements
# - Need fast membership testing
# - Need set operations

# When to use lists:
# - Need ordered collection
# - Need to modify elements
# - Need to access by index

# When to use tuples:
# - Need immutable collection
# - Need ordered collection
# - Need to use as dictionary key
```

## Best Practices
```python
# 1. Use sets for unique collections
unique_tags = set(["python", "programming", "tutorial", "python"])

# 2. Use sets for fast membership testing
valid_users = {"alice", "bob", "charlie"}
if username in valid_users:
    print("Valid user")

# 3. Use set operations for data analysis
completed_tasks = {"task1", "task2", "task4"}
all_tasks = {"task1", "task2", "task3", "task4"}
pending_tasks = all_tasks - completed_tasks

# 4. Use set comprehension for transformations
numbers = {1, 2, 3, 4, 5}
squares = {x**2 for x in numbers}
```

## Practice Examples
See `practice.py` for hands-on exercises with sets! 