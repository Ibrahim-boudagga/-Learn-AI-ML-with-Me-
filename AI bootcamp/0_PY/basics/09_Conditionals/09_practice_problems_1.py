# Practice Problems 1

print("=== PRACTICE PROBLEMS 1 ===\n")

# 9. Practice Problems
print("9. Practice Problems:")


# Problem 1: Calculate grade based on score
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


# Test grade calculation
test_scores = [95, 85, 75, 65, 55]
for score in test_scores:
    grade = calculate_grade(score)
    print(f"Score {score} = Grade {grade}")


# Problem 2: Get age category
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


# Test age categorization
test_ages = [-5, 10, 15, 25, 70]
for age in test_ages:
    category = get_age_category(age)
    print(f"Age {age} = {category}")


# Problem 3: Classify number
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


# Test number classification
test_numbers = [0, 5, -3, 8, -10, "hello"]
for num in test_numbers:
    classification = classify_number(num)
    print(f"Number {num} = {classification}")


# Problem 4: Check password strength
def check_password_strength(password):
    if not isinstance(password, str):
        return "Invalid input"

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


# Test password strength
test_passwords = ["abc", "password123", "Password123", "P@ssw0rd", 123]
for pwd in test_passwords:
    strength = check_password_strength(pwd)
    print(f"Password '{pwd}' = {strength}")


# Problem 5: Check leap year
def is_leap_year(year):
    if not isinstance(year, int) or year < 0:
        return False

    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


# Test leap year
test_years = [2000, 2020, 2021, 1900, 1600]
for year in test_years:
    is_leap = is_leap_year(year)
    print(f"Year {year} is leap year: {is_leap}")

print("\n=== END ===")
