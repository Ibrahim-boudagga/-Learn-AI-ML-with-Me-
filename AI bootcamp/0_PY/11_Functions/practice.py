# Python Functions Practice

print("=== PYTHON FUNCTIONS PRACTICE ===\n")

# 1. Basic Function Definition
print("1. Basic Function Definition:")


def greet():
    print("Hello, World!")


def greet_with_name(name):
    print(f"Hello, {name}!")


def add_numbers(a, b):
    return a + b


# Calling functions
greet()
greet_with_name("Alice")
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")
print()

# 2. Function Parameters
print("2. Function Parameters:")


def describe_person(name, age, city="Unknown"):
    print(f"{name} is {age} years old from {city}")


# Positional arguments
describe_person("Alice", 25, "New York")

# Keyword arguments
describe_person(name="Bob", age=30, city="London")

# Using default parameter
describe_person("Charlie", 35)
print()

# 3. Return Values
print("3. Return Values:")


def square(x):
    return x**2


def get_min_max(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)


def check_age(age):
    if age < 0:
        return "Invalid age"
    elif age < 18:
        return "Minor"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"


# Testing return values
print(f"Square of 5: {square(5)}")
numbers = [1, 2, 3, 4, 5]
min_val, max_val = get_min_max(numbers)
print(f"Min: {min_val}, Max: {max_val}")

ages = [15, 25, 70, -5]
for age in ages:
    category = check_age(age)
    print(f"Age {age}: {category}")
print()

# 4. Arbitrary Arguments
print("4. Arbitrary Arguments:")


def sum_all(*args):
    return sum(args)


def print_info(*args):
    for arg in args:
        print(f"  {arg}")


def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


# Testing arbitrary arguments
print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")
print("Info about Alice:")
print_info("Alice", 25, "Engineer", "New York")

print("Person details:")
person_info(name="Alice", age=25, job="Engineer", city="New York")
print()

# 5. Variable Scope
print("5. Variable Scope:")

global_var = "I'm global"


def test_scope():
    local_var = "I'm local"
    print(f"Inside function - local_var: {local_var}")
    print(f"Inside function - global_var: {global_var}")


def modify_global():
    global global_var
    global_var = "Modified global"
    print(f"Modified global_var to: {global_var}")


test_scope()
modify_global()
print(f"Outside function - global_var: {global_var}")
print()

# 6. Lambda Functions
print("6. Lambda Functions:")

# Basic lambda
square_lambda = lambda x: x**2
add_lambda = lambda x, y: x + y

print(f"Square of 4: {square_lambda(4)}")
print(f"Sum of 3 and 5: {add_lambda(3, 5)}")

# Lambda with conditional logic
is_even = lambda x: x % 2 == 0
get_sign = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"

test_numbers = [2, 3, 0, -1, 5]
for num in test_numbers:
    even = is_even(num)
    sign = get_sign(num)
    print(f"{num} is even: {even}, sign: {sign}")
print()

# 7. Recursion
print("7. Recursion:")


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def count_down(n):
    if n <= 0:
        print("Blast off!")
        return
    print(n)
    count_down(n - 1)


# Testing recursion
print(f"Factorial of 5: {factorial(5)}")
print(f"Fibonacci(8): {fibonacci(8)}")
print("Countdown:")
count_down(3)
print()

# 8. Higher-Order Functions
print("8. Higher-Order Functions:")


def apply_operation(func, numbers):
    return [func(num) for num in numbers]


def square(x):
    return x**2


def double(x):
    return x * 2


def create_multiplier(factor):
    def multiplier(x):
        return x * factor

    return multiplier


# Testing higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = apply_operation(square, numbers)
doubled = apply_operation(double, numbers)

print(f"Original: {numbers}")
print(f"Squared: {squared}")
print(f"Doubled: {doubled}")

# Function returning function
double_func = create_multiplier(2)
triple_func = create_multiplier(3)

print(f"Double of 5: {double_func(5)}")
print(f"Triple of 5: {triple_func(5)}")
print()

# 9. Built-in Functions with Functions
print("9. Built-in Functions with Functions:")

# map()
numbers = [1, 2, 3, 4, 5]
squared_map = list(map(lambda x: x**2, numbers))
print(f"map() result: {squared_map}")

# filter()
evens_filter = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filter() result: {evens_filter}")

# reduce()
from functools import reduce

sum_reduce = reduce(lambda x, y: x + y, numbers)
print(f"reduce() result: {sum_reduce}")
print()

# 10. Practice Problems
print("10. Practice Problems:")


# Problem 1: Calculate area of different shapes
def calculate_area(shape, *args):
    if shape == "rectangle":
        length, width = args
        return length * width
    elif shape == "circle":
        radius = args[0]
        import math

        return math.pi * radius**2
    elif shape == "triangle":
        base, height = args
        return 0.5 * base * height
    else:
        return "Unknown shape"


