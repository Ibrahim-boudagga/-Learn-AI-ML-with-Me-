# Python Numbers Practice

print("=== PYTHON NUMBERS PRACTICE ===\n")

# 1. Basic Number Types
print("1. Basic Number Types:")
age = 25
height = 1.75
print(f"Age: {age} (type: {type(age)})")
print(f"Height: {height} (type: {type(height)})")
print()

# 2. Mathematical Operations
print("2. Mathematical Operations:")
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

# 3. Assignment Operators
print("3. Assignment Operators:")
x = 10
print(f"Initial x = {x}")

x += 5
print(f"After x += 5: x = {x}")

x -= 3
print(f"After x -= 3: x = {x}")

x *= 2
print(f"After x *= 2: x = {x}")

x /= 4
print(f"After x /= 4: x = {x}")
print()

# 4. Type Conversion
print("4. Type Conversion:")
float_num = 3.14
int_num = 42
string_num = "123"

print(f"Converting {float_num} to int: {int(float_num)}")
print(f"Converting {int_num} to float: {float(int_num)}")
print(f"Converting '{string_num}' to int: {int(string_num)}")
print(f"Converting '{string_num}' to float: {float(string_num)}")
print()

# 5. Built-in Functions
print("5. Built-in Functions:")
numbers = [1, -5, 10, -3, 8]

print(f"Numbers: {numbers}")
print(f"Absolute values: {[abs(n) for n in numbers]}")
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")
print()

# 6. Math Module
import math

print("6. Math Module:")
radius = 5
area = math.pi * radius**2

print(f"Radius: {radius}")
print(f"Area of circle: {area:.2f}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"2 to the power of 8: {math.pow(2, 8)}")
print(f"Ceiling of 3.2: {math.ceil(3.2)}")
print(f"Floor of 3.8: {math.floor(3.8)}")
print(f"Factorial of 5: {math.factorial(5)}")
print()

# 7. Practice Problems
print("7. Practice Problems:")

# Problem 1: Calculate area of a rectangle
length = 10
width = 5
area_rectangle = length * width
print(f"Rectangle area ({length} x {width}): {area_rectangle}")

# Problem 2: Convert temperature from Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Problem 3: Calculate compound interest
principal = 1000
rate = 0.05  # 5%
time = 3
amount = principal * (1 + rate) ** time
print(f"Compound interest: ${amount:.2f}")

# Problem 4: Find the largest number
numbers_list = [23, 45, 12, 67, 34, 89, 56]
largest = max(numbers_list)
print(f"Largest number in {numbers_list}: {largest}")

# Problem 5: Calculate average
grades = [85, 92, 78, 96, 88]
average_grade = sum(grades) / len(grades)
print(f"Average grade: {average_grade:.1f}")

print("\n=== END OF PRACTICE ===")
