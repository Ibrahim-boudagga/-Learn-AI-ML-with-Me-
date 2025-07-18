# Python Conditionals Practice

print("=== PYTHON CONDITIONALS PRACTICE ===\n")

# 1. Basic If Statements
print("1. Basic If Statements:")
age = 18

if age >= 18:
    print("You are an adult")

age = 16
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

age = 15
if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")
print()

# 2. Comparison Operators
print("2. Comparison Operators:")
x = 10
y = 5

print(f"x = {x}, y = {y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")

# String comparisons
name1 = "Alice"
name2 = "Bob"
print(f"\nname1 = '{name1}', name2 = '{name2}'")
print(f"name1 < name2: {name1 < name2}")
print(f"name1 == name2: {name1 == name2}")
print(f"name1 != name2: {name1 != name2}")
print()

# 3. Identity and Membership
print("3. Identity and Membership:")
# Identity operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"x = {x}, y = {y}, z = x")
print(f"x is y: {x is y}")
print(f"x is z: {x is z}")
print(f"x == y: {x == y}")

# Membership operators
fruits = ["apple", "banana", "orange"]
print(f"\nfruits = {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")
print()

# 4. Logical Operators
print("4. Logical Operators:")
age = 25
income = 50000

# AND operator
if age >= 18 and income >= 30000:
    print("Eligible for loan")

# OR operator
age = 16
parent_consent = True
if age >= 18 or parent_consent:
    print("Can participate")

# NOT operator
is_student = False
if not is_student:
    print("Must pay full price")

# Combining logical operators
age = 25
income = 50000
credit_score = 750
print(f"\nAge: {age}, Income: {income}, Credit Score: {credit_score}")

if age >= 18 and income >= 30000 and credit_score >= 700:
    print("Approved for loan")
elif age >= 18 and (income >= 50000 or credit_score >= 800):
    print("Approved with conditions")
else:
    print("Not approved")
print()

# 5. Nested Conditionals
print("5. Nested Conditionals:")
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
print()

# 6. Ternary Operator
print("6. Ternary Operator:")
age = 20

# Traditional if-else
if age >= 18:
    status = "adult"
else:
    status = "minor"
print(f"Traditional: {status}")

# Ternary operator
status = "adult" if age >= 18 else "minor"
print(f"Ternary: {status}")

# Multiple conditions
grade = 85
letter_grade = (
    "A" if grade >= 90 else "B" if grade >= 80 else "C" if grade >= 70 else "F"
)
print(f"Grade {grade} = {letter_grade}")
print()

# 7. Truthy and Falsy Values
print("7. Truthy and Falsy Values:")
# Falsy values
falsy_values = [False, None, 0, "", [], {}, ()]

print("Falsy values:")
for value in falsy_values:
    if value:
        print(f"  {value} is truthy")
    else:
        print(f"  {value} is falsy")

# Truthy values
truthy_values = [True, 1, "hello", [1, 2], {"a": 1}]

print("\nTruthy values:")
for value in truthy_values:
    if value:
        print(f"  {value} is truthy")
    else:
        print(f"  {value} is falsy")
print()

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
        return sum(data)
    else:
        return "Unknown type"


print(f"process_data('hello'): {process_data('hello')}")
print(f"process_data(5): {process_data(5)}")
print(f"process_data([1, 2, 3]): {process_data([1, 2, 3])}")
print()

# 9. Practice Problems
print("9. Practice Problems:")


# Problem 1: Grade calculator
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


test_scores = [95, 85, 75, 65, 55]
for score in test_scores:
    grade = calculate_grade(score)
    print(f"Score {score} = Grade {grade}")


# Problem 2: Age category
def get_age_category(age):
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"


test_ages = [-5, 10, 15, 25, 70]
for age in test_ages:
    category = get_age_category(age)
    print(f"Age {age} = {category}")


# Problem 3: Number classifier
def classify_number(num):
    if not isinstance(num, (int, float)):
        return "Not a number"

    if num == 0:
        return "Zero"
    elif num > 0:
        if num % 2 == 0:
            return "Positive even"
        else:
            return "Positive odd"
    else:
        if num % 2 == 0:
            return "Negative even"
        else:
            return "Negative odd"


