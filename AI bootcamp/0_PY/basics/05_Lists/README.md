# Lists in Python

This folder covers Python lists - ordered, mutable collections that are fundamental to Python programming.

## Course Structure

### 1. List Creation (`01_list_creation.py`)
- **Topics Covered**: Creating lists, list literals, list constructor, nested lists
- **Learning Objectives**: 
  - Create lists using different methods
  - Understand list structure
  - Work with nested lists
- **Run Command**: `python 01_list_creation.py`

### 2. List Operations (`02_list_operations.py`)
- **Topics Covered**: Indexing, slicing, concatenation, repetition
- **Learning Objectives**:
  - Access list elements
  - Extract sublists
  - Combine lists
- **Run Command**: `python 02_list_operations.py`

### 3. List Methods (`03_list_methods.py`)
- **Topics Covered**: append(), extend(), insert(), remove(), pop(), clear()
- **Learning Objectives**:
  - Modify lists using methods
  - Add and remove elements
  - Understand method behavior
- **Run Command**: `python 03_list_methods.py`

### 4. List Slicing (`04_list_slicing.py`)
- **Topics Covered**: Advanced slicing, step parameter, negative indices
- **Learning Objectives**:
  - Use advanced slicing techniques
  - Understand slice notation
  - Manipulate list portions
- **Run Command**: `python 04_list_slicing.py`

### 5. List Comprehension (`05_list_comprehension.py`)
- **Topics Covered**: List comprehensions, conditional comprehensions, nested comprehensions
- **Learning Objectives**:
  - Create lists efficiently
  - Use conditional logic in comprehensions
  - Write readable list operations
- **Run Command**: `python 05_list_comprehension.py`

### 6. List Sorting (`06_list_sorting.py`)
- **Topics Covered**: sort(), sorted(), reverse(), key functions, custom sorting
- **Learning Objectives**:
  - Sort lists effectively
  - Use custom sorting criteria
  - Understand sorting algorithms
- **Run Command**: `python 06_list_sorting.py`

### 7. List Searching (`07_list_searching.py`)
- **Topics Covered**: in operator, index(), count(), find methods
- **Learning Objectives**:
  - Search for elements in lists
  - Count occurrences
  - Find element positions
- **Run Command**: `python 07_list_searching.py`

### 8. Built-in Functions (`08_built_in_functions.py`)
- **Topics Covered**: len(), max(), min(), sum(), any(), all()
- **Learning Objectives**:
  - Use built-in functions with lists
  - Calculate list statistics
  - Check list properties
- **Run Command**: `python 08_built_in_functions.py`

### 9. List Patterns (`09_list_patterns.py`)
- **Topics Covered**: Common list patterns, best practices, performance tips
- **Learning Objectives**:
  - Use common list patterns
  - Write efficient list code
  - Follow best practices
- **Run Command**: `python 09_list_patterns.py`

### 10. Practice Problems (`10_practice_problems.py`)
- **Topics Covered**: Comprehensive exercises covering all list concepts
- **Learning Objectives**:
  - Apply list operations to real problems
  - Practice list manipulation
  - Build problem-solving skills
- **Run Command**: `python 10_practice_problems.py`

## Key Concepts

### List Properties
- **Ordered**: Elements maintain their order
- **Mutable**: Can be changed after creation
- **Indexed**: Access elements by position (0-based)
- **Heterogeneous**: Can contain different data types

### Common List Methods
- `.append(x)` - Add element to end
- `.extend(iterable)` - Add all elements from iterable
- `.insert(i, x)` - Insert element at position i
- `.remove(x)` - Remove first occurrence of x
- `.pop([i])` - Remove and return element at position i
- `.clear()` - Remove all elements
- `.sort()` - Sort list in place
- `.reverse()` - Reverse list in place

### List Comprehension Syntax
```python
# Basic: [expression for item in iterable]
squares = [x**2 for x in range(10)]

# Conditional: [expression for item in iterable if condition]
evens = [x for x in range(10) if x % 2 == 0]

# Nested: [expression for item1 in iterable1 for item2 in iterable2]
pairs = [(x, y) for x in [1, 2] for y in ['a', 'b']]
```

## Common Patterns

### List Creation
```python
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]
```

### List Operations
```python
numbers = [1, 2, 3, 4, 5]
first = numbers[0]  # 1
last = numbers[-1]  # 5
subset = numbers[1:4]  # [2, 3, 4]
reversed_list = numbers[::-1]  # [5, 4, 3, 2, 1]
```

### List Methods
```python
fruits = ["apple", "banana"]
fruits.append("orange")  # ["apple", "banana", "orange"]
fruits.insert(1, "grape")  # ["apple", "grape", "banana", "orange"]
fruits.remove("banana")  # ["apple", "grape", "orange"]
last_fruit = fruits.pop()  # "orange"
```

## Best Practices

1. **Use list comprehensions**: More readable than loops for simple operations
2. **Avoid modifying while iterating**: Use copy or iterate backwards
3. **Use appropriate methods**: Choose the right method for the task
4. **Consider performance**: Some operations are more efficient than others
5. **Use meaningful variable names**: `user_names` instead of `l`

## Common Mistakes

1. **Modifying list while iterating**: Can cause unexpected behavior
2. **Confusing sort() and sorted()**: sort() modifies, sorted() returns new list
3. **Forgetting list mutability**: Lists are changed in place
4. **Using wrong index**: Remember 0-based indexing

## Next Steps

After mastering lists, continue with:
- **Tuples** (`../06_Tuples/`) - Immutable sequences
- **Dictionaries** (`../07_Dictionaries/`) - Key-value pairs
- **Sets** (`../08_Sets/`) - Unordered collections

## Advanced Topics

- **List performance**: Understanding time complexity
- **Memory management**: How lists use memory
- **List vs other collections**: When to use different data structures
- **Functional programming**: Using lists with map, filter, reduce

## Resources

- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [List Methods](https://docs.python.org/3/library/stdtypes.html#list)
- [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

Happy list processing! 📋 