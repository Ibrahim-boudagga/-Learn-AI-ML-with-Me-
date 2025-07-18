# Python Introduction

## What is Python?
Python is a high-level, interpreted programming language known for its simplicity and readability. It was created by Guido van Rossum and released in 1991.

## Why Python?
- **Easy to learn**: Simple syntax, readable code
- **Versatile**: Web development, data science, AI, automation, and more
- **Large community**: Extensive libraries and frameworks
- **Cross-platform**: Runs on Windows, macOS, Linux
- **Great for beginners**: Excellent first programming language

## Installing Python

### Windows
1. Visit [python.org](https://www.python.org/downloads/)
2. Download the latest version
3. Run the installer
4. Check "Add Python to PATH" during installation
5. Verify installation: Open Command Prompt and type `python --version`

### macOS
```bash
# Using Homebrew
brew install python

# Or download from python.org
```

### Linux
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3

# CentOS/RHEL
sudo yum install python3
```

## Your First Python Program

### Hello World
```python
print("Hello, World!")
```

### Running Python Code
1. **Interactive Mode**: Type `python` in terminal
2. **Script Mode**: Save code in `.py` file and run with `python filename.py`
3. **IDE**: Use VS Code, PyCharm, or other IDEs

## Basic Syntax

### Comments
```python
# This is a single-line comment

"""
This is a multi-line comment
or docstring
"""

'''
This is also a multi-line comment
'''
```

### Variables
```python
# Variable assignment
name = "Alice"
age = 25
height = 1.75
is_student = True

# Multiple assignment
x, y, z = 1, 2, 3

# Print variables
print(f"Name: {name}, Age: {age}")
```

### Data Types
```python
# Numbers
integer = 42
float_num = 3.14

# Strings
text = "Hello, Python!"

# Booleans
true_value = True
false_value = False

# Check type
print(type(integer))  # <class 'int'>
print(type(text))     # <class 'str'>
```

## Basic Operations

### Mathematical Operations
```python
a = 10
b = 3

addition = a + b        # 13
subtraction = a - b     # 7
multiplication = a * b  # 30
division = a / b        # 3.333...
floor_division = a // b # 3
modulo = a % b          # 1
exponent = a ** b       # 1000
```

### String Operations
```python
first_name = "John"
last_name = "Doe"

# Concatenation
full_name = first_name + " " + last_name

# String formatting
greeting = f"Hello, {full_name}!"

# String methods
upper_name = full_name.upper()
lower_name = full_name.lower()
```

## Input and Output

### Getting User Input
```python
# Get string input
name = input("Enter your name: ")

# Get numeric input
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
```

### Output Formatting
```python
name = "Alice"
age = 25

# f-strings (recommended)
print(f"Name: {name}, Age: {age}")

# .format() method
print("Name: {}, Age: {}".format(name, age))

# % operator (old style)
print("Name: %s, Age: %d" % (name, age))
```

## Control Flow Basics

### If Statements
```python
age = 18

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")
```

### Loops
```python
# For loop
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
```

## Functions

### Defining Functions
```python
def greet(name):
    return f"Hello, {name}!"

# Calling function
message = greet("Alice")
print(message)
```

### Function with Parameters
```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # 8
```

## Common Built-in Functions

```python
# Type conversion
str(42)      # "42"
int("42")    # 42
float("3.14") # 3.14

# Length
len("Python") # 6

# Range
range(5)     # 0, 1, 2, 3, 4
range(1, 6)  # 1, 2, 3, 4, 5

# Print
print("Hello", "World", sep="-")  # Hello-World
```

## Best Practices

### Code Style
```python
# Use descriptive variable names
user_name = "Alice"  # Good
n = "Alice"          # Bad

# Use proper indentation (4 spaces)
if condition:
    print("This is indented")

# Keep lines under 79 characters
long_string = ("This is a very long string "
               "that spans multiple lines")
```

### Error Handling
```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

## Next Steps
1. Learn about data structures (lists, tuples, dictionaries)
2. Explore object-oriented programming
3. Study file handling and modules
4. Practice with projects and exercises

## Resources
- [Python Official Documentation](https://docs.python.org/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)
- [Python.org](https://www.python.org/)

## Course Structure

This introduction section is organized into individual practice files for focused learning:

### **Practice Files:**

1. **`01_first_program.py`** - Your first Python program
   - Basic print statements
   - Understanding program structure

2. **`02_variables_data_types.py`** - Variables and data types
   - String, integer, float, boolean types
   - Variable assignment and type checking

3. **`03_mathematical_operations.py`** - Mathematical operations
   - Addition, subtraction, multiplication, division
   - Floor division, modulo, exponentiation

4. **`04_string_operations.py`** - String operations
   - String concatenation and formatting
   - String methods (upper, lower, title)
   - String length and manipulation

5. **`05_type_conversion.py`** - Type conversion
   - Converting between data types
   - int(), float(), str() functions

6. **`06_input_output.py`** - Input and output
   - Getting user input with input()
   - Output formatting with print()

7. **`07_control_flow.py`** - Control flow
   - If, elif, else statements
   - Conditional logic and decision making

8. **`08_loops.py`** - Loops
   - For loops with range() and lists
   - While loops and iteration

9. **`09_functions.py`** - Functions
   - Function definition and calling
   - Parameters and return values

10. **`10_built_in_functions.py`** - Built-in functions
    - len(), sum(), max(), min()
    - String methods and utilities

11. **`11_practice_problems.py`** - Practice problems
    - 10 practical exercises
    - Real-world problem solving

### **How to Use This Course:**

1. **Start with the README** - Read through the theory and concepts
2. **Run each file individually** - Execute `python filename.py` to see examples
3. **Experiment with code** - Modify variables and try different values
4. **Complete practice problems** - Work through the exercises in `11_practice_problems.py`
5. **Move to next section** - Progress to Variables and Data Types section

### **Running the Examples:**

```bash
# Run individual files
python 01_first_program.py
python 02_variables_data_types.py
python 03_mathematical_operations.py
# ... and so on

# Or run all files in sequence
for file in *.py; do
    echo "=== Running $file ==="
    python "$file"
    echo
done
```

## Practice Examples
Each file contains hands-on exercises and examples. Start with `01_first_program.py` and work your way through! 