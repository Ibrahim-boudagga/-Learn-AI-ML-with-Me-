# Common Conditional Patterns

print("=== COMMON CONDITIONAL PATTERNS ===\n")

# 8. Common Conditional Patterns
print("8. Common Conditional Patterns:")

# Range checking
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
print(f"Score {score} = Grade {grade}")

# Multiple conditions
username = "admin"
password = "secret123"
is_active = True

if username == "admin" and password == "secret123" and is_active:
    print("Login successful")
else:
    print("Login failed")


# Type checking
def process_data(data):
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, (int, float)):
        return data * 2
    elif isinstance(data, list):
        return len(data)
    else:
        return "Unknown type"


# Test type checking
print(f"\nType checking examples:")
print(f"String 'hello': {process_data('hello')}")
print(f"Number 42: {process_data(42)}")
print(f"List [1, 2, 3]: {process_data([1, 2, 3])}")
print(f"Boolean True: {process_data(True)}")

# Additional pattern examples
print("\nMore pattern examples:")


# Guard clauses
def process_user(user):
    if not user:
        return "No user provided"

    if not user.get("name"):
        return "User has no name"

    if user.get("age", 0) < 18:
        return "User is too young"

    return f"Processing user: {user['name']}"


# Test guard clauses
print("Guard clause examples:")
print(process_user(None))
print(process_user({"age": 25}))
print(process_user({"name": "Alice", "age": 16}))
print(process_user({"name": "Bob", "age": 25}))


# Switch-like patterns
def get_day_name(day_number):
    day_names = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    return day_names.get(day_number, "Invalid day")


print(f"\nSwitch-like pattern:")
print(f"Day 1: {get_day_name(1)}")
print(f"Day 5: {get_day_name(5)}")
print(f"Day 10: {get_day_name(10)}")


# Early return pattern
def validate_input(value, min_val, max_val):
    if value is None:
        return False, "Value cannot be None"

    if not isinstance(value, (int, float)):
        return False, "Value must be numeric"

    if value < min_val:
        return False, f"Value too small (min: {min_val})"

    if value > max_val:
        return False, f"Value too large (max: {max_val})"

    return True, "Valid input"


print(f"\nEarly return pattern:")
print(validate_input(None, 0, 100))
print(validate_input("abc", 0, 100))
print(validate_input(-5, 0, 100))
print(validate_input(150, 0, 100))
print(validate_input(50, 0, 100))

print("\n=== END ===")
