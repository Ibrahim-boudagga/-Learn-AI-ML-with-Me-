# Strings in Python

This folder covers Python string manipulation, formatting, and operations - essential for text processing and data handling.

## Course Structure

### 1. String Creation (`01_string_creation.py`)
- **Topics Covered**: String literals, quotes, escape sequences, raw strings
- **Learning Objectives**: 
  - Create strings using different methods
  - Use escape sequences properly
  - Understand raw strings
- **Run Command**: `python 01_string_creation.py`

### 2. String Operations (`02_string_operations.py`)
- **Topics Covered**: Concatenation, repetition, indexing, slicing
- **Learning Objectives**:
  - Combine strings effectively
  - Access string characters
  - Extract substrings
- **Run Command**: `python 02_string_operations.py`

### 3. String Methods (`03_string_methods.py`)
- **Topics Covered**: Case conversion, searching, replacing, splitting, joining
- **Learning Objectives**:
  - Use built-in string methods
  - Manipulate text effectively
  - Transform string data
- **Run Command**: `python 03_string_methods.py`

### 4. String Formatting (`04_string_formatting.py`)
- **Topics Covered**: f-strings, format() method, % operator, placeholders
- **Learning Objectives**:
  - Format strings dynamically
  - Insert variables into strings
  - Control output formatting
- **Run Command**: `python 04_string_formatting.py`

### 5. String Validation (`05_string_validation.py`)
- **Topics Covered**: Checking string properties, validation methods, patterns
- **Learning Objectives**:
  - Validate string content
  - Check string properties
  - Use validation methods
- **Run Command**: `python 05_string_validation.py`

### 6. String Manipulation (`06_string_manipulation.py`)
- **Topics Covered**: Advanced manipulation, text processing, custom functions
- **Learning Objectives**:
  - Process text data
  - Create custom string functions
  - Handle complex text operations
- **Run Command**: `python 06_string_manipulation.py`

### 7. Regular Expressions (`07_regular_expressions.py`)
- **Topics Covered**: re module, patterns, matching, searching, replacing
- **Learning Objectives**:
  - Use regular expressions
  - Match patterns in text
  - Extract information from strings
- **Run Command**: `python 07_regular_expressions.py`

### 8. Built-in Functions (`08_built_in_functions.py`)
- **Topics Covered**: len(), ord(), chr(), str(), eval(), repr()
- **Learning Objectives**:
  - Use string-related built-in functions
  - Convert between types
  - Understand function behavior
- **Run Command**: `python 08_built_in_functions.py`

### 9. Practice Problems (`09_practice_problems.py`)
- **Topics Covered**: Comprehensive exercises covering all string concepts
- **Learning Objectives**:
  - Apply string operations to real problems
  - Practice text processing
  - Build string manipulation skills
- **Run Command**: `python 09_practice_problems.py`

## Key Concepts

### String Properties
- **Immutable**: Strings cannot be changed after creation
- **Indexed**: Access characters by position (0-based)
- **Sliced**: Extract substrings using slice notation
- **Iterable**: Loop through characters

### Common String Methods
- `.upper()`, `.lower()` - Case conversion
- `.strip()`, `.lstrip()`, `.rstrip()` - Remove whitespace
- `.split()`, `.join()` - Split and join strings
- `.replace()` - Replace substrings
- `.find()`, `.index()` - Search for substrings
- `.startswith()`, `.endswith()` - Check prefixes/suffixes

### String Formatting
```python
# f-strings (Python 3.6+)
name = "Alice"
age = 25
message = f"Hello, {name}! You are {age} years old."

# format() method
message = "Hello, {}! You are {} years old.".format(name, age)

# % operator (legacy)
message = "Hello, %s! You are %d years old." % (name, age)
```

## Common Patterns

### String Creation
```python
single_quotes = 'Hello'
double_quotes = "World"
triple_quotes = """Multi-line
string"""
raw_string = r"C:\path\to\file"
```

### String Operations
```python
text = "Python Programming"
first_char = text[0]  # 'P'
last_char = text[-1]  # 'g'
substring = text[0:6]  # 'Python'
reversed_text = text[::-1]  # 'gnimmargorP nohtyP'
```

### String Methods
```python
text = "  Hello, World!  "
cleaned = text.strip()  # "Hello, World!"
uppercase = text.upper()  # "  HELLO, WORLD!  "
words = text.split(',')  # ['  Hello', ' World!  ']
```

## Best Practices

1. **Use f-strings**: Modern, readable string formatting
2. **Handle encoding**: Be aware of character encoding issues
3. **Validate input**: Check string properties before processing
4. **Use appropriate methods**: Choose the right method for the task
5. **Consider performance**: String operations can be expensive for large data

## Common Mistakes

1. **Forgetting string immutability**: Strings cannot be modified in place
2. **Confusing find() and index()**: find() returns -1, index() raises exception
3. **Ignoring case sensitivity**: String comparisons are case-sensitive
4. **Not handling encoding**: Unicode issues in international text

## Next Steps

After mastering strings, continue with:
- **Lists** (`../05_Lists/`) - Ordered collections
- **Tuples** (`../06_Tuples/`) - Immutable sequences
- **Dictionaries** (`../07_Dictionaries/`) - Key-value pairs

## Advanced Topics

- **Unicode handling**: International character support
- **Text processing**: Natural language processing basics
- **Regular expressions**: Advanced pattern matching
- **String performance**: Optimizing string operations

## Resources

- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [String Formatting](https://docs.python.org/3/library/string.html#format-string-syntax)
- [Regular Expressions](https://docs.python.org/3/library/re.html)
- [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)

Happy text processing! 📝 