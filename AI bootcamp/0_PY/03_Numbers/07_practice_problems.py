# Practice Problems

print("=== PRACTICE PROBLEMS ===\n")

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

print("\n=== END OF PRACTICE PROBLEMS ===")
