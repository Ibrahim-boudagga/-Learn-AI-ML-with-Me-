# Higher-Order Functions

print("=== HIGHER-ORDER FUNCTIONS ===\n")


# Function that takes another function as parameter
def apply_operation(func, numbers):
    return [func(num) for num in numbers]


# Function that returns a function
def create_multiplier(factor):
    def multiplier(x):
        return x * factor

    return multiplier


# Function that takes multiple functions
def apply_multiple_operations(operations, numbers):
    results = {}
    for name, func in operations.items():
        results[name] = [func(num) for num in numbers]
    return results


# Function that returns different functions based on condition
def get_operation(operation_type):
    if operation_type == "square":
        return lambda x: x**2
    elif operation_type == "double":
        return lambda x: x * 2
    elif operation_type == "increment":
        return lambda x: x + 1
    else:
        return lambda x: x


# Function that creates a decorator-like pattern
def create_validator(condition_func):
    def validator(value):
        if condition_func(value):
            return True, "Valid"
        else:
            return False, "Invalid"

    return validator


# Function that combines multiple functions
def compose(*functions):
    def composed(x):
        result = x
        for func in reversed(functions):
            result = func(result)
        return result

    return composed


# Function that creates a memoization wrapper
def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


# Function that creates a retry mechanism
def retry(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed, retrying...")
            return None

        return wrapper

    return decorator


# Testing higher-order functions
print("1. Function as parameter:")
numbers = [1, 2, 3, 4, 5]


def square(x):
    return x**2


def double(x):
    return x * 2


squared = apply_operation(square, numbers)
doubled = apply_operation(double, numbers)

print(f"Original: {numbers}")
print(f"Squared: {squared}")
print(f"Doubled: {doubled}")

print("\n2. Function returning function:")
double_func = create_multiplier(2)
triple_func = create_multiplier(3)
quadruple_func = create_multiplier(4)

print(f"Double of 5: {double_func(5)}")
print(f"Triple of 5: {triple_func(5)}")
print(f"Quadruple of 5: {quadruple_func(5)}")

print("\n3. Multiple operations:")
operations = {"square": square, "double": double, "increment": lambda x: x + 1}

results = apply_multiple_operations(operations, numbers)
for operation, result in results.items():
    print(f"{operation}: {result}")

print("\n4. Dynamic function selection:")
operation_types = ["square", "double", "increment", "unknown"]
for op_type in operation_types:
    func = get_operation(op_type)
    result = func(5)
    print(f"{op_type}(5) = {result}")

print("\n5. Function composition:")


def add_one(x):
    return x + 1


def multiply_by_two(x):
    return x * 2


def square_compose(x):
    return x**2


composed_func = compose(add_one, multiply_by_two, square_compose)
result = composed_func(3)
print(f"compose(add_one, multiply_by_two, square)(3) = {result}")

print("\n6. Validator creation:")
is_positive = create_validator(lambda x: x > 0)
is_even = create_validator(lambda x: x % 2 == 0)
is_adult = create_validator(lambda x: x >= 18)

test_values = [5, -3, 10, 15, 20]
for value in test_values:
    pos_valid, pos_msg = is_positive(value)
    even_valid, even_msg = is_even(value)
    adult_valid, adult_msg = is_adult(value)
    print(f"{value}: positive={pos_msg}, even={even_msg}, adult={adult_msg}")

print("\n7. Memoization:")


@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci with memoization:")
for i in range(10):
    result = fibonacci(i)
    print(f"fibonacci({i}) = {result}")

print("\n8. Retry mechanism:")


@retry(max_attempts=3)
def risky_function(should_fail=True):
    if should_fail:
        raise ValueError("Simulated failure")
    return "Success"


print("Testing retry mechanism:")
try:
    result = risky_function(should_fail=True)
    print(f"Result: {result}")
except Exception as e:
    print(f"Final error: {e}")

print("\n9. Function factory:")


def create_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter1 = create_counter()
counter2 = create_counter()

print("Function factory - counters:")
for i in range(3):
    print(f"Counter1: {counter1()}, Counter2: {counter2()}")

print("\n10. Higher-order function with partial application:")
from functools import partial


def power(base, exponent):
    return base**exponent


square_partial = partial(power, exponent=2)
cube_partial = partial(power, exponent=3)

print("Partial application:")
print(f"square(5) = {square_partial(5)}")
print(f"cube(3) = {cube_partial(3)}")

print("\n=== END OF HIGHER-ORDER FUNCTIONS ===")
