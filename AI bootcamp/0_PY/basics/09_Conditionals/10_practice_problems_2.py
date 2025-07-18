# Practice Problems 2

print("=== PRACTICE PROBLEMS 2 ===\n")


# Problem 6: Classify triangle
def classify_triangle(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        return "Invalid input"

    if any(x <= 0 for x in [a, b, c]):
        return "Invalid triangle - sides must be positive"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid triangle - violates triangle inequality"

    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"


# Test triangle classification
test_triangles = [(3, 3, 3), (3, 4, 3), (3, 4, 5), (1, 1, 3), (0, 1, 2)]
for a, b, c in test_triangles:
    triangle_type = classify_triangle(a, b, c)
    print(f"Triangle ({a}, {b}, {c}) = {triangle_type}")


# Problem 7: Classify time period
def classify_time_period(hour):
    if not isinstance(hour, int) or hour < 0 or hour > 23:
        return "Invalid hour"

    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"


# Test time period classification
test_hours = [6, 12, 15, 19, 23, 25, -1]
for hour in test_hours:
    period = classify_time_period(hour)
    print(f"Hour {hour} = {period}")


# Problem 8: Check number range
def check_number_range(num, min_val, max_val, include_bounds=True):
    if not isinstance(num, (int, float)):
        return "Invalid number"

    if include_bounds:
        if min_val <= num <= max_val:
            return "In range"
        else:
            return "Out of range"
    else:
        if min_val < num < max_val:
            return "In range"
        else:
            return "Out of range"


# Test range checking
test_cases = [
    (5, 0, 10, True),
    (5, 0, 10, False),
    (0, 0, 10, True),
    (0, 0, 10, False),
    (10, 0, 10, True),
    (10, 0, 10, False),
    (15, 0, 10, True),
    ("abc", 0, 10, True),
]

for num, min_val, max_val, include_bounds in test_cases:
    result = check_number_range(num, min_val, max_val, include_bounds)
    bounds_text = "inclusive" if include_bounds else "exclusive"
    print(f"Number {num} in range [{min_val}, {max_val}] ({bounds_text}) = {result}")


# Problem 9: Classify character
def classify_character(char):
    if not isinstance(char, str) or len(char) != 1:
        return "Invalid input - must be a single character"

    if char.isupper():
        return "Uppercase letter"
    elif char.islower():
        return "Lowercase letter"
    elif char.isdigit():
        return "Digit"
    elif char.isspace():
        return "Whitespace"
    elif char in "!@#$%^&*()_+-=[]{}|;:,.<>?":
        return "Special character"
    else:
        return "Other character"


# Test character classification
test_chars = ["A", "a", "5", " ", "!", "ñ", "ab", 123]
for char in test_chars:
    classification = classify_character(char)
    print(f"Character '{char}' = {classification}")


# Problem 10: Check loan eligibility
def check_loan_eligibility(age, income, credit_score, employment_years):
    # Check basic requirements
    if age < 18:
        return "Rejected - too young"

    if income < 20000:
        return "Rejected - income too low"

    if credit_score < 300:
        return "Rejected - poor credit score"

    if employment_years < 1:
        return "Rejected - insufficient employment history"

    # Check approval levels
    if age >= 25 and income >= 50000 and credit_score >= 700 and employment_years >= 2:
        return "Approved - excellent terms"
    elif (
        age >= 21 and income >= 30000 and credit_score >= 600 and employment_years >= 1
    ):
        return "Approved - standard terms"
    else:
        return "Approved - with conditions"


# Test loan eligibility
test_applications = [
    (25, 60000, 750, 3),  # Excellent
    (22, 35000, 650, 1),  # Standard
    (30, 25000, 550, 2),  # With conditions
    (16, 40000, 800, 1),  # Too young
    (25, 15000, 700, 2),  # Income too low
    (25, 50000, 250, 2),  # Poor credit
    (25, 50000, 700, 0),  # No employment history
]

for age, income, credit_score, employment_years in test_applications:
    result = check_loan_eligibility(age, income, credit_score, employment_years)
    print(
        f"Age: {age}, Income: {income}, Credit: {credit_score}, Employment: {employment_years} years"
    )
    print(f"Result: {result}\n")

print("\n=== END ===")
