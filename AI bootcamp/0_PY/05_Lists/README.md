# Python Lists

## Overview
Lists in Python are ordered, mutable collections of items. They can contain elements of different data types and are one of the most commonly used data structures.

## List Creation
```python
# Empty list
empty_list = []

# List with elements
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "hello", 3.14, True]

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Using list() constructor
list_from_range = list(range(5))  # [0, 1, 2, 3, 4]
list_from_string = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
```

## List Indexing and Slicing
```python
fruits = ["apple", "banana", "orange", "grape", "kiwi"]

# Indexing (starts from 0)
first_fruit = fruits[0]      # "apple"
last_fruit = fruits[-1]      # "kiwi"
second_fruit = fruits[1]     # "banana"

# Slicing [start:end:step]
first_two = fruits[0:2]      # ["apple", "banana"]
last_three = fruits[-3:]     # ["orange", "grape", "kiwi"]
every_second = fruits[::2]   # ["apple", "orange", "kiwi"]
reverse = fruits[::-1]       # ["kiwi", "grape", "orange", "banana", "apple"]
```

## List Methods

### Adding Elements
```python
numbers = [1, 2, 3]

# append() - adds element to the end
numbers.append(4)  # [1, 2, 3, 4]

# insert() - inserts element at specific position
numbers.insert(1, 1.5)  # [1, 1.5, 2, 3, 4]

# extend() - adds all elements from another list
numbers.extend([5, 6])  # [1, 1.5, 2, 3, 4, 5, 6]

# + operator - creates new list
new_numbers = numbers + [7, 8]  # [1, 1.5, 2, 3, 4, 5, 6, 7, 8]
```

### Removing Elements
```python
numbers = [1, 2, 3, 2, 4, 2, 5]

# remove() - removes first occurrence of value
numbers.remove(2)  # [1, 3, 2, 4, 2, 5]

# pop() - removes and returns element at index
popped = numbers.pop(1)  # popped = 3, numbers = [1, 2, 4, 2, 5]

# del statement - removes element at index
del numbers[0]  # [2, 4, 2, 5]

# clear() - removes all elements
numbers.clear()  # []
```

### Finding Elements
```python
fruits = ["apple", "banana", "orange", "apple"]

# index() - returns index of first occurrence
apple_index = fruits.index("apple")  # 0

# count() - counts occurrences
apple_count = fruits.count("apple")  # 2

# in operator - checks if element exists
has_banana = "banana" in fruits  # True
has_grape = "grape" in fruits    # False
```

### Sorting and Reversing
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() - sorts in place
numbers.sort()  # [1, 1, 2, 3, 4, 5, 6, 9]

# sort() with reverse=True
numbers.sort(reverse=True)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() - returns new sorted list
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)  # [1, 1, 3, 4, 5]

# reverse() - reverses in place
numbers.reverse()  # [1, 1, 2, 3, 4, 5, 6, 9]
```

## List Operations

### Concatenation
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using + operator
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]

# Using extend()
list1.extend(list2)  # list1 becomes [1, 2, 3, 4, 5, 6]
```

### Repetition
```python
numbers = [1, 2, 3]

# Using * operator
repeated = numbers * 3  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### Comparison
```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]

list1 == list2  # True
list1 == list3  # False
list1 < list3   # True (lexicographic comparison)
```

## List Comprehension
```python
# Basic comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]

# Nested comprehension
matrix = [[i+j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# Dictionary comprehension
word_lengths = {word: len(word) for word in ["apple", "banana", "orange"]}
# {'apple': 5, 'banana': 6, 'orange': 6}
```

## Built-in Functions with Lists
```python
numbers = [1, 2, 3, 4, 5]

len(numbers)      # 5
max(numbers)      # 5
min(numbers)      # 1
sum(numbers)      # 15
any(numbers)      # True (any non-zero is True)
all(numbers)      # True (all non-zero)

# enumerate() - returns index-value pairs
for index, value in enumerate(numbers):
    print(f"Index {index}: {value}")

# zip() - combines multiple lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

## Common List Patterns

### Filtering
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Using list comprehension
even_numbers = [x for x in numbers if x % 2 == 0]
```

### Mapping
```python
numbers = [1, 2, 3, 4, 5]

# Using map()
squares = list(map(lambda x: x**2, numbers))

# Using list comprehension
squares = [x**2 for x in numbers]
```

### Flattening
```python
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Using nested loops
flattened = [item for sublist in nested for item in sublist]

# Using itertools
from itertools import chain
flattened = list(chain.from_iterable(nested))
```

## List Performance Tips
```python
# Use append() instead of + for single elements
# Good
numbers = []
for i in range(1000):
    numbers.append(i)

# Bad
numbers = []
for i in range(1000):
    numbers = numbers + [i]

# Use list comprehension for simple transformations
# Good
squares = [x**2 for x in range(1000)]

# Bad
squares = []
for x in range(1000):
    squares.append(x**2)
```

## Common Use Cases
```python
# Stack (LIFO)
stack = []
stack.append(1)  # push
stack.append(2)
stack.append(3)
last_item = stack.pop()  # pop

# Queue (FIFO)
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)  # enqueue
first_item = queue.popleft()  # dequeue

# Matrix operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = list(zip(*matrix))

# Data processing
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
names = [name for name, age in data]
ages = [age for name, age in data]
```

## Practice Examples
See `practice.py` for hands-on exercises with lists! 