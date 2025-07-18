# Python Functions

## Overview
Functions in Python are reusable blocks of code that perform specific tasks. They help organize code, reduce duplication, and make programs more modular.

## Function Definition

### Basic Function
```python
def greet():
    print("Hello, World!")

# Calling the function
greet()
```

### Function with Parameters
```python
def greet(name):
    print(f"Hello, {name}!")

# Calling with argument
greet("Alice")
```

### Function with Multiple Parameters
```python
def add_numbers(a, b):
    return a + b

# Calling with multiple arguments
result = add_numbers(5, 3)
print(result)  # 8
```

### Function with Default Parameters
```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Using default parameter
greet("Alice")  # Hello, Alice!

# Overriding default parameter
greet("Bob", "Good morning")  # Good morning, Bob!
```

## Return Values

### Basic Return
```python
def square(x):
    return x ** 2

result = square(5)
print(result)  # 25
```

### Multiple Return Values
```python
def get_min_max(numbers):
    if not numbers:
        return None, None
    
    min_val = min(numbers)
    max_val = max(numbers)
    return min_val, max_val

min_num, max_num = get_min_max([1, 2, 3, 4, 5])
print(f"Min: {min_num}, Max: {max_num}")
```

### Early Return
```python
def check_age(age):
    if age < 0:
        return "Invalid age"
    
    if age < 18:
        return "Minor"
    
    if age < 65:
        return "Adult"
    
    return "Senior"

print(check_age(25))  # Adult
print(check_age(-5))  # Invalid age
```

## Parameter Types

### Positional Arguments
```python
def describe_person(name, age, city):
    print(f"{name} is {age} years old from {city}")

describe_person("Alice", 25, "New York")
```

### Keyword Arguments
```python
def describe_person(name, age, city):
    print(f"{name} is {age} years old from {city}")

# Using keyword arguments
describe_person(name="Alice", age=25, city="New York")
describe_person(age=25, name="Alice", city="New York")
```

### Arbitrary Arguments (*args)
```python
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))  # 15
print(sum_numbers(10, 20))         # 30

def print_info(*args):
    for arg in args:
        print(arg)

print_info("Alice", 25, "Engineer", "New York")
```

### Arbitrary Keyword Arguments (**kwargs)
```python
def print_person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_person_info(name="Alice", age=25, job="Engineer", city="New York")
```

### Combining Different Parameter Types
```python
def complex_function(name, age, *args, city="Unknown", **kwargs):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Additional args: {args}")
    print(f"Additional kwargs: {kwargs}")

complex_function("Alice", 25, "Engineer", "Python", city="New York", hobby="reading")
```

## Variable Scope

### Local Variables
```python
def my_function():
    local_var = "I'm local"
    print(local_var)

my_function()
# print(local_var)  # Error - local_var is not accessible outside function
```

### Global Variables
```python
global_var = "I'm global"

def my_function():
    print(global_var)  # Can access global variable

def modify_global():
    global global_var
    global_var = "Modified global"

my_function()
modify_global()
print(global_var)
```

### Nonlocal Variables
```python
def outer_function():
    outer_var = "I'm outer"
    
    def inner_function():
        nonlocal outer_var
        outer_var = "Modified outer"
    
    inner_function()
    print(outer_var)

outer_function()
```

## Lambda Functions

### Basic Lambda
```python
# Regular function
def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

print(square(5))        # 25
print(square_lambda(5)) # 25
```

### Lambda with Multiple Parameters
```python
add = lambda x, y: x + y
multiply = lambda x, y: x * y

print(add(3, 5))      # 8
print(multiply(3, 5)) # 15
```

### Lambda with Conditional Logic
```python
is_even = lambda x: x % 2 == 0
get_sign = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"

print(is_even(4))      # True
print(get_sign(5))     # positive
print(get_sign(-3))    # negative
print(get_sign(0))     # zero
```

## Function Decorators

### Basic Decorator
```python
def timer(func):
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
    return "Done"

slow_function()
```

### Decorator with Parameters
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

## Recursion

### Basic Recursion
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

### Recursion with Base Cases
```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # 55
```

## Higher-Order Functions

### Functions as Parameters
```python
def apply_operation(func, numbers):
    return [func(num) for num in numbers]

def square(x):
    return x ** 2

def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
squared = apply_operation(square, numbers)
doubled = apply_operation(double, numbers)

print(squared)  # [1, 4, 9, 16, 25]
print(doubled)  # [2, 4, 6, 8, 10]
```

### Functions Returning Functions
```python
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

## Built-in Functions with Functions

### map()
```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

### filter()
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]
```

### reduce()
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)  # 15
```

## Common Function Patterns

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

## Practice Examples
See `practice.py` for hands-on exercises with functions! 