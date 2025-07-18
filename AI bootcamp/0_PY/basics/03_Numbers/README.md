# Numbers in Python

This folder covers Python's numeric data types and operations - essential for mathematical computations and data analysis.

## Course Structure

### 1. Number Types (`01_number_types.py`)
- **Topics Covered**: Integers, floats, complex numbers, numeric literals
- **Learning Objectives**: 
  - Understand different number types
  - Know when to use each type
  - Handle numeric literals
- **Run Command**: `python 01_number_types.py`

### 2. Arithmetic Operations (`02_arithmetic_operations.py`)
- **Topics Covered**: Addition, subtraction, multiplication, division, modulo, exponentiation
- **Learning Objectives**:
  - Perform basic arithmetic operations
  - Understand operator precedence
  - Handle division types (/, //, %)
- **Run Command**: `python 02_arithmetic_operations.py`

### 3. Comparison Operators (`03_comparison_operators.py`)
- **Topics Covered**: ==, !=, <, >, <=, >=, chained comparisons
- **Learning Objectives**:
  - Compare numbers effectively
  - Use chained comparisons
  - Understand boolean results
- **Run Command**: `python 03_comparison_operators.py`

### 4. Math Functions (`04_math_functions.py`)
- **Topics Covered**: Built-in math functions, math module, common operations
- **Learning Objectives**:
  - Use Python's math functions
  - Import and use the math module
  - Apply mathematical concepts
- **Run Command**: `python 04_math_functions.py`

### 5. Number Methods (`05_number_methods.py`)
- **Topics Covered**: Number object methods, bitwise operations, number properties
- **Learning Objectives**:
  - Use number-specific methods
  - Perform bitwise operations
  - Understand number properties
- **Run Command**: `python 05_number_methods.py`

### 6. Random Numbers (`06_random_numbers.py`)
- **Topics Covered**: random module, generating random numbers, probability
- **Learning Objectives**:
  - Generate random numbers
  - Use different random distributions
  - Apply random numbers in programs
- **Run Command**: `python 06_random_numbers.py`

### 7. Decimal and Fraction (`07_decimal_fraction.py`)
- **Topics Covered**: Decimal for precision, Fraction for exact fractions
- **Learning Objectives**:
  - Handle decimal precision issues
  - Work with exact fractions
  - Choose appropriate numeric types
- **Run Command**: `python 07_decimal_fraction.py`

### 8. Number Formatting (`08_number_formatting.py`)
- **Topics Covered**: String formatting, f-strings, format() method
- **Learning Objectives**:
  - Format numbers for display
  - Control decimal places
  - Use different number formats
- **Run Command**: `python 08_number_formatting.py`

### 9. Built-in Functions (`09_built_in_functions.py`)
- **Topics Covered**: abs(), round(), min(), max(), sum(), pow()
- **Learning Objectives**:
  - Use built-in numeric functions
  - Apply functions to number sequences
  - Understand function behavior
- **Run Command**: `python 09_built_in_functions.py`

### 10. Practice Problems (`10_practice_problems.py`)
- **Topics Covered**: Comprehensive exercises covering all numeric concepts
- **Learning Objectives**:
  - Apply numeric operations to real problems
  - Practice mathematical programming
  - Build problem-solving skills
- **Run Command**: `python 10_practice_problems.py`

## Key Concepts

### Number Types
1. **Integers (int)**: Whole numbers, unlimited precision
2. **Floats (float)**: Decimal numbers, finite precision
3. **Complex (complex)**: Numbers with real and imaginary parts

### Arithmetic Operators
- `+` Addition
- `-` Subtraction  
- `*` Multiplication
- `/` Division (returns float)
- `//` Floor division (returns int)
- `%` Modulo (remainder)
- `**` Exponentiation

### Math Module Functions
- `math.sqrt()` - Square root
- `math.pow()` - Power function
- `math.floor()` - Floor function
- `math.ceil()` - Ceiling function
- `math.sin()`, `math.cos()`, `math.tan()` - Trigonometric functions

## Common Patterns

### Basic Arithmetic
```python
a = 10
b = 3
sum_result = a + b
quotient = a / b  # 3.333...
floor_quotient = a // b  # 3
remainder = a % b  # 1
power = a ** b  # 1000
```

### Random Numbers
```python
import random
random_int = random.randint(1, 100)
random_float = random.uniform(0, 1)
random_choice = random.choice([1, 2, 3, 4, 5])
```

### Number Formatting
```python
pi = 3.14159
formatted = f"Pi: {pi:.2f}"  # "Pi: 3.14"
percentage = f"{0.75:.1%}"  # "75.0%"
```

## Best Practices

1. **Use appropriate types**: int for whole numbers, float for decimals
2. **Handle precision**: Use Decimal for financial calculations
3. **Check for division by zero**: Always validate denominators
4. **Use meaningful variable names**: `total_price` instead of `x`
5. **Format output appropriately**: Use proper number formatting

## Common Mistakes

1. **Floating point precision**: `0.1 + 0.2 != 0.3`
2. **Integer division**: `5 / 2` vs `5 // 2`
3. **Forgetting parentheses**: Operator precedence matters
4. **Ignoring type conversion**: Ensure proper types for operations

## Next Steps

After mastering numbers, continue with:
- **Strings** (`../04_Strings/`) - Text manipulation
- **Lists** (`../05_Lists/`) - Ordered collections
- **Functions** (`../11_Functions/`) - Reusable code blocks

## Advanced Topics

- **NumPy**: Advanced numerical computing
- **Scientific computing**: SciPy, pandas
- **Financial calculations**: Decimal precision
- **Performance optimization**: Efficient numeric operations

## Resources

- [Python Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [Math Module](https://docs.python.org/3/library/math.html)
- [Random Module](https://docs.python.org/3/library/random.html)
- [Decimal Module](https://docs.python.org/3/library/decimal.html)

Happy computing! 🔢 