# Sets in Python

This folder covers Python sets - unordered collections of unique elements, perfect for mathematical operations and data deduplication.

## Course Structure

### 1. Set Creation (`01_set_creation.py`)
- **Topics Covered**: Creating sets, set constructor, set literals, empty sets
- **Learning Objectives**: 
  - Create sets using different methods
  - Understand set properties
  - Work with set literals
- **Run Command**: `python 01_set_creation.py`

### 2. Set Operations (`02_set_operations.py`)
- **Topics Covered**: Adding/removing elements, membership testing, set size
- **Learning Objectives**:
  - Modify set contents
  - Check membership efficiently
  - Understand set mutability
- **Run Command**: `python 02_set_operations.py`

### 3. Set Methods (`03_set_methods.py`)
- **Topics Covered**: add(), remove(), discard(), pop(), clear(), copy()
- **Learning Objectives**:
  - Use set methods effectively
  - Safely modify sets
  - Understand method differences
- **Run Command**: `python 03_set_methods.py`

### 4. Mathematical Operations (`04_mathematical_operations.py`)
- **Topics Covered**: Union, intersection, difference, symmetric difference
- **Learning Objectives**:
  - Perform set mathematics
  - Combine sets in different ways
  - Understand set algebra
- **Run Command**: `python 04_mathematical_operations.py`

### 5. Set Comprehension (`05_set_comprehension.py`)
- **Topics Covered**: Set comprehensions, conditional comprehensions
- **Learning Objectives**:
  - Create sets efficiently
  - Use conditional logic in comprehensions
  - Transform data into sets
- **Run Command**: `python 05_set_comprehension.py`

### 6. Frozen Sets (`06_frozen_sets.py`)
- **Topics Covered**: Immutable sets, frozenset constructor, use cases
- **Learning Objectives**:
  - Create immutable sets
  - Use frozen sets as dictionary keys
  - Understand immutability benefits
- **Run Command**: `python 06_frozen_sets.py`

### 7. Built-in Functions (`07_built_in_functions.py`)
- **Topics Covered**: len(), max(), min(), sum(), any(), all() with sets
- **Learning Objectives**:
  - Use built-in functions with sets
  - Calculate set statistics
  - Check set properties
- **Run Command**: `python 07_built_in_functions.py`

### 8. Practice Problems (`08_practice_problems.py`)
- **Topics Covered**: Comprehensive exercises covering all set concepts
- **Learning Objectives**:
  - Apply set operations to real problems
  - Practice set manipulation
  - Build problem-solving skills
- **Run Command**: `python 08_practice_problems.py`

## Key Concepts

### Set Properties
- **Unordered**: Elements don't maintain order
- **Unique**: No duplicate elements
- **Mutable**: Can be changed after creation (except frozenset)
- **Hashable elements**: All elements must be hashable
- **Fast membership testing**: O(1) average case

### Common Set Methods
- `.add(element)` - Add element to set
- `.remove(element)` - Remove element (raises KeyError if missing)
- `.discard(element)` - Remove element (no error if missing)
- `.pop()` - Remove and return arbitrary element
- `.clear()` - Remove all elements
- `.copy()` - Create shallow copy

### Mathematical Operations
- **Union**: `set1 | set2` or `set1.union(set2)`
- **Intersection**: `set1 & set2` or `set1.intersection(set2)`
- **Difference**: `set1 - set2` or `set1.difference(set2)`
- **Symmetric Difference**: `set1 ^ set2` or `set1.symmetric_difference(set2)`

### Set Comprehension
```python
# Basic: {expression for item in iterable}
squares = {x**2 for x in range(10)}

# Conditional: {expression for item in iterable if condition}
even_squares = {x**2 for x in range(10) if x % 2 == 0}

# From existing set: {expression for item in set}
doubled = {x * 2 for x in numbers}
```

## Common Patterns

### Set Creation
```python
empty_set = set()
numbers = {1, 2, 3, 4, 5}
letters = set("hello")  # {'h', 'e', 'l', 'o'}
unique_words = set(["apple", "banana", "apple"])  # {'apple', 'banana'}
```

### Set Operations
```python
fruits = {"apple", "banana", "orange"}
fruits.add("grape")  # Add element
fruits.remove("banana")  # Remove element
"apple" in fruits  # Membership test
len(fruits)  # Set size
```

### Mathematical Operations
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union = set1 | set2  # {1, 2, 3, 4, 5, 6}
intersection = set1 & set2  # {3, 4}
difference = set1 - set2  # {1, 2}
symmetric_diff = set1 ^ set2  # {1, 2, 5, 6}
```

## Best Practices

1. **Use sets for uniqueness**: Perfect for removing duplicates
2. **Use for membership testing**: Faster than lists for large data
3. **Use mathematical operations**: Clean way to combine data
4. **Choose appropriate methods**: remove() vs discard() based on needs
5. **Consider frozen sets**: When immutability is needed

## Common Mistakes

1. **Expecting order**: Sets are unordered
2. **Using unhashable elements**: Lists and dicts can't be in sets
3. **Confusing with lists**: Different use cases and behaviors
4. **Ignoring return values**: Methods often return useful information

## When to Use Sets

### Use Sets For:
- **Removing duplicates**: Unique elements only
- **Membership testing**: Fast "in" operations
- **Mathematical operations**: Union, intersection, etc.
- **Finding differences**: What's in one but not another
- **Efficient lookups**: When order doesn't matter

### Use Other Structures For:
- **Ordered data**: Lists or tuples
- **Key-value pairs**: Dictionaries
- **Indexed access**: Lists or arrays

## Next Steps

After mastering sets, continue with:
- **Conditionals** (`../09_Conditionals/`) - Decision making
- **Loops** (`../10_Loops/`) - Iteration and repetition
- **Functions** (`../11_Functions/`) - Reusable code blocks

## Advanced Topics

- **Set performance**: Understanding hash-based operations
- **Set vs other collections**: When to use each
- **Frozen sets**: Immutable set variants
- **Set algebra**: Mathematical set theory

## Resources

- [Python Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Set Methods](https://docs.python.org/3/library/stdtypes.html#set)
- [Set Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#sets)

Happy set processing! 🎯 