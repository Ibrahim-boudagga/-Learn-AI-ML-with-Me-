# Python Variables and Data Types

## Variables

### What are Variables?
Variables are containers for storing data values. In Python, variables are created when you assign a value to them.

### Variable Assignment
```python
# Basic assignment
name = "Alice"
age = 25
height = 1.75
is_student = True

# Multiple assignment
x, y, z = 1, 2, 3

# Chained assignment
a = b = c = 10

# Augmented assignment
count = 5
count += 1  # count = count + 1
count -= 1  # count = count - 1
count *= 2  # count = count * 2
count /= 2  # count = count / 2
```

### Variable Naming Rules
```python
# Valid variable names
user_name = "Alice"
userName = "Bob"
user_name_2 = "Charlie"
_private_var = "Private"
CONSTANT = "Constant"

# Invalid variable names (will cause errors)
# 2user = "Invalid"      # Cannot start with number
# user-name = "Invalid"   # Cannot contain hyphens
# user name = "Invalid"   # Cannot contain spaces
# class = "Invalid"       # Cannot use reserved keywords
```

### Variable Scope
```python
# Global variable
global_var = "I'm global"

def my_function():
    # Local variable
    local_var = "I'm local"
    print(local_var)
    print(global_var)  # Can access global variable

# Accessing variables
print(global_var)  # Works
# print(local_var)  # Error - local_var is not accessible here
```

## Data Types

### Numeric Types

#### Integers (int)
```python
# Positive integers
age = 25
year = 2024

# Negative integers
temperature = -5
debt = -1000

# Zero
zero = 0

# Large integers (Python handles them automatically)
large_number = 123456789012345678901234567890
```

#### Floating Point (float)
```python
# Decimal numbers
pi = 3.14159
temperature = 98.6
price = 19.99

# Scientific notation
large_float = 1.23e5    # 123000.0
small_float = 1.23e-5   # 0.0000123

# Converting to float
float_from_int = float(42)  # 42.0
float_from_string = float("3.14")  # 3.14
```

#### Complex Numbers (complex)
```python
# Complex numbers
complex_num = 3 + 4j
real_part = complex_num.real    # 3.0
imaginary_part = complex_num.imag  # 4.0

# Creating complex numbers
z1 = complex(3, 4)  # 3 + 4j
z2 = complex(5)     # 5 + 0j
```

### String Type (str)
```python
# String creation
name = "Alice"
message = 'Hello, World!'
multi_line = """
This is a multi-line
string in Python
"""

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenation
greeting = f"Hello, {full_name}!"         # f-string formatting

# String methods
text = "  Hello World  "
print(text.upper())      # "  HELLO WORLD  "
print(text.lower())      # "  hello world  "
print(text.strip())      # "Hello World"
print(text.replace("World", "Python"))
```

### Boolean Type (bool)
```python
# Boolean values
is_active = True
is_finished = False

# Boolean expressions
age = 18
is_adult = age >= 18  # True
is_teenager = 13 <= age < 20  # True

# Truthy and Falsy values
print(bool(1))      # True
print(bool(0))      # False
print(bool(""))     # False
print(bool("hello")) # True
print(bool([]))     # False
print(bool([1, 2])) # True
```

### Sequence Types

#### Lists (list)
```python
# List creation
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "hello", 3.14, True]

# List operations
numbers.append(6)        # Add element
numbers.insert(0, 0)     # Insert at index
removed = numbers.pop()   # Remove and return last element
numbers.remove(3)        # Remove first occurrence of 3
```

#### Tuples (tuple)
```python
# Tuple creation
coordinates = (10, 20)
person = ("Alice", 25, "Engineer")

# Tuples are immutable
# coordinates[0] = 100  # This would raise an error

# Tuple unpacking
x, y = coordinates
name, age, job = person
```

#### Range (range)
```python
# Range objects
range_5 = range(5)           # 0, 1, 2, 3, 4
range_1_6 = range(1, 6)      # 1, 2, 3, 4, 5
range_step = range(0, 10, 2) # 0, 2, 4, 6, 8

# Converting to list
numbers = list(range(5))  # [0, 1, 2, 3, 4]
```

