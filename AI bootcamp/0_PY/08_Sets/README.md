# Python Sets

## Overview
Sets in Python are unordered collections of unique elements. They are mutable and support mathematical set operations like union, intersection, and difference.

## Course Structure

This course is organized into focused modules for better learning:

### 1. Basic Operations
- **`01_set_creation.py`** - Creating sets using various methods
- **`02_set_properties.py`** - Set properties and characteristics
- **`03_set_operations.py`** - Adding, removing, and modifying set elements

### 2. Advanced Operations
- **`04_set_membership.py`** - Membership testing and boolean operations
- **`05_mathematical_set_operations.py`** - Union, intersection, difference operations
- **`06_set_methods.py`** - Set methods and comparison operations

### 3. Special Features
- **`07_set_comprehension.py`** - Set comprehensions and transformations
- **`08_frozen_sets.py`** - Immutable frozen sets
- **`09_builtin_functions_sets.py`** - Built-in functions working with sets

### 4. Practice Problems
- **`10_practice_problems_1.py`** - Basic practice problems with sets
- **`11_practice_problems_2.py`** - Advanced problems including caching and validation

## How to Use This Course

### Running Individual Files
Each file can be run independently to focus on specific concepts:

```bash
# Run set creation
python 01_set_creation.py

# Run set properties
python 02_set_properties.py

# Run set operations
python 03_set_operations.py

# And so on for each file...
```

### Learning Path
1. Start with `01_set_creation.py` to understand set basics
2. Move to `02_set_properties.py` and `03_set_operations.py` for core operations
3. Study `04_set_membership.py` and `05_mathematical_set_operations.py` for advanced usage
4. Learn about `06_set_methods.py` for method usage
5. Explore `07_set_comprehension.py` for transformations
6. Understand `08_frozen_sets.py` for immutable sets
7. Practice with `09_builtin_functions_sets.py` for built-in function usage
8. Practice with `10_practice_problems_1.py` and `11_practice_problems_2.py`

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
union = set1 | set2  # Returns a regular set
```

## Built-in Functions with Sets
```python
fruits = {"apple", "banana", "orange"}

len(fruits)      # 3
max(fruits)      # 'orange' (lexicographic)
min(fruits)      # 'apple'
any(fruits)      # True
all(fruits)      # True

# sorted() with sets
sorted_fruits = sorted(fruits)  # ['apple', 'banana', 'orange']
```

## Common Use Cases

### Removing Duplicates
```python
# Remove duplicates from list
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)  # [1, 2, 3, 4, 5]
```

### Finding Common Elements
```python
# Find common elements between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(common)  # [4, 5]
```

### Set Operations for Data Analysis
```python
# Students in different classes
math_students = {"Alice", "Bob", "Charlie", "Diana"}
science_students = {"Bob", "Diana", "Eve", "Frank"}

# Students taking both classes
both_classes = math_students & science_students

# Students taking only math
only_math = math_students - science_students

# All students
all_students = math_students | science_students
```

### Performance Considerations
```python
# Sets are very fast for membership testing
import time

large_set = set(range(1000000))
large_list = list(range(1000000))

# Set membership test
start = time.time()
for i in range(1000):
    _ = i in large_set
end = time.time()
print(f"Set membership: {end - start:.6f} seconds")

# List membership test
start = time.time()
for i in range(1000):
    _ = i in large_list
end = time.time()
print(f"List membership: {end - start:.6f} seconds")
```

## Practice Examples
Each file contains hands-on exercises with sets! Start with the basic files and work your way up to the practice problems. 