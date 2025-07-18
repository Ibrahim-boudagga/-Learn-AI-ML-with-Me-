# Conditionals in Python

This folder covers Python conditional statements - decision-making tools that control program flow based on conditions.

## Course Structure

### 1. Basic If Statements (`01_basic_if_statements.py`)
- **Topics Covered**: if statements, indentation, simple conditions
- **Learning Objectives**: 
  - Write basic if statements
  - Understand Python indentation
  - Control program flow
- **Run Command**: `python 01_basic_if_statements.py`

### 2. Comparison Operators (`02_comparison_operators.py`)
- **Topics Covered**: ==, !=, <, >, <=, >=, chained comparisons
- **Learning Objectives**:
  - Use comparison operators
  - Chain comparisons effectively
  - Understand operator precedence
- **Run Command**: `python 02_comparison_operators.py`

### 3. Identity and Membership (`03_identity_membership.py`)
- **Topics Covered**: is, is not, in, not in operators
- **Learning Objectives**:
  - Check object identity
  - Test membership in collections
  - Understand identity vs equality
- **Run Command**: `python 03_identity_membership.py`

### 4. Logical Operators (`04_logical_operators.py`)
- **Topics Covered**: and, or, not, short-circuit evaluation
- **Learning Objectives**:
  - Combine conditions logically
  - Use short-circuit evaluation
  - Write complex conditions
- **Run Command**: `python 04_logical_operators.py`

### 5. Nested Conditionals (`05_nested_conditionals.py`)
- **Topics Covered**: Nested if statements, elif chains, complex logic
- **Learning Objectives**:
  - Write nested conditional logic
  - Use elif effectively
  - Structure complex decisions
- **Run Command**: `python 05_nested_conditionals.py`

### 6. Ternary Operator (`06_ternary_operator.py`)
- **Topics Covered**: Conditional expressions, inline conditionals
- **Learning Objectives**:
  - Use ternary operator
  - Write concise conditional code
  - Choose appropriate syntax
- **Run Command**: `python 06_ternary_operator.py`

### 7. Truthy and Falsy (`07_truthy_falsy.py`)
- **Topics Covered**: Truth values, boolean evaluation, implicit conversion
- **Learning Objectives**:
  - Understand truthy/falsy values
  - Use implicit boolean conversion
  - Write cleaner conditions
- **Run Command**: `python 07_truthy_falsy.py`

### 8. Common Patterns (`08_common_patterns.py`)
- **Topics Covered**: Common conditional patterns, best practices, idioms
- **Learning Objectives**:
  - Use common conditional patterns
  - Write readable conditional code
  - Follow Python idioms
- **Run Command**: `python 08_common_patterns.py`

### 9. Practice Problems (`09_practice_problems.py`)
- **Topics Covered**: Comprehensive exercises covering all conditional concepts
- **Learning Objectives**:
  - Apply conditionals to real problems
  - Practice decision-making logic
  - Build problem-solving skills
- **Run Command**: `python 09_practice_problems.py`

## Key Concepts

### Conditional Structure
```python
if condition:
    # code to execute if condition is True
elif another_condition:
    # code to execute if another_condition is True
else:
    # code to execute if no conditions are True
```

### Comparison Operators
- `==` Equal to
- `!=` Not equal to
- `<` Less than
- `>` Greater than
- `<=` Less than or equal to
- `>=` Greater than or equal to

### Logical Operators
- `and` Both conditions must be True
- `or` At least one condition must be True
- `not` Negates the condition

### Identity vs Equality
- `is` Checks object identity (same object)
- `==` Checks value equality (same value)
- `in` Checks membership in collection
- `not in` Checks absence from collection

## Common Patterns

### Basic If Statement
```python
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

### Multiple Conditions
```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

### Ternary Operator
```python
age = 20
status = "adult" if age >= 18 else "minor"
```

### Membership Testing
```python
fruits = ["apple", "banana", "orange"]
if "apple" in fruits:
    print("Apple is available")
```

## Best Practices

1. **Use clear condition names**: `is_valid` instead of `flag`
2. **Avoid deep nesting**: Use early returns or guard clauses
3. **Use elif for mutually exclusive conditions**: More efficient than multiple ifs
4. **Consider truthy/falsy values**: Leverage implicit boolean conversion
5. **Use parentheses for complex conditions**: Improves readability

## Common Mistakes

1. **Using = instead of ==**: Assignment vs comparison
2. **Forgetting colons**: Required after if, elif, else
3. **Incorrect indentation**: Python is indentation-sensitive
4. **Confusing is and ==**: Identity vs equality
5. **Over-complicating conditions**: Break complex logic into smaller parts

## Truthy and Falsy Values

### Falsy Values:
- `False`
- `None`
- `0` (zero)
- `""` (empty string)
- `[]` (empty list)
- `()` (empty tuple)
- `{}` (empty dict)
- `set()` (empty set)

### Truthy Values:
- Everything else is truthy
- Non-zero numbers
- Non-empty strings, lists, tuples, dicts, sets
- Any object that's not None

## Next Steps

After mastering conditionals, continue with:
- **Loops** (`../10_Loops/`) - Iteration and repetition
- **Functions** (`../11_Functions/`) - Reusable code blocks
- **File Handling** (`../13_File_Handling/`) - Working with files

## Advanced Topics

- **Guard clauses**: Early returns for cleaner code
- **Pattern matching**: Python 3.10+ match statements
- **Conditional expressions**: Advanced ternary usage
- **Boolean logic**: Understanding logical operations

## Resources

- [Python Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Comparison Operations](https://docs.python.org/3/library/stdtypes.html#comparisons)

Happy decision making! 🤔 