### Mapping Type

#### Dictionaries (dict)
```python
# Dictionary creation
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Dictionary operations
person["job"] = "Engineer"    # Add key-value pair
age = person["age"]           # Access value
name = person.get("name")     # Safe access
person.pop("city")            # Remove key-value pair
```

### Set Types

#### Sets (set)
```python
# Set creation
fruits = {"apple", "banana", "orange"}
numbers = set([1, 2, 3, 4, 5])

# Set operations
fruits.add("grape")           # Add element
fruits.remove("banana")       # Remove element
fruits.discard("kiwi")        # Remove if exists (no error)
```

#### Frozen Sets (frozenset)
```python
# Frozen set (immutable)
frozen_fruits = frozenset(["apple", "banana", "orange"])
# frozen_fruits.add("grape")  # This would raise an error
```

## Type Checking and Conversion

### Checking Data Types
```python
# Using type() function
name = "Alice"
age = 25
height = 1.75

print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(height))  # <class 'float'>

# Using isinstance()
print(isinstance(name, str))    # True
print(isinstance(age, int))     # True
print(isinstance(height, float)) # True
```

### Type Conversion
```python
# Converting between types
number_string = "42"
number_float = "3.14"

# String to number
number_int = int(number_string)      # 42
number_float = float(number_float)   # 3.14

# Number to string
string_from_int = str(42)           # "42"
string_from_float = str(3.14)       # "3.14"

# List conversions
string_to_list = list("Python")     # ['P', 'y', 't', 'h', 'o', 'n']
tuple_to_list = list((1, 2, 3))     # [1, 2, 3]
set_to_list = list({1, 2, 3})       # [1, 2, 3] (order may vary)

# Dictionary conversions
items = [("name", "Alice"), ("age", 25)]
dict_from_items = dict(items)        # {'name': 'Alice', 'age': 25}
```

## Memory and References

### Object Identity
```python
# Checking object identity
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)  # False (different objects)
print(a is c)  # True (same object)
print(a == b)  # True (same values)

# id() function
print(id(a))   # Memory address of object a
print(id(b))   # Different memory address
print(id(c))   # Same as id(a)
```

### Mutable vs Immutable Types
```python
# Immutable types (cannot be changed after creation)
# int, float, str, tuple, frozenset

# Mutable types (can be changed after creation)
# list, dict, set

# Example with immutable type
name = "Alice"
# name[0] = "B"  # This would raise an error

# Example with mutable type
numbers = [1, 2, 3]
numbers[0] = 10  # This works
```

## Best Practices

### Variable Naming
```python
# Use descriptive names
user_name = "Alice"          # Good
un = "Alice"                 # Bad

# Use snake_case for variables
first_name = "John"          # Good
firstName = "John"           # Bad (camelCase)

# Use UPPERCASE for constants
PI = 3.14159                 # Good
MAX_RETRY_COUNT = 3          # Good

# Avoid reserved keywords
# class = "Invalid"          # Don't use reserved words
# def = "Invalid"            # Don't use reserved words
```

### Type Hints (Python 3.5+)
```python
# Type hints for better code documentation
def greet(name: str) -> str:
    return f"Hello, {name}!"

def calculate_area(length: float, width: float) -> float:
    return length * width

# Variable type hints
age: int = 25
name: str = "Alice"
scores: list[int] = [85, 90, 78]
```

### Common Pitfalls
```python
# 1. Mutable default arguments
def bad_function(items=[]):  # Don't do this
    items.append(1)
    return items

def good_function(items=None):  # Do this instead
    if items is None:
        items = []
    items.append(1)
    return items

# 2. Comparing with None
x = None
# if x == None:  # Don't do this
if x is None:    # Do this instead
    print("x is None")

# 3. String concatenation in loops
# Bad
result = ""
for i in range(1000):
    result += str(i)

# Good
result = "".join(str(i) for i in range(1000))
```

## Practice Examples
See `practice.py` for hands-on exercises with variables and data types! 