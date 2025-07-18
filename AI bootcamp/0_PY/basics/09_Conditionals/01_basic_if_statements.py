# Basic If Statements

print("=== BASIC IF STATEMENTS ===\n")

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

# Additional basic examples
print("More basic examples:")

# Simple if
temperature = 25
if temperature > 20:
    print("It's warm outside")

# If-else
score = 85
if score >= 90:
    print("Excellent!")
else:
    print("Good job, but room for improvement")

# If-elif-else
grade = 78
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

print("\n=== END ===")
