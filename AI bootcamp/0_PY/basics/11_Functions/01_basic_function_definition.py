# Basic Function Definition

print("=== BASIC FUNCTION DEFINITION ===\n")


# Simple function with no parameters
def greet():
    print("Hello, World!")


# Function with parameters
def greet_with_name(name):
    print(f"Hello, {name}!")


# Function with parameters and return value
def add_numbers(a, b):
    return a + b


# Function with multiple parameters
def multiply_numbers(a, b, c):
    return a * b * c


# Function with string operations
def create_full_name(first_name, last_name):
    return f"{first_name} {last_name}"


# Function with conditional logic
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False


# Calling functions
print("1. Simple function call:")
greet()

print("\n2. Function with parameters:")
greet_with_name("Alice")
greet_with_name("Bob")

print("\n3. Function with return value:")
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

print("\n4. Function with multiple parameters:")
product = multiply_numbers(2, 3, 4)
print(f"2 * 3 * 4 = {product}")

print("\n5. Function with string operations:")
full_name = create_full_name("John", "Doe")
print(f"Full name: {full_name}")

print("\n6. Function with conditional logic:")
ages = [15, 20, 25, 17]
for age in ages:
    adult = is_adult(age)
    print(f"Age {age}: {'Adult' if adult else 'Minor'}")

print("\n=== END OF BASIC FUNCTION DEFINITION ===")