print(f"Rectangle area (5x3): {calculate_area('rectangle', 5, 3)}")
print(f"Circle area (radius 4): {calculate_area('circle', 4):.2f}")
print(f"Triangle area (base 6, height 4): {calculate_area('triangle', 6, 4)}")


# Problem 2: Check if number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


test_primes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for num in test_primes:
    prime = is_prime(num)
    print(f"{num} is prime: {prime}")


# Problem 3: Find GCD using Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


test_gcd = [(48, 18), (54, 24), (7, 13)]
for a, b in test_gcd:
    result1 = gcd(a, b)
    result2 = gcd_recursive(a, b)
    print(f"GCD of {a} and {b}: {result1} (iterative), {result2} (recursive)")


# Problem 4: Convert decimal to binary
def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2

    return binary


def decimal_to_binary_recursive(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary_recursive(n // 2) + str(n % 2)


test_decimals = [5, 10, 15, 255]
for num in test_decimals:
    binary1 = decimal_to_binary(num)
    binary2 = decimal_to_binary_recursive(num)
    print(f"{num} in binary: {binary1} (iterative), {binary2} (recursive)")


# Problem 5: Check if string is palindrome
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def is_palindrome_recursive(text):
    cleaned = text.lower().replace(" ", "")
    if len(cleaned) <= 1:
        return True
    if cleaned[0] != cleaned[-1]:
        return False
    return is_palindrome_recursive(cleaned[1:-1])


test_palindromes = ["racecar", "hello", "A man a plan a canal Panama", "level"]
for word in test_palindromes:
    palindrome1 = is_palindrome(word)
    palindrome2 = is_palindrome_recursive(word)
    print(
        f"'{word}' is palindrome: {palindrome1} (iterative), {palindrome2} (recursive)"
    )


# Problem 6: Generate all permutations
def generate_permutations(items):
    if len(items) <= 1:
        return [items]

    permutations = []
    for i in range(len(items)):
        current = items[i]
        remaining = items[:i] + items[i + 1 :]

        for perm in generate_permutations(remaining):
            permutations.append([current] + perm)

    return permutations


test_items = [1, 2, 3]
permutations = generate_permutations(test_items)
print(f"Permutations of {test_items}: {permutations}")


# Problem 7: Calculate compound interest
def compound_interest(principal, rate, time, compounds_per_year=1):
    rate_decimal = rate / 100
    amount = principal * (1 + rate_decimal / compounds_per_year) ** (
        compounds_per_year * time
    )
    return amount - principal


principal = 1000
rate = 5  # 5%
time = 3  # 3 years

simple_interest = compound_interest(principal, rate, time, 1)
monthly_interest = compound_interest(principal, rate, time, 12)
daily_interest = compound_interest(principal, rate, time, 365)

print(f"Principal: ${principal}")
print(f"Rate: {rate}%")
print(f"Time: {time} years")
print(f"Simple interest: ${simple_interest:.2f}")
print(f"Monthly compound: ${monthly_interest:.2f}")
print(f"Daily compound: ${daily_interest:.2f}")


# Problem 8: Find longest common subsequence
def lcs(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


test_pairs = [("ABCDGH", "AEDFHR"), ("AGGTAB", "GXTXAYB"), ("HELLO", "WORLD")]

for str1, str2 in test_pairs:
    length = lcs(str1, str2)
    print(f"LCS of '{str1}' and '{str2}': {length}")


# Problem 9: Validate credit card number (Luhn algorithm)
def validate_credit_card(card_number):
    # Remove spaces and convert to list of digits
    digits = [int(d) for d in str(card_number).replace(" ", "")]

    # Double every second digit from right
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    # Sum all digits
    total = sum(digits)

    return total % 10 == 0


test_cards = [
    "4532015112830366",  # Valid
    "4532015112830367",  # Invalid
    "1234567890123456",  # Invalid
]

for card in test_cards:
    valid = validate_credit_card(card)
    print(f"Card {card}: {'Valid' if valid else 'Invalid'}")


# Problem 10: Create a simple calculator function
def calculator(operation, *args):
    if not args:
        return "Error: No numbers provided"

    if operation == "add":
        return sum(args)
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
        return result
    elif operation == "divide":
        if len(args) < 2:
            return "Error: Need at least 2 numbers for division"
        result = args[0]
        for num in args[1:]:
            if num == 0:
                return "Error: Division by zero"
            result /= num
        return result
    elif operation == "subtract":
        if len(args) < 2:
            return "Error: Need at least 2 numbers for subtraction"
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    else:
        return "Error: Unknown operation"


# Test calculator
print(f"Add 1, 2, 3, 4: {calculator('add', 1, 2, 3, 4)}")
print(f"Multiply 2, 3, 4: {calculator('multiply', 2, 3, 4)}")
print(f"Divide 20, 4, 2: {calculator('divide', 20, 4, 2)}")
print(f"Subtract 10, 3, 2: {calculator('subtract', 10, 3, 2)}")

print("\n=== END OF PRACTICE ===")
