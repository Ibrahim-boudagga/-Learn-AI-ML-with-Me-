# Python Numbers

## Overview
Python has three numeric types:
- **int** - Integer numbers (whole numbers)
- **float** - Floating point numbers (decimal numbers)
- **complex** - Complex numbers (real + imaginary part)

## Integer (int)
```python
# Positive integers
age = 25
year = 2024

# Negative integers
temperature = -5
debt = -1000

# Zero
zero = 0
```

## Float (float)
```python
# Decimal numbers
pi = 3.14159
temperature = 98.6
price = 19.99

# Scientific notation
large_number = 1.23e5  # 123000
small_number = 1.23e-5  # 0.0000123
```

## Mathematical Operations

### Basic Operations
```python
# Addition
result = 10 + 5  # 15

# Subtraction
result = 10 - 5  # 5

# Multiplication
result = 10 * 5  # 50

# Division (always returns float)
result = 10 / 5  # 2.0

# Floor Division (returns integer)
result = 10 // 3  # 3

# Modulo (remainder)
result = 10 % 3  # 1

# Exponentiation
result = 2 ** 3  # 8
```

### Assignment Operators
```python
x = 10
x += 5   # x = x + 5
x -= 3   # x = x - 3
x *= 2   # x = x * 2
x /= 4   # x = x / 4
x //= 2  # x = x // 2
x %= 3   # x = x % 3
x **= 2  # x = x ** 2
```

## Type Conversion
```python
# Converting between types
int_number = 42
float_number = 3.14

# Convert float to int
int_from_float = int(3.14)  # 3

# Convert int to float
float_from_int = float(42)  # 42.0

# Convert string to number
number_from_string = int("123")  # 123
float_from_string = float("3.14")  # 3.14
```

## Built-in Functions
```python
# abs() - Absolute value
abs(-5)  # 5

# round() - Round to nearest integer
round(3.6)  # 4
round(3.4)  # 3

# min() and max()
min(1, 2, 3, 4, 5)  # 1
max(1, 2, 3, 4, 5)  # 5

# sum() - Sum of numbers
sum([1, 2, 3, 4, 5])  # 15
```

## Math Module
```python
import math

# Constants
math.pi      # 3.141592653589793
math.e       # 2.718281828459045

# Functions
math.sqrt(16)    # 4.0
math.pow(2, 3)   # 8.0
math.ceil(3.2)   # 4
math.floor(3.8)  # 3
math.factorial(5) # 120
```

## Common Pitfalls
```python
# Integer division vs float division
result1 = 10 / 3   # 3.3333333333333335
result2 = 10 // 3  # 3

# Floating point precision
0.1 + 0.2  # 0.30000000000000004 (not exactly 0.3)

# Use round() for precise calculations
round(0.1 + 0.2, 1)  # 0.3
```

## Practice Examples
See `practice.py` for hands-on exercises with numbers! 