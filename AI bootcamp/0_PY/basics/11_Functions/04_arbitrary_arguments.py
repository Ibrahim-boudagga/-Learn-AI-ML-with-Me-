# Arbitrary Arguments

print("=== ARBITRARY ARGUMENTS ===\n")


# Function with *args (arbitrary positional arguments)
def sum_all(*args):
    return sum(args)


# Function with *args and other parameters
def print_info(title, *args):
    print(f"Title: {title}")
    for arg in args:
        print(f"  {arg}")


# Function with **kwargs (arbitrary keyword arguments)
def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


# Function with both *args and **kwargs
def flexible_function(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(f"  {arg}")

    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


# Function with fixed parameters and *args
def create_profile(name, age, *hobbies, **details):
    profile = {"name": name, "age": age, "hobbies": list(hobbies), "details": details}
    return profile


# Function with *args for mathematical operations
def calculate_average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# Function with **kwargs for configuration
def configure_settings(**settings):
    default_settings = {"theme": "light", "language": "en", "notifications": True}
    default_settings.update(settings)
    return default_settings


# Testing arbitrary arguments
print("1. Basic *args:")
print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")
print(f"Sum of 10, 20: {sum_all(10, 20)}")

print("\n2. *args with other parameters:")
print_info("Student Details", "Alice", 25, "Engineer", "New York")

print("\n3. Basic **kwargs:")
print("Person details:")
person_info(name="Alice", age=25, job="Engineer", city="New York")

print("\n4. Both *args and **kwargs:")
flexible_function("apple", "banana", "orange", name="Alice", age=25)

print("\n5. Creating profiles with *args and **kwargs:")
profile1 = create_profile("Alice", 25, "reading", "swimming", city="NYC")
profile2 = create_profile(
    "Bob", 30, "gaming", "cooking", "traveling", city="London", occupation="Developer"
)

print(f"Profile 1: {profile1}")
print(f"Profile 2: {profile2}")

print("\n6. Mathematical operations with *args:")
avg1 = calculate_average(1, 2, 3, 4, 5)
avg2 = calculate_average(10, 20, 30)
print(f"Average of 1,2,3,4,5: {avg1}")
print(f"Average of 10,20,30: {avg2}")

print("\n7. Configuration with **kwargs:")
settings1 = configure_settings()
settings2 = configure_settings(theme="dark", language="es")
settings3 = configure_settings(
    theme="dark", notifications=False, font_size=14, auto_save=True
)

print(f"Default settings: {settings1}")
print(f"Custom settings: {settings2}")
print(f"Advanced settings: {settings3}")

print("\n8. Unpacking arguments:")
numbers = [1, 2, 3, 4, 5]
person_data = {"name": "Charlie", "age": 35, "city": "Paris"}

print(f"Sum using unpacking: {sum_all(*numbers)}")
print("Person info using unpacking:")
person_info(**person_data)

print("\n=== END OF ARBITRARY ARGUMENTS ===")
