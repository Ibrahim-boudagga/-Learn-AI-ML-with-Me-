# Return Values

print("=== RETURN VALUES ===\n")


# Function returning single value
def get_min_max(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)


# Function returning different types based on condition
def check_age(age):
    if age < 0:
        return "Invalid age"
    elif age < 18:
        return "Minor"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"


# Function returning multiple values
def calculate_stats(numbers):
    if not numbers:
        return None, None, None, None

    total = sum(numbers)
    count = len(numbers)
    average = total / count
    variance = sum((x - average) ** 2 for x in numbers) / count

    return total, count, average, variance


# Function returning a list
def get_even_numbers(limit):
    return [i for i in range(2, limit + 1, 2)]


# Function returning a dictionary
def create_person_dict(name, age, city):
    return {"name": name, "age": age, "city": city, "adult": age >= 18}


# Function returning a tuple
def get_coordinates():
    return (10, 20)


# Function returning None (implicit)
def print_greeting(name):
    print(f"Hello, {name}!")


# Function returning boolean
def is_even(number):
    return number % 2 == 0


# Testing return values
print("1. Multiple return values:")
numbers = [1, 2, 3, 4, 5]
min_val, max_val = get_min_max(numbers)
print(f"Min: {min_val}, Max: {max_val}")

print("\n2. Conditional return values:")
ages = [15, 25, 70, -5]
for age in ages:
    category = check_age(age)
    print(f"Age {age}: {category}")

print("\n3. Complex return values:")
stats = calculate_stats([1, 2, 3, 4, 5])
if stats[0] is not None:
    total, count, avg, var = stats
    print(f"Total: {total}, Count: {count}, Average: {avg:.2f}, Variance: {var:.2f}")

print("\n4. Returning lists:")
even_nums = get_even_numbers(10)
print(f"Even numbers up to 10: {even_nums}")

print("\n5. Returning dictionaries:")
person = create_person_dict("Alice", 25, "New York")
print(f"Person dict: {person}")

print("\n6. Returning tuples:")
x, y = get_coordinates()
print(f"Coordinates: ({x}, {y})")

print("\n7. Function returning None:")
result = print_greeting("Bob")
print(f"Return value: {result}")

print("\n8. Boolean return values:")
test_numbers = [2, 3, 4, 5, 6]
for num in test_numbers:
    even = is_even(num)
    print(f"{num} is even: {even}")

print("\n=== END OF RETURN VALUES ===")
