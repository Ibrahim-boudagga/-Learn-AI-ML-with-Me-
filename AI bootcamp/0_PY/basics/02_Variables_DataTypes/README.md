# Variables and Data Types

This folder covers Python variables, data types, and type manipulation - fundamental concepts for any Python programmer.

## Course Structure

### 1. Variable Assignment (`01_variable_assignment.py`)
- **Topics Covered**: Basic variable creation, naming conventions, assignment operators
- **Learning Objectives**: 
  - Create and assign variables
  - Follow Python naming conventions
  - Understand assignment operators
- **Run Command**: `python 01_variable_assignment.py`

### 2. Multiple Assignment (`02_multiple_assignment.py`)
- **Topics Covered**: Multiple variable assignment, tuple unpacking, parallel assignment
- **Learning Objectives**:
  - Assign multiple variables at once
  - Use tuple unpacking
  - Swap variable values efficiently
- **Run Command**: `python 02_multiple_assignment.py`

### 3. Data Types (`03_data_types.py`)
- **Topics Covered**: Integer, float, string, boolean, None type
- **Learning Objectives**:
  - Understand all basic data types
  - Know when to use each type
  - Handle type-specific operations
- **Run Command**: `python 03_data_types.py`

### 4. Type Checking (`04_type_checking.py`)
- **Topics Covered**: type() function, isinstance(), type hints
- **Learning Objectives**:
  - Check variable types
  - Use type checking in code
  - Understand type hints
- **Run Command**: `python 04_type_checking.py`

### 5. Type Conversion (`05_type_conversion.py`)
- **Topics Covered**: Converting between types, safe conversion, error handling
- **Learning Objectives**:
  - Convert between data types safely
  - Handle conversion errors
  - Understand when conversion is needed
- **Run Command**: `python 05_type_conversion.py`

### 6. Memory References (`06_memory_references.py`)
- **Topics Covered**: Object identity, memory management, id() function
- **Learning Objectives**:
  - Understand how Python manages memory
  - Check object identity
  - Avoid common memory-related pitfalls
- **Run Command**: `python 06_memory_references.py`

## Key Concepts

### Variables
- Variables are containers for storing data
- Python uses dynamic typing
- Variable names must follow specific rules

### Data Types
1. **Integers (int)**: Whole numbers (1, -5, 1000)
2. **Floats (float)**: Decimal numbers (3.14, -2.5, 1.0)
3. **Strings (str)**: Text data ("hello", 'Python')
4. **Booleans (bool)**: True/False values
5. **None**: Represents absence of value

### Type Conversion
- `int()`: Convert to integer
- `float()`: Convert to float
- `str()`: Convert to string
- `bool()`: Convert to boolean

## How to Use This Course

1. **Start with basics**: Begin with variable assignment
2. **Understand types**: Learn each data type thoroughly
3. **Practice conversion**: Master type conversion techniques
4. **Check types**: Learn to verify data types
5. **Understand memory**: Know how Python handles objects

## Common Patterns

### Variable Assignment
```python
name = "John"
age = 25
height = 1.75
is_student = True
```

### Multiple Assignment
```python
x, y, z = 1, 2, 3
a = b = c = 0
```

### Type Conversion
```python
number = int("123")
text = str(456)
decimal = float("3.14")
```

## Best Practices

1. **Use descriptive names**: `user_age` instead of `a`
2. **Follow naming conventions**: Use snake_case for variables
3. **Check types when needed**: Use `isinstance()` for validation
4. **Handle conversion errors**: Always check for exceptions
5. **Understand memory implications**: Be aware of object identity

## Exercises

Each file contains practical exercises. Try to:
- Modify the examples with different values
- Create your own variables and test them
- Experiment with type conversions
- Practice checking types in different scenarios

## Next Steps

After mastering variables and data types, continue with:
- **Numbers** (`../03_Numbers/`) - Deep dive into numeric operations
- **Strings** (`../04_Strings/`) - Text manipulation
- **Lists** (`../05_Lists/`) - Ordered collections

## Common Mistakes to Avoid

1. **Forgetting quotes for strings**: `name = John` (wrong) vs `name = "John"` (correct)
2. **Confusing = and ==**: Assignment vs comparison
3. **Ignoring type conversion errors**: Always handle exceptions
4. **Using reserved words**: Don't use `class`, `def`, etc. as variable names
5. **Not checking types**: Verify data types when working with user input

## Advanced Topics

- **Type hints**: Modern Python feature for type annotations
- **Memory optimization**: Understanding object reuse
- **Custom types**: Creating your own data types
- **Type checking tools**: Using mypy and similar tools

## Resources

- [Python Variables](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)
- [Python Data Types](https://docs.python.org/3/library/stdtypes.html)
- [Type Hints](https://docs.python.org/3/library/typing.html)

Happy learning! 🐍 