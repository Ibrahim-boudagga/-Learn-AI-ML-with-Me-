# Python Conditionals

## Overview
Conditionals in Python allow you to execute different code blocks based on whether certain conditions are true or false. They are fundamental to controlling program flow.

## Course Structure

This course is organized into focused modules for better learning:

### 1. Basic Operations
- **`01_basic_if_statements.py`** - Basic if, if-else, and if-elif-else statements
- **`02_comparison_operators.py`** - Comparison operators and their usage
- **`03_identity_membership.py`** - Identity and membership operators

### 2. Advanced Operations
- **`04_logical_operators.py`** - Logical operators (AND, OR, NOT) and combinations
- **`05_nested_conditionals.py`** - Nested conditional statements
- **`06_ternary_operator.py`** - Ternary operator for concise conditionals

### 3. Special Features
- **`07_truthy_falsy_values.py`** - Truthy and falsy values in Python
- **`08_common_conditional_patterns.py`** - Common patterns and best practices

### 4. Practice Problems
- **`09_practice_problems_1.py`** - Basic practice problems with conditionals
- **`10_practice_problems_2.py`** - Advanced problems including validation and classification

## How to Use This Course

### Running Individual Files
Each file can be run independently to focus on specific concepts:

```bash
# Run basic if statements
python 01_basic_if_statements.py

# Run comparison operators
python 02_comparison_operators.py

# Run logical operators
python 04_logical_operators.py

# And so on for each file...
```

### Learning Path
1. Start with `01_basic_if_statements.py` to understand conditional basics
2. Move to `02_comparison_operators.py` and `03_identity_membership.py` for operators
3. Study `04_logical_operators.py` for logical combinations
4. Learn about `05_nested_conditionals.py` for complex structures
5. Explore `06_ternary_operator.py` for concise syntax
6. Understand `07_truthy_falsy_values.py` for boolean evaluation
8. Practice with `08_common_conditional_patterns.py` for patterns
9. Practice with `09_practice_problems_1.py` and `10_practice_problems_2.py`

## If Statements

### Basic If Statement
```python
age = 18

if age >= 18:
    print("You are an adult")
```

### If-Else Statement
```python
age = 16

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

### If-Elif-Else Statement
```python
age = 15

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")
```

## Comparison Operators

### Numeric Comparisons
```python
x = 10
y = 5

print(x > y)   # True
print(x < y)   # False
print(x >= y)  # True
print(x <= y)  # False
print(x == y)  # False
print(x != y)  # True
```

### String Comparisons
```python
name1 = "Alice"
name2 = "Bob"

print(name1 < name2)   # True (alphabetical)
print(name1 == name2)  # False
print(name1 != name2)  # True
```

### Identity and Membership
```python
# Identity operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)      # False (different objects)
print(x is z)      # True (same object)
print(x == y)      # True (same values)

# Membership operators
fruits = ["apple", "banana", "orange"]
print("apple" in fruits)      # True
print("grape" not in fruits)  # True
```

## Logical Operators

### AND Operator
```python
age = 25
income = 50000

if age >= 18 and income >= 30000:
    print("Eligible for loan")
```

### OR Operator
```python
age = 16
parent_consent = True

if age >= 18 or parent_consent:
    print("Can participate")
```

### NOT Operator
```python
is_student = False

if not is_student:
    print("Must pay full price")
```

### Combining Logical Operators
```python
age = 25
income = 50000
credit_score = 750

if age >= 18 and income >= 30000 and credit_score >= 700:
    print("Approved for loan")
elif age >= 18 and (income >= 50000 or credit_score >= 800):
    print("Approved with conditions")
else:
    print("Not approved")
```

## Nested Conditionals
```python
age = 25
income = 50000
credit_score = 750

if age >= 18:
    if income >= 30000:
        if credit_score >= 700:
            print("Fully approved")
        else:
            print("Approved with higher interest")
    else:
        print("Income too low")
else:
    print("Too young")
```

## Ternary Operator
```python
age = 20

# Traditional if-else
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary operator
status = "adult" if age >= 18 else "minor"

# Multiple conditions
grade = 85
letter_grade = "A" if grade >= 90 else "B" if grade >= 80 else "C" if grade >= 70 else "F"
```

## Truthy and Falsy Values
```python
# Falsy values
falsy_values = [False, None, 0, "", [], {}, ()]

for value in falsy_values:
    if value:
        print(f"{value} is truthy")
    else:
        print(f"{value} is falsy")

# Truthy values
truthy_values = [True, 1, "hello", [1, 2], {"a": 1}]

for value in truthy_values:
    if value:
        print(f"{value} is truthy")
    else:
        print(f"{value} is falsy")
```

## Common Conditional Patterns

### Range Checking
```python
score = 85

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
else:
    grade = "F"
```

### Multiple Conditions
```python
username = "admin"
password = "secret123"
is_active = True

if username == "admin" and password == "secret123" and is_active:
    print("Login successful")
else:
    print("Login failed")
```

### Type Checking
```python
def process_data(data):
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, (int, float)):
        return data * 2
    elif isinstance(data, list):
        return len(data)
    else:
        return "Unknown type"
```

### Guard Clauses
```python
def process_user(user):
    if not user:
        return "No user provided"
    
    if not user.get('name'):
        return "User has no name"
    
    if user.get('age', 0) < 18:
        return "User is too young"
    
    return f"Processing user: {user['name']}"
```

## Best Practices

### 1. Use Clear Condition Names
```python
# Good
is_adult = age >= 18
has_income = income >= 30000
is_eligible = is_adult and has_income

if is_eligible:
    print("Approved")

# Avoid
if age >= 18 and income >= 30000:
    print("Approved")
```

### 2. Avoid Deep Nesting
```python
# Instead of deep nesting, use early returns
def process_order(order):
    if not order:
        return "No order"
    
    if not order.items:
        return "Empty order"
    
    if order.total < 0:
        return "Invalid total"
    
    return "Order processed"
```

### 3. Use Appropriate Operators
```python
# Use 'in' for membership
if item in collection:
    print("Found")

# Use 'is' for identity
if value is None:
    print("No value")

# Use '==' for equality
if name == "admin":
    print("Admin user")
```

### 4. Consider Readability
```python
# Complex condition - hard to read
if (age >= 18 and income >= 30000) or (age >= 21 and income >= 50000) or credit_score >= 800:
    print("Approved")

# Better - break into parts
is_standard_eligible = age >= 18 and income >= 30000
is_premium_eligible = age >= 21 and income >= 50000
has_excellent_credit = credit_score >= 800

if is_standard_eligible or is_premium_eligible or has_excellent_credit:
    print("Approved")
```

## Performance Considerations
```python
# Short-circuit evaluation
def expensive_check():
    print("This is expensive!")
    return True

# With short-circuit
result = False and expensive_check()  # expensive_check() not called
result = True or expensive_check()    # expensive_check() not called

# Order conditions for efficiency
# Put most likely to be False first for AND
# Put most likely to be True first for OR
if rare_condition and common_condition:
    pass

if common_condition or rare_condition:
    pass
```

## Practice Examples
Each file contains hands-on exercises with conditionals! Start with the basic files and work your way up to the practice problems. 