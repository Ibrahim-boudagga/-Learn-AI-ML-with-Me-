# Ternary Operator

print("=== TERNARY OPERATOR ===\n")

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

# Additional ternary operator examples
print("More ternary operator examples:")

# Simple ternary
x = 10
y = 5
result = "x is greater" if x > y else "y is greater or equal"
print(f"x = {x}, y = {y}")
print(f"Result: {result}")

# Ternary with different data types
temperature = 25
weather = "warm" if temperature > 20 else "cold"
print(f"Temperature: {temperature}°C")
print(f"Weather: {weather}")

# Ternary with string operations
name = "Alice"
greeting = f"Hello {name}!" if name else "Hello stranger!"
print(f"Name: {name}")
print(f"Greeting: {greeting}")

# Ternary with list operations
numbers = [1, 2, 3, 4, 5]
message = "List has elements" if numbers else "List is empty"
print(f"Numbers: {numbers}")
print(f"Message: {message}")

# Complex ternary expressions
score = 85
feedback = (
    "Excellent!"
    if score >= 90
    else (
        "Good job!"
        if score >= 80
        else (
            "Not bad!"
            if score >= 70
            else "Keep trying!" if score >= 60 else "Need improvement!"
        )
    )
)
print(f"Score: {score}")
print(f"Feedback: {feedback}")


# Ternary with function calls
def get_status(age, income):
    return "Eligible" if age >= 18 and income >= 30000 else "Not eligible"


person_age = 25
person_income = 50000
eligibility = get_status(person_age, person_income)
print(f"Age: {person_age}, Income: {person_income}")
print(f"Loan eligibility: {eligibility}")

print("\n=== END ===")
