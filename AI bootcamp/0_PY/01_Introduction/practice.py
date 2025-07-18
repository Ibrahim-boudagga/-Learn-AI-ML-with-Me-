# Python Introduction Practice

print("=== PYTHON INTRODUCTION PRACTICE ===\n")

# 1. Your First Program
print("1. Your First Program:")
print("Hello, World!")
print("Welcome to Python!")
print()

# 2. Variables and Data Types
print("2. Variables and Data Types:")
name = "Alice"
age = 25
height = 1.75
is_student = True

print(f"Name: {name} (type: {type(name)})")
print(f"Age: {age} (type: {type(age)})")
print(f"Height: {height} (type: {type(height)})")
print(f"Is student: {is_student} (type: {type(is_student)})")
print()

# 3. Mathematical Operations
print("3. Mathematical Operations:")
a = 15
b = 4

print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulo: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")
print()

# 4. String Operations
print("4. String Operations:")
first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

greeting = f"Hello, {full_name}!"
print(f"Greeting: {greeting}")

print(f"Upper case: {full_name.upper()}")
print(f"Lower case: {full_name.lower()}")
print(f"Title case: {full_name.title()}")
print(f"Length: {len(full_name)}")
print()

# 5. Type Conversion
print("5. Type Conversion:")
number_string = "42"
float_string = "3.14"

number_int = int(number_string)
number_float = float(float_string)

print(f"String '{number_string}' to int: {number_int}")
print(f"String '{float_string}' to float: {number_float}")
print(f"Int {number_int} to string: '{str(number_int)}'")
print()

# 6. Input and Output
print("6. Input and Output:")
# Uncomment the following lines to test input
# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))
# print(f"Hello {user_name}, you are {user_age} years old!")

# Simulating input for demonstration
user_name = "Alice"
user_age = 25
print(f"Hello {user_name}, you are {user_age} years old!")
print()

# 7. Control Flow - If Statements
print("7. Control Flow - If Statements:")
ages = [15, 18, 25, 12, 30]

for age in ages:
    if age >= 18:
        print(f"Age {age}: Adult")
    elif age >= 13:
        print(f"Age {age}: Teenager")
    else:
        print(f"Age {age}: Child")
print()

# 8. Loops
print("8. Loops:")
print("For loop (range 5):")
for i in range(5):
    print(f"  Count: {i}")

print("\nWhile loop:")
count = 0
while count < 3:
    print(f"  While count: {count}")
    count += 1

print("\nFor loop with list:")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"  Fruit: {fruit}")
print()

# 9. Functions
print("9. Functions:")


def greet(name):
    return f"Hello, {name}!"


def add_numbers(a, b):
    return a + b


def calculate_area(length, width):
    return length * width


# Testing functions
print(f"Greet function: {greet('Alice')}")
print(f"Add numbers: {add_numbers(5, 3)}")
print(f"Calculate area: {calculate_area(4, 6)}")
print()

# 10. Built-in Functions
print("10. Built-in Functions:")
numbers = [1, 2, 3, 4, 5]
text = "Python Programming"

print(f"Numbers: {numbers}")
print(f"Length of numbers: {len(numbers)}")
print(f"Sum of numbers: {sum(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")

print(f"\nText: '{text}'")
print(f"Length: {len(text)}")
print(f"Upper: '{text.upper()}'")
print(f"Lower: '{text.lower()}'")
print()

# 11. Practice Problems
print("11. Practice Problems:")


# Problem 1: Calculate average of three numbers
def calculate_average(a, b, c):
    return (a + b + c) / 3


test_numbers = [10, 20, 30]
average = calculate_average(*test_numbers)
print(f"Average of {test_numbers}: {average}")


# Problem 2: Convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


celsius_temp = 25
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C = {fahrenheit_temp}°F")


# Problem 3: Check if number is even or odd
def is_even(number):
    return number % 2 == 0


test_numbers = [2, 3, 4, 5, 6]
for num in test_numbers:
    result = "even" if is_even(num) else "odd"
    print(f"{num} is {result}")


# Problem 4: Calculate simple interest
def calculate_interest(principal, rate, time):
    return principal * rate * time / 100


principal = 1000
rate = 5  # 5%
time = 2  # 2 years
interest = calculate_interest(principal, rate, time)
print(f"Simple interest: ${interest}")


# Problem 5: Reverse a string
def reverse_string(text):
    return text[::-1]


test_string = "Python"
reversed_string = reverse_string(test_string)
print(f"Original: '{test_string}' -> Reversed: '{reversed_string}'")


# Problem 6: Check if string is palindrome
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


test_palindromes = ["racecar", "hello", "A man a plan a canal Panama"]
for word in test_palindromes:
    result = "is" if is_palindrome(word) else "is not"
    print(f"'{word}' {result} a palindrome")


# Problem 7: Generate multiplication table
def print_multiplication_table(n):
    print(f"Multiplication table for {n}:")
    for i in range(1, 11):
        print(f"  {n} x {i} = {n * i}")


print_multiplication_table(5)
print()


# Problem 8: Calculate factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


factorial_test = 5
result = factorial(factorial_test)
print(f"Factorial of {factorial_test}: {result}")


# Problem 9: Check if year is leap year
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
    result = "is" if is_leap_year(year) else "is not"
    print(f"{year} {result} a leap year")


# Problem 10: Simple calculator
def calculator(operation, a, b):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"


# Test calculator
operations = [("+", 10, 5), ("-", 10, 5), ("*", 10, 5), ("/", 10, 5)]
for op, a, b in operations:
    result = calculator(op, a, b)
    print(f"{a} {op} {b} = {result}")

print("\n=== END OF PRACTICE ===")