test_numbers = [0, 5, -3, 8, -10, "hello"]
for num in test_numbers:
    classification = classify_number(num)
    print(f"{num} = {classification}")


# Problem 4: Password strength checker
def check_password_strength(password):
    if len(password) < 8:
        return "Weak - too short"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()" for c in password)

    if has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif has_upper and has_lower and has_digit:
        return "Medium"
    else:
        return "Weak"


test_passwords = ["abc", "password", "Password123", "StrongP@ss1"]
for password in test_passwords:
    strength = check_password_strength(password)
    print(f"'{password}' = {strength}")


# Problem 5: Leap year checker
def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


test_years = [2000, 2004, 2100, 2024]
for year in test_years:
    leap = is_leap_year(year)
    print(f"{year} is leap year: {leap}")


# Problem 6: Triangle type classifier
def classify_triangle(a, b, c):
    if not (a > 0 and b > 0 and c > 0):
        return "Invalid - sides must be positive"

    if a + b <= c or b + c <= a or a + c <= b:
        return "Invalid - triangle inequality"

    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"


test_triangles = [(3, 3, 3), (3, 4, 4), (3, 4, 5), (1, 1, 3)]
for sides in test_triangles:
    triangle_type = classify_triangle(*sides)
    print(f"Triangle {sides} = {triangle_type}")


# Problem 7: Time period classifier
def classify_time_period(hour):
    if not (0 <= hour <= 23):
        return "Invalid hour"

    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"


test_hours = [6, 12, 18, 23, 25]
for hour in test_hours:
    period = classify_time_period(hour)
    print(f"Hour {hour} = {period}")


# Problem 8: Number range checker
def check_number_range(num, min_val, max_val, include_bounds=True):
    if include_bounds:
        return min_val <= num <= max_val
    else:
        return min_val < num < max_val


test_ranges = [
    (5, 1, 10, True),
    (5, 1, 10, False),
    (1, 1, 10, True),
    (1, 1, 10, False),
    (10, 1, 10, True),
    (10, 1, 10, False),
]

for num, min_val, max_val, include_bounds in test_ranges:
    in_range = check_number_range(num, min_val, max_val, include_bounds)
    bounds_text = "inclusive" if include_bounds else "exclusive"
    print(f"{num} in range [{min_val}, {max_val}] ({bounds_text}): {in_range}")


# Problem 9: Character type classifier
def classify_character(char):
    if len(char) != 1:
        return "Invalid - not a single character"

    if char.isupper():
        return "Uppercase letter"
    elif char.islower():
        return "Lowercase letter"
    elif char.isdigit():
        return "Digit"
    elif char.isspace():
        return "Whitespace"
    else:
        return "Special character"


test_chars = ["A", "a", "5", " ", "!", "Hello"]
for char in test_chars:
    char_type = classify_character(char)
    print(f"'{char}' = {char_type}")


# Problem 10: Complex eligibility checker
def check_loan_eligibility(age, income, credit_score, employment_years):
    # Check basic requirements
    if age < 18:
        return "Denied - too young"

    if income < 25000:
        return "Denied - income too low"

    if credit_score < 600:
        return "Denied - poor credit"

    if employment_years < 1:
        return "Denied - insufficient employment history"

    # Check for excellent conditions
    if age >= 25 and income >= 75000 and credit_score >= 750 and employment_years >= 3:
        return "Approved - excellent terms"

    # Check for good conditions
    if age >= 22 and income >= 50000 and credit_score >= 700 and employment_years >= 2:
        return "Approved - good terms"

    # Check for standard conditions
    if age >= 20 and income >= 35000 and credit_score >= 650 and employment_years >= 1:
        return "Approved - standard terms"

    return "Denied - does not meet requirements"


test_applicants = [
    (25, 80000, 800, 5),  # Excellent
    (23, 60000, 720, 2),  # Good
    (21, 40000, 680, 1),  # Standard
    (17, 30000, 700, 1),  # Too young
    (25, 20000, 750, 3),  # Income too low
    (25, 50000, 550, 2),  # Poor credit
    (25, 50000, 700, 0),  # No employment history
]

for applicant in test_applicants:
    age, income, credit_score, employment_years = applicant
    result = check_loan_eligibility(age, income, credit_score, employment_years)
    print(f"Applicant {applicant}: {result}")

print("\n=== END OF PRACTICE ===")
