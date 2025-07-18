# Python Conditionals

## Overview
Conditionals in Python allow you to execute different code blocks based on whether certain conditions are true or false. They are fundamental to controlling program flow.

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
        return sum(data)
    else:
        return "Unknown type"
```

## Error Handling with Conditionals
```python
def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero"
    elif not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Invalid input types"
    else:
        return a / b

print(divide_numbers(10, 2))    # 5.0
print(divide_numbers(10, 0))    # Error: Division by zero
print(divide_numbers("10", 2))  # Error: Invalid input types
```

## Best Practices

### Use Clear Variable Names
```python
# Good
is_adult = age >= 18
has_income = income > 0
can_apply = is_adult and has_income

if can_apply:
    print("Can apply for loan")

# Bad
if age >= 18 and income > 0:
    print("Can apply for loan")
```

### Avoid Deep Nesting
```python
# Bad - too nested
def check_eligibility(age, income, credit_score):
    if age >= 18:
        if income >= 30000:
            if credit_score >= 700:
                return "Approved"
            else:
                return "Denied - poor credit"
        else:
            return "Denied - low income"
    else:
        return "Denied - too young"

# Good - early returns
def check_eligibility(age, income, credit_score):
    if age < 18:
        return "Denied - too young"
    
    if income < 30000:
        return "Denied - low income"
    
    if credit_score < 700:
        return "Denied - poor credit"
    
    return "Approved"
```

### Use Appropriate Operators
```python
# Use 'is' for identity, '==' for equality
x = None
if x is None:  # Good
    print("x is None")

# Use 'in' for membership
fruits = ["apple", "banana"]
if "apple" in fruits:  # Good
    print("Apple found")

# Use logical operators for complex conditions
age = 25
income = 50000
if age >= 18 and income >= 30000:  # Good
    print("Eligible")
```

## Common Pitfalls

### Assignment vs Comparison
```python
# Common mistake
x = 5
if x = 5:  # SyntaxError: invalid syntax
    print("x is 5")

# Correct
if x == 5:
    print("x is 5")
```

### Floating Point Comparisons
```python
# Avoid direct equality with floats
if 0.1 + 0.2 == 0.3:  # False due to floating point precision
    print("Equal")

# Use tolerance
if abs(0.1 + 0.2 - 0.3) < 1e-10:
    print("Equal")
```

### Short-Circuit Evaluation
```python
# Python uses short-circuit evaluation
def expensive_function():
    print("Expensive operation")
    return True

# This won't call expensive_function() if x is False
x = False
if x and expensive_function():
    print("This won't execute")
```

## Practice Examples
See `practice.py` for hands-on exercises with conditionals! 