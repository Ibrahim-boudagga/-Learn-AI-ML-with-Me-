# Nested Conditionals

print("=== NESTED CONDITIONALS ===\n")

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

# Additional nested conditional examples
print("More nested conditional examples:")

# Nested if-else with multiple levels
username = "admin"
password = "secret123"
is_active = True
has_permission = True

if username == "admin":
    if password == "secret123":
        if is_active:
            if has_permission:
                print("Full access granted")
            else:
                print("Access denied - insufficient permissions")
        else:
            print("Account is inactive")
    else:
        print("Invalid password")
else:
    print("User not found")

# Nested conditionals with different scenarios
temperature = 30
humidity = 80
is_weekend = True

print(
    f"\ntemperature = {temperature}, humidity = {humidity}, is_weekend = {is_weekend}"
)

if temperature > 25:
    if humidity > 70:
        if is_weekend:
            print("Stay home and watch movies")
        else:
            print("Use air conditioning at work")
    else:
        if is_weekend:
            print("Go to the beach")
        else:
            print("Enjoy the warm weather")
else:
    if humidity > 70:
        print("It's cool but humid")
    else:
        print("Pleasant weather")

# Complex nested structure
student_grade = 85
attendance = 90
participation = 75

print(
    f"\nstudent_grade = {student_grade}, attendance = {attendance}, participation = {participation}"
)

if student_grade >= 80:
    if attendance >= 85:
        if participation >= 80:
            print("Excellent student - recommend for honors")
        else:
            print("Good student - encourage more participation")
    else:
        if participation >= 80:
            print("Good student - improve attendance")
        else:
            print("Average student - needs improvement in attendance and participation")
else:
    if attendance >= 85:
        print("Student needs academic support")
    else:
        print("Student needs comprehensive support")

print("\n=== END ===")
