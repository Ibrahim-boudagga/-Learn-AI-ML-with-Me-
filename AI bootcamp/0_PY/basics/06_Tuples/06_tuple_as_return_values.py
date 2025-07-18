# Tuple as Return Values

print("=== TUPLE AS RETURN VALUES ===\n")

# 6. Tuple as Return Values
print("6. Tuple as Return Values:")


def get_coordinates():
    return (10, 20)


def get_person_info():
    return ("Alice", 25, "Engineer")


coords = get_coordinates()
x, y = coords
print(f"Coordinates from function: ({x}, {y})")

person_info = get_person_info()
name, age, job = person_info
print(f"Person info: {name}, {age} years old, {job}")
print()

# Additional examples
print("More return value examples:")


def calculate_stats(numbers):
    """Return min, max, and average of a list of numbers."""
    if not numbers:
        return None
    return (min(numbers), max(numbers), sum(numbers) / len(numbers))


def get_rectangle_info(width, height):
    """Return area, perimeter, and diagonal of a rectangle."""
    area = width * height
    perimeter = 2 * (width + height)
    diagonal = (width**2 + height**2) ** 0.5
    return (area, perimeter, diagonal)


# Test the functions
test_numbers = [1, 2, 3, 4, 5]
stats = calculate_stats(test_numbers)
if stats:
    min_val, max_val, avg = stats
    print(f"Stats for {test_numbers}: min={min_val}, max={max_val}, avg={avg:.2f}")

rect_info = get_rectangle_info(3, 4)
area, perimeter, diagonal = rect_info
print(f"Rectangle (3x4): area={area}, perimeter={perimeter}, diagonal={diagonal:.2f}")


# Multiple return values with unpacking
def get_circle_info(radius):
    """Return diameter, circumference, and area of a circle."""
    import math

    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    area = math.pi * radius**2
    return (diameter, circumference, area)


circle_info = get_circle_info(5)
diameter, circumference, area = circle_info
print(
    f"Circle (r=5): diameter={diameter}, circumference={circumference:.2f}, area={area:.2f}"
)

print("\n=== END ===")
