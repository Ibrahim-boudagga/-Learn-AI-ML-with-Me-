# Function Parameters

print("=== FUNCTION PARAMETERS ===\n")


# Function with default parameters
def describe_person(name, age, city="Unknown"):
    print(f"{name} is {age} years old from {city}")


# Function with multiple default parameters
def create_profile(name, age=25, city="Unknown", occupation="Unknown"):
    return {
        "name": name,
        "age": age,
        "city": city,
        "occupation": occupation,
    }


# Function with keyword-only parameters
def calculate_rectangle_area(*, length, width):
    return length * width


# Function with positional-only parameters
def calculate_circle_area(radius, /):
    import math

    return math.pi * radius**2


# Function with mixed parameter types
def mixed_params(pos_only, /, pos_or_keyword, *, keyword_only):
    return f"pos_only: {pos_only}, pos_or_keyword: {pos_or_keyword}, keyword_only: {keyword_only}"


# Testing different parameter types
print("1. Positional arguments:")
describe_person("Alice", 25, "New York")

print("\n2. Keyword arguments:")
describe_person(name="Bob", age=30, city="London")

print("\n3. Using default parameter:")
describe_person("Charlie", 35)

print("\n4. Multiple default parameters:")
profile1 = create_profile("Alice")
profile2 = create_profile("Bob", 30)
profile3 = create_profile("Charlie", 35, "Paris", "Engineer")

print(f"Profile 1: {profile1}")
print(f"Profile 2: {profile2}")
print(f"Profile 3: {profile3}")

print("\n5. Keyword-only parameters:")
area1 = calculate_rectangle_area(length=5, width=3)
area2 = calculate_rectangle_area(width=4, length=6)
print(f"Rectangle area (5x3): {area1}")
print(f"Rectangle area (6x4): {area2}")

print("\n6. Positional-only parameters:")
circle_area = calculate_circle_area(4)
print(f"Circle area (radius 4): {circle_area:.2f}")

print("\n7. Mixed parameter types:")
result = mixed_params(1, 2, keyword_only=3)
print(f"Mixed params result: {result}")

print("\n8. Parameter order examples:")
# Positional arguments must come before keyword arguments
describe_person("David", age=28, city="Berlin")

print("\n=== END OF FUNCTION PARAMETERS ===")
