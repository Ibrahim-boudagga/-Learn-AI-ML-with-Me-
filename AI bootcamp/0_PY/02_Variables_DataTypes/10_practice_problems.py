# Practice Problems

print("=== PRACTICE PROBLEMS ===\n")


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

print("\n=== END OF PRACTICE PROBLEMS ===")
