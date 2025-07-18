# Python Variables and Data Types Practice

print("=== PYTHON VARIABLES AND DATA TYPES PRACTICE ===\n")

# 1. Variable Assignment
print("1. Variable Assignment:")
name = "Alice"
age = 25
height = 1.75
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is student: {is_student}")
print()

# 2. Multiple Assignment
print("2. Multiple Assignment:")
x, y, z = 1, 2, 3
print(f"x = {x}, y = {y}, z = {z}")

a = b = c = 10
print(f"a = {a}, b = {b}, c = {c}")

# Augmented assignment
count = 5
count += 1
print(f"After count += 1: {count}")

count *= 2
print(f"After count *= 2: {count}")
print()

# 3. Data Types
print("3. Data Types:")

# Numeric types
integer_num = 42
float_num = 3.14
complex_num = 3 + 4j

print(f"Integer: {integer_num} (type: {type(integer_num)})")
print(f"Float: {float_num} (type: {type(float_num)})")
print(f"Complex: {complex_num} (type: {type(complex_num)})")

# String type
text = "Hello, Python!"
print(f"String: '{text}' (type: {type(text)})")

# Boolean type
is_active = True
is_finished = False
print(f"Boolean: {is_active} (type: {type(is_active)})")
print()

# 4. Type Checking
print("4. Type Checking:")
test_values = [42, 3.14, "Hello", True, [1, 2, 3], {"a": 1}]

for value in test_values:
    print(f"Value: {value} -> Type: {type(value).__name__}")

# Using isinstance()
print("\nUsing isinstance():")
for value in test_values:
    if isinstance(value, int):
        print(f"{value} is an integer")
    elif isinstance(value, float):
        print(f"{value} is a float")
    elif isinstance(value, str):
        print(f"{value} is a string")
    elif isinstance(value, bool):
        print(f"{value} is a boolean")
    elif isinstance(value, list):
        print(f"{value} is a list")
    elif isinstance(value, dict):
        print(f"{value} is a dictionary")
print()

# 5. Type Conversion
print("5. Type Conversion:")

# String to number
number_string = "42"
float_string = "3.14"

number_int = int(number_string)
number_float = float(float_string)

print(f"String '{number_string}' to int: {number_int}")
print(f"String '{float_string}' to float: {number_float}")

# Number to string
int_to_string = str(42)
float_to_string = str(3.14)

print(f"Int {42} to string: '{int_to_string}'")
print(f"Float {3.14} to string: '{float_to_string}'")

# List conversions
string_to_list = list("Python")
tuple_to_list = list((1, 2, 3))

print(f"String 'Python' to list: {string_to_list}")
print(f"Tuple (1, 2, 3) to list: {tuple_to_list}")
print()

# 6. Memory and References
print("6. Memory and References:")

# Object identity
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print(f"a is b: {a is b}")  # False (different objects)
print(f"a is c: {a is c}")  # True (same object)
print(f"a == b: {a == b}")  # True (same values)

print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(c): {id(c)}")
print()

# 7. Mutable vs Immutable
print("7. Mutable vs Immutable:")

# Immutable example
name = "Alice"
print(f"Original name: '{name}'")
# name[0] = "B"  # This would raise an error

# Mutable example
numbers = [1, 2, 3]
print(f"Original numbers: {numbers}")
numbers[0] = 10
print(f"After modification: {numbers}")
print()

# 8. Variable Scope
print("8. Variable Scope:")

global_var = "I'm a global variable"


def test_function():
    local_var = "I'm a local variable"
    print(f"Inside function - local_var: {local_var}")
    print(f"Inside function - global_var: {global_var}")


test_function()
print(f"Outside function - global_var: {global_var}")
# print(f"Outside function - local_var: {local_var}")  # This would raise an error
print()

# 9. Truthy and Falsy Values
print("9. Truthy and Falsy Values:")

test_values = [0, 1, -1, "", "hello", [], [1, 2], None, True, False]

for value in test_values:
    truthiness = bool(value)
    print(f"Value: {value} -> bool(): {truthiness}")

print()

# 10. Practice Problems
print("10. Practice Problems:")


