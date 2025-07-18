# Practice Problems

print("=== PRACTICE PROBLEMS ===\n")


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

print("\n=== END OF PRACTICE PROBLEMS ===")
