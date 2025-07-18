# Logical Operators

print("=== LOGICAL OPERATORS ===\n")

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

# Additional logical operator examples
print("More logical operator examples:")

# AND operator
x = 5
y = 10
z = 15
print(f"x = {x}, y = {y}, z = {z}")
print(f"x < y and y < z: {x < y and y < z}")
print(f"x > y and y < z: {x > y and y < z}")

# OR operator
username = "admin"
password = "secret123"
print(f"\nusername = '{username}', password = '{password}'")
print(
    f"username == 'admin' or password == 'secret123': {username == 'admin' or password == 'secret123'}"
)

# NOT operator
is_raining = False
print(f"\nis_raining = {is_raining}")
print(f"not is_raining: {not is_raining}")

# Complex logical expressions
temperature = 25
humidity = 60
is_sunny = True
print(f"\ntemperature = {temperature}, humidity = {humidity}, is_sunny = {is_sunny}")

if (temperature > 20 and humidity < 70) or is_sunny:
    print("Good weather for outdoor activities")
else:
    print("Stay indoors")


# Short-circuit evaluation
def expensive_function():
    print("This function is expensive!")
    return True


# With short-circuit
print("\nTesting short-circuit evaluation:")
result1 = False and expensive_function()  # expensive_function() not called
print(f"False and expensive_function(): {result1}")

result2 = True or expensive_function()  # expensive_function() not called
print(f"True or expensive_function(): {result2}")

print("\n=== END ===")
