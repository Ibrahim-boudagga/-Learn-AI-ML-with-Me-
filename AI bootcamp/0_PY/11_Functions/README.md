# Python Functions

## Overview
Functions in Python are reusable blocks of code that perform specific tasks. They help organize code, reduce duplication, and make programs more modular.

## Course Structure

This course is organized into focused modules for better learning:

### Core Concepts
- **01_basic_function_definition.py** - Basic function syntax and definition
- **02_function_parameters.py** - Understanding different parameter types
- **03_return_values.py** - Function return values and types
- **04_arbitrary_arguments.py** - Using *args and **kwargs
- **05_variable_scope.py** - Understanding variable scope and LEGB rule
- **06_lambda_functions.py** - Anonymous functions and lambda expressions
- **07_recursion.py** - Recursive function patterns and algorithms
- **08_higher_order_functions.py** - Functions as parameters and return values
- **09_builtin_functions_with_functions.py** - map(), filter(), reduce(), etc.

### Practice Problems
- **10_practice_problems_1.py** - Basic to intermediate function problems (Problems 1-5)
- **11_practice_problems_2.py** - Advanced function problems (Problems 6-10)

## How to Use This Course

### For Beginners
1. Start with `01_basic_function_definition.py` to understand function syntax
2. Progress through each file in numerical order
3. Run each file to see the output and understand the concepts
4. Practice with the problems in the practice files

### For Intermediate Learners
1. Review concepts you're less familiar with
2. Focus on the practice problems to strengthen your skills
3. Experiment with modifying the examples

### Running the Examples
```bash
# Run a specific concept file
python 01_basic_function_definition.py

# Run practice problems
python 10_practice_problems_1.py
python 11_practice_problems_2.py
```

## Key Concepts Covered

### Basic Function Definition
```python
# Simple function with no parameters
def greet():
    print("Hello, World!")

# Function with parameters
def greet_with_name(name):
    print(f"Hello, {name}!")

# Function with parameters and return value
def add_numbers(a, b):
    return a + b
```

### Function Parameters
```python
# Function with default parameters
def describe_person(name, age, city="Unknown"):
    print(f"{name} is {age} years old from {city}")

# Function with keyword-only parameters
def calculate_rectangle_area(*, length, width):
    return length * width

# Function with positional-only parameters
def calculate_circle_area(radius, /):
    import math
    return math.pi * radius**2
```

### Return Values
```python
# Function returning single value
def square(x):
    return x**2

# Function returning multiple values
def get_min_max(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)

# Function returning different types
def check_age(age):
    if age < 0:
        return "Invalid age"
    elif age < 18:
        return "Minor"
    else:
        return "Adult"
```

### Arbitrary Arguments
```python
# Function with *args
def sum_all(*args):
    return sum(args)

# Function with **kwargs
def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Function with both *args and **kwargs
def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
```

### Variable Scope
```python
# Global variable
global_var = "I'm global"

def test_scope():
    local_var = "I'm local"
    print(f"Local: {local_var}")
    print(f"Global: {global_var}")

def modify_global():
    global global_var
    global_var = "Modified global"
```

### Lambda Functions
```python
# Basic lambda
square_lambda = lambda x: x**2
add_lambda = lambda x, y: x + y

# Lambda with conditional logic
is_even = lambda x: x % 2 == 0
get_sign = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"

# Lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

### Recursion
```python
# Basic factorial function
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Binary search recursively
def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)
```

### Higher-Order Functions
```python
# Function that takes another function as parameter
def apply_operation(func, numbers):
    return [func(num) for num in numbers]

# Function that returns a function
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

# Function composition
def compose(*functions):
    def composed(x):
        result = x
        for func in reversed(functions):
            result = func(result)
        return result
    return composed
```

### Built-in Functions with Functions
```python
# map() function
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))

# filter() function
evens = list(filter(lambda x: x % 2 == 0, numbers))

# reduce() function
from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)

# sorted() with key function
words = ["banana", "apple", "cherry"]
sorted_by_length = sorted(words, key=lambda x: len(x))
```

## Practice Problems Included

### Part 1 (Basic to Intermediate)
1. Calculate area of different shapes
2. Check if number is prime
3. Find GCD using Euclidean algorithm
4. Convert decimal to binary
5. Check if string is palindrome

### Part 2 (Advanced)
6. Generate all permutations
7. Calculate compound interest
8. Find longest common subsequence
9. Validate credit card number (Luhn algorithm)
10. Create a simple calculator function

## Best Practices

### Use Descriptive Names
```python
# Good
def calculate_monthly_payment(principal, rate, years):
    pass

# Bad
def calc(pr, rt, yr):
    pass
```

### Keep Functions Small
```python
# Good - single responsibility
def validate_email(email):
    return "@" in email and "." in email

def send_email(email, message):
    if validate_email(email):
        # Send email logic
        pass

# Bad - multiple responsibilities
def process_user_data(user_data):
    # Too many responsibilities in one function
    pass
```

### Use Default Parameters Wisely
```python
# Good
def create_user(name, email, age=None, city="Unknown"):
    pass

# Bad - mutable default arguments
def add_item(item, items=[]):  # Don't do this!
    items.append(item)
    return items
```

### Return Early
```python
# Good
def check_eligibility(age, income):
    if age < 18:
        return False
    if income < 30000:
        return False
    return True

# Bad - deep nesting
def check_eligibility(age, income):
    if age >= 18:
        if income >= 30000:
            return True
        else:
            return False
    else:
        return False
```

### Use Type Hints
```python
def calculate_area(length: float, width: float) -> float:
    return length * width

def process_data(data: list) -> dict:
    return {"count": len(data), "sum": sum(data)}
```

### Document Your Functions
```python
def calculate_interest(principal: float, rate: float, time: float) -> float:
    """
    Calculate simple interest.
    
    Args:
        principal (float): The principal amount
        rate (float): The interest rate (as decimal)
        time (float): The time period in years
    
    Returns:
        float: The calculated interest
    """
    return principal * rate * time
```

### Handle Errors Gracefully
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid input types"
```

## Common Function Patterns

### Function with Error Handling
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid input types"

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # Error: Division by zero
print(safe_divide("10", 2)) # Error: Invalid input types
```

### Function with Type Hints
```python
def calculate_area(length: float, width: float) -> float:
    return length * width

def process_data(data: list) -> dict:
    return {"count": len(data), "sum": sum(data)}
```

### Function with Documentation
```python
def calculate_interest(principal: float, rate: float, time: float) -> float:
    """
    Calculate simple interest.
    
    Args:
        principal (float): The principal amount
        rate (float): The interest rate (as decimal)
        time (float): The time period in years
    
    Returns:
        float: The calculated interest
    """
    return principal * rate * time
```

## Next Steps
After completing this module, you should be comfortable with:
- Basic and advanced function concepts
- Parameter types and return values
- Lambda functions and functional programming
- Recursion and higher-order functions
- Built-in functions that work with functions
- Best practices for function design

Move on to the next module to continue your Python learning journey! 