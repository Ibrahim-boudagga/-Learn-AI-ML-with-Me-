# Tuples in Python

This folder covers Python tuples - immutable, ordered sequences that are useful for data that shouldn't change.

## Course Structure

### 1. Tuple Creation (`01_tuple_creation.py`)
- **Topics Covered**: Creating tuples, tuple literals, single-element tuples, nested tuples
- **Learning Objectives**: 
  - Create tuples using different methods
  - Understand tuple syntax
  - Work with nested tuples
- **Run Command**: `python 01_tuple_creation.py`

### 2. Tuple Operations (`02_tuple_operations.py`)
- **Topics Covered**: Indexing, slicing, concatenation, repetition, unpacking
- **Learning Objectives**:
  - Access tuple elements
  - Extract subtuples
  - Unpack tuple values
- **Run Command**: `python 02_tuple_operations.py`

### 3. Tuple Methods (`03_tuple_methods.py`)
- **Topics Covered**: count(), index(), tuple-specific operations
- **Learning Objectives**:
  - Use tuple methods effectively
  - Search within tuples
  - Understand tuple limitations
- **Run Command**: `python 03_tuple_methods.py`

### 4. Tuple Unpacking (`04_tuple_unpacking.py`)
- **Topics Covered**: Basic unpacking, extended unpacking, multiple assignment
- **Learning Objectives**:
  - Unpack tuple values
  - Use extended unpacking
  - Return multiple values from functions
- **Run Command**: `python 04_tuple_unpacking.py`

### 5. Named Tuples (`05_named_tuples.py`)
- **Topics Covered**: collections.namedtuple, field access, named tuple methods
- **Learning Objectives**:
  - Create named tuples
  - Access fields by name
  - Use named tuples for data structures
- **Run Command**: `python 05_named_tuples.py`

### 6. Tuple vs List (`06_tuple_vs_list.py`)
- **Topics Covered**: Immutability, performance, use cases, when to use each
- **Learning Objectives**:
  - Understand differences between tuples and lists
  - Choose appropriate data structure
  - Consider performance implications
- **Run Command**: `python 06_tuple_vs_list.py`

### 7. Built-in Functions (`07_built_in_functions.py`)
- **Topics Covered**: len(), max(), min(), sum(), any(), all() with tuples
- **Learning Objectives**:
  - Use built-in functions with tuples
  - Calculate tuple statistics
  - Check tuple properties
- **Run Command**: `python 07_built_in_functions.py`

### 8. Tuple Patterns (`08_tuple_patterns.py`)
- **Topics Covered**: Common tuple patterns, best practices, tuple idioms
- **Learning Objectives**:
  - Use common tuple patterns
  - Write efficient tuple code
  - Follow Python idioms
- **Run Command**: `python 08_tuple_patterns.py`

### 9. Practice Problems (`09_practice_problems.py`)
- **Topics Covered**: Comprehensive exercises covering all tuple concepts
- **Learning Objectives**:
  - Apply tuple operations to real problems
  - Practice tuple manipulation
  - Build problem-solving skills
- **Run Command**: `python 09_practice_problems.py`

## Key Concepts

### Tuple Properties
- **Immutable**: Cannot be changed after creation
- **Ordered**: Elements maintain their order
- **Indexed**: Access elements by position (0-based)
- **Heterogeneous**: Can contain different data types

### Tuple Methods
- `.count(x)` - Count occurrences of x
- `.index(x)` - Find first occurrence of x
- Limited methods due to immutability

### Tuple Unpacking
```python
# Basic unpacking
x, y, z = (1, 2, 3)

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)

# Multiple assignment
a, b = b, a  # Swap values
```

## Common Patterns

### Tuple Creation
```python
empty_tuple = ()
single_element = (42,)  # Note the comma
coordinates = (10, 20)
person = ("Alice", 25, "Engineer")
```

### Tuple Operations
```python
point = (3, 4)
x, y = point  # Unpacking
distance = (x**2 + y**2)**0.5

# Multiple return values
def get_name_age():
    return ("Bob", 30)

name, age = get_name_age()
```

### Named Tuples
```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)  # 10 20
```

## Best Practices

1. **Use tuples for immutable data**: Coordinates, configuration, return values
2. **Use named tuples for structured data**: Better than regular tuples for complex data
3. **Leverage unpacking**: Clean way to assign multiple variables
4. **Consider performance**: Tuples are slightly more efficient than lists
5. **Use for function returns**: Return multiple values cleanly

## Common Mistakes

1. **Trying to modify tuples**: Tuples are immutable
2. **Forgetting comma for single-element tuples**: `(42)` is not a tuple
3. **Confusing with lists**: Different use cases and behaviors
4. **Not using unpacking**: More verbose than necessary

## When to Use Tuples

### Use Tuples For:
- **Coordinates**: `(x, y)` positions
- **Return values**: Multiple values from functions
- **Dictionary keys**: Immutable, hashable
- **Data records**: Fixed structure data
- **Configuration**: Immutable settings

### Use Lists For:
- **Dynamic collections**: Data that changes
- **Sequences to modify**: Adding/removing elements
- **Iteration with modification**: Processing with changes

## Next Steps

After mastering tuples, continue with:
- **Dictionaries** (`../07_Dictionaries/`) - Key-value pairs
- **Sets** (`../08_Sets/`) - Unordered collections
- **Functions** (`../11_Functions/`) - Reusable code blocks

## Advanced Topics

- **Tuple performance**: Memory and speed advantages
- **Tuple unpacking patterns**: Advanced unpacking techniques
- **Named tuples vs classes**: When to use each
- **Tuple as dictionary keys**: Hashable nature

## Resources

- [Python Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Named Tuples](https://docs.python.org/3/library/collections.html#collections.namedtuple)
- [Tuple Methods](https://docs.python.org/3/library/stdtypes.html#tuple)

Happy tuple processing! 📦 