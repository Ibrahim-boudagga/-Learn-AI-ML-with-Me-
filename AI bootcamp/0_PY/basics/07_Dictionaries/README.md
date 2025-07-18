# Dictionaries in Python

This folder covers Python dictionaries - key-value pairs that provide fast lookup and flexible data storage.

## Course Structure

### 1. Dictionary Creation (`01_dictionary_creation.py`)
- **Topics Covered**: Creating dictionaries, dict constructor, nested dictionaries
- **Learning Objectives**: 
  - Create dictionaries using different methods
  - Understand key-value structure
  - Work with nested dictionaries
- **Run Command**: `python 01_dictionary_creation.py`

### 2. Dictionary Operations (`02_dictionary_operations.py`)
- **Topics Covered**: Accessing values, adding/updating items, removing items
- **Learning Objectives**:
  - Access dictionary values
  - Modify dictionary contents
  - Handle missing keys
- **Run Command**: `python 02_dictionary_operations.py`

### 3. Dictionary Methods (`03_dictionary_methods.py`)
- **Topics Covered**: get(), setdefault(), update(), pop(), clear(), copy()
- **Learning Objectives**:
  - Use dictionary methods effectively
  - Safely access dictionary values
  - Manipulate dictionary data
- **Run Command**: `python 03_dictionary_methods.py`

### 4. Dictionary Views (`04_dictionary_views.py`)
- **Topics Covered**: keys(), values(), items(), view objects, iteration
- **Learning Objectives**:
  - Use dictionary views
  - Iterate over dictionaries
  - Understand view behavior
- **Run Command**: `python 04_dictionary_views.py`

### 5. Dictionary Comprehension (`05_dictionary_comprehension.py`)
- **Topics Covered**: Dictionary comprehensions, conditional comprehensions
- **Learning Objectives**:
  - Create dictionaries efficiently
  - Use conditional logic in comprehensions
  - Transform data structures
- **Run Command**: `python 05_dictionary_comprehension.py`

### 6. Dictionary Patterns (`06_dictionary_patterns.py`)
- **Topics Covered**: Common patterns, best practices, dictionary idioms
- **Learning Objectives**:
  - Use common dictionary patterns
  - Write efficient dictionary code
  - Follow Python idioms
- **Run Command**: `python 06_dictionary_patterns.py`

### 7. Built-in Functions (`07_built_in_functions.py`)
- **Topics Covered**: len(), max(), min(), sum(), any(), all() with dictionaries
- **Learning Objectives**:
  - Use built-in functions with dictionaries
  - Calculate dictionary statistics
  - Check dictionary properties
- **Run Command**: `python 07_built_in_functions.py`

### 8. Practice Problems (`08_practice_problems.py`)
- **Topics Covered**: Comprehensive exercises covering all dictionary concepts
- **Learning Objectives**:
  - Apply dictionary operations to real problems
  - Practice data structure manipulation
  - Build problem-solving skills
- **Run Command**: `python 08_practice_problems.py`

## Key Concepts

### Dictionary Properties
- **Key-Value Pairs**: Each item has a key and associated value
- **Mutable**: Can be changed after creation
- **Unordered**: Keys don't maintain order (Python 3.7+ preserves insertion order)
- **Keys must be hashable**: Strings, numbers, tuples (immutable)
- **Values can be anything**: Any Python object

### Common Dictionary Methods
- `.get(key, default)` - Safely get value with default
- `.setdefault(key, default)` - Get value, set if missing
- `.update(other_dict)` - Update with another dictionary
- `.pop(key, default)` - Remove and return value
- `.clear()` - Remove all items
- `.copy()` - Create shallow copy
- `.keys()`, `.values()`, `.items()` - Get views

### Dictionary Comprehension
```python
# Basic: {key: value for item in iterable}
squares = {x: x**2 for x in range(5)}

# Conditional: {key: value for item in iterable if condition}
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

# From existing dict: {key: value for key, value in dict.items()}
uppercase = {k.upper(): v for k, v in data.items()}
```

## Common Patterns

### Dictionary Creation
```python
empty_dict = {}
person = {"name": "Alice", "age": 30, "city": "New York"}
config = dict(debug=True, timeout=30, max_connections=100)
```

### Dictionary Operations
```python
user = {"name": "Bob", "age": 25}
name = user["name"]  # Direct access
age = user.get("age", 0)  # Safe access with default
user["email"] = "bob@example.com"  # Add new key
user["age"] = 26  # Update existing key
```

### Dictionary Methods
```python
data = {"a": 1, "b": 2}
value = data.get("c", 0)  # Safe access
data.setdefault("d", 3)  # Set if missing
data.update({"e": 4, "f": 5})  # Add multiple items
removed = data.pop("a")  # Remove and return
```

## Best Practices

1. **Use .get() for safe access**: Avoid KeyError exceptions
2. **Use .setdefault() for counters**: Efficient counting patterns
3. **Use dictionary comprehensions**: More readable than loops
4. **Choose meaningful keys**: Descriptive key names
5. **Consider performance**: Dictionaries are fast for lookups

## Common Mistakes

1. **Accessing non-existent keys**: Use .get() or check with 'in'
2. **Modifying during iteration**: Create copy or use different approach
3. **Using mutable keys**: Keys must be hashable
4. **Ignoring return values**: Methods often return useful information

## When to Use Dictionaries

### Use Dictionaries For:
- **Lookup tables**: Fast key-based access
- **Configuration data**: Settings and parameters
- **Data aggregation**: Counting and grouping
- **Object-like data**: Structured information
- **Caching**: Storing computed results

### Use Other Structures For:
- **Ordered sequences**: Lists or tuples
- **Unique collections**: Sets
- **Simple key-value with order**: OrderedDict

## Next Steps

After mastering dictionaries, continue with:
- **Sets** (`../08_Sets/`) - Unordered unique collections
- **Functions** (`../11_Functions/`) - Reusable code blocks
- **Modules** (`../12_Modules_Packages/`) - Code organization

## Advanced Topics

- **Dictionary performance**: Understanding hash tables
- **Nested dictionaries**: Complex data structures
- **DefaultDict**: Automatic default values
- **OrderedDict**: Maintaining insertion order

## Resources

- [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Dictionary Methods](https://docs.python.org/3/library/stdtypes.html#dict)
- [Dictionary Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

Happy dictionary processing! 📚 