# Problem 1: Type conversion function
def safe_convert(value, target_type):
    try:
        if target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == str:
            return str(value)
        else:
            return None
    except (ValueError, TypeError):
        return None


# Test safe conversion
test_conversions = [
    ("42", int),
    ("3.14", float),
    ("hello", int),
    (42, str),
    (3.14, int),
]

for value, target_type in test_conversions:
    result = safe_convert(value, target_type)
    print(f"Converting {value} to {target_type.__name__}: {result}")


# Problem 2: Variable swap without temporary variable
def swap_variables(a, b):
    a, b = b, a
    return a, b


x, y = 10, 20
print(f"\nBefore swap: x = {x}, y = {y}")
x, y = swap_variables(x, y)
print(f"After swap: x = {x}, y = {y}")


# Problem 3: Check if variable is numeric
def is_numeric(value):
    return isinstance(value, (int, float))


test_numeric = [42, 3.14, "hello", True, [1, 2, 3]]
for value in test_numeric:
    result = is_numeric(value)
    print(f"{value} is numeric: {result}")


# Problem 4: Create a simple data validator
def validate_person_data(name, age, height):
    errors = []

    if not isinstance(name, str) or len(name.strip()) == 0:
        errors.append("Name must be a non-empty string")

    if not isinstance(age, int) or age < 0 or age > 150:
        errors.append("Age must be an integer between 0 and 150")

    if not isinstance(height, (int, float)) or height <= 0 or height > 3:
        errors.append("Height must be a positive number less than 3 meters")

    return errors


# Test data validation
test_persons = [
    ("Alice", 25, 1.75),
    ("", 25, 1.75),
    ("Bob", -5, 1.80),
    ("Charlie", 25, 4.0),
    ("Diana", "25", 1.65),
]

for person in test_persons:
    name, age, height = person
    errors = validate_person_data(name, age, height)
    if errors:
        print(f"Person {person}: {errors}")
    else:
        print(f"Person {person}: Valid")


# Problem 5: Type-safe calculator
def type_safe_calculator(operation, a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Both operands must be numbers"

    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: Invalid operation"


# Test type-safe calculator
test_calculations = [
    ("+", 10, 5),
    ("-", 10, 5),
    ("*", 10, 5),
    ("/", 10, 5),
    ("/", 10, 0),
    ("+", "10", 5),
]

for op, a, b in test_calculations:
    result = type_safe_calculator(op, a, b)
    print(f"{a} {op} {b} = {result}")


# Problem 6: Memory-efficient string builder
def build_string_efficiently(parts):
    return "".join(parts)


def build_string_inefficiently(parts):
    result = ""
    for part in parts:
        result += part
    return result


# Test string building
test_parts = ["Hello", " ", "World", "!", " ", "Python"]
efficient_result = build_string_efficiently(test_parts)
inefficient_result = build_string_inefficiently(test_parts)

print(f"\nEfficient result: '{efficient_result}'")
print(f"Inefficient result: '{inefficient_result}'")


# Problem 7: Variable type analyzer
def analyze_variables(variables):
    analysis = {
        "integers": [],
        "floats": [],
        "strings": [],
        "booleans": [],
        "lists": [],
        "dictionaries": [],
        "others": [],
    }

    for name, value in variables.items():
        if isinstance(value, int):
            analysis["integers"].append((name, value))
        elif isinstance(value, float):
            analysis["floats"].append((name, value))
        elif isinstance(value, str):
            analysis["strings"].append((name, value))
        elif isinstance(value, bool):
            analysis["booleans"].append((name, value))
        elif isinstance(value, list):
            analysis["lists"].append((name, value))
        elif isinstance(value, dict):
            analysis["dictionaries"].append((name, value))
        else:
            analysis["others"].append((name, value))

    return analysis


# Test variable analysis
test_variables = {
    "name": "Alice",
    "age": 25,
    "height": 1.75,
    "is_student": True,
    "scores": [85, 90, 78],
    "info": {"city": "New York", "job": "Engineer"},
    "complex_num": 3 + 4j,
}

analysis = analyze_variables(test_variables)
print("\nVariable Analysis:")
for category, variables in analysis.items():
    if variables:
        print(f"{category.capitalize()}: {variables}")

print("\n=== END OF PRACTICE ===")
