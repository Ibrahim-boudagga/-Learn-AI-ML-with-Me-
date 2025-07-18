# Python Tuples Practice

print("=== PYTHON TUPLES PRACTICE ===\n")

# 1. Tuple Creation and Basic Operations
print("1. Tuple Creation and Basic Operations:")
numbers = (1, 2, 3, 4, 5)
names = ("Alice", "Bob", "Charlie")
mixed = (1, "hello", 3.14, True)

print(f"Numbers: {numbers}")
print(f"Names: {names}")
print(f"Mixed: {mixed}")
print(f"Length of numbers: {len(numbers)}")
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
print()

# 2. Tuple Slicing
print("2. Tuple Slicing:")
data = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(f"Original tuple: {data}")
print(f"First 3 elements: {data[:3]}")
print(f"Last 3 elements: {data[-3:]}")
print(f"Middle elements (3-7): {data[3:7]}")
print(f"Every second element: {data[::2]}")
print(f"Reverse: {data[::-1]}")
print()

# 3. Tuple Methods
print("3. Tuple Methods:")
fruits = ("apple", "banana", "orange", "apple", "grape")
print(f"Fruits: {fruits}")

print(f"Count of 'apple': {fruits.count('apple')}")
print(f"Index of 'banana': {fruits.index('banana')}")
print(f"'orange' in fruits: {'orange' in fruits}")
print(f"'kiwi' in fruits: {'kiwi' in fruits}")
print()

# 4. Tuple Operations
print("4. Tuple Operations:")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print(f"Combined: {combined}")

# Repetition
repeated = tuple1 * 3
print(f"Repeated: {repeated}")

# Comparison
print(f"tuple1 == tuple2: {tuple1 == tuple2}")
print(f"tuple1 < tuple2: {tuple1 < tuple2}")  # type: ignore
print()

# 5. Tuple Unpacking
print("5. Tuple Unpacking:")
coordinates = (10, 20)
x, y = coordinates
print(f"Coordinates: x={x}, y={y}")

# Multiple assignment
a, b, c = (1, 2, 3)
print(f"Multiple assignment: a={a}, b={b}, c={c}")

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
print(f"Extended unpacking: first={first}, middle={middle}, last={last}")

# Ignoring values with underscore
name, age, _ = ("Alice", 25, "Engineer")
print(f"Ignoring values: name={name}, age={age}")
print()

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

# 7. Named Tuples
print("7. Named Tuples:")
from collections import namedtuple

# Creating a named tuple
Person = namedtuple("Person", ["name", "age", "city"])

# Creating instances
person1 = Person("Alice", 25, "New York")
person2 = Person("Bob", 30, "London")

print(f"Person 1: {person1.name} is {person1.age} years old from {person1.city}")
print(f"Person 2: {person2.name} is {person2.age} years old from {person2.city}")

# Accessing by index
print(f"Person 1 by index: {person1[0]} is {person1[1]} years old from {person1[2]}")

# Converting to dictionary
person_dict = person1._asdict()
print(f"Person 1 as dictionary: {person_dict}")
print()

# 8. Built-in Functions with Tuples
print("8. Built-in Functions with Tuples:")
numbers = (1, 2, 3, 4, 5)
print(f"Numbers: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Any non-zero: {any(numbers)}")
print(f"All non-zero: {all(numbers)}")

# enumerate()
print("\nEnumerate:")
for index, value in enumerate(numbers):
    print(f"  Index {index}: {value}")

# zip()
names = ("Alice", "Bob", "Charlie")
ages = (25, 30, 35)
print("\nZip:")
for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")
print()

# 9. Tuple vs List
print("9. Tuple vs List:")
# Tuples are immutable
coordinates = (10, 20)
print(f"Original coordinates: {coordinates}")

# This would raise an error:
# coordinates[0] = 100  # TypeError

# But we can create a new tuple
new_coordinates = coordinates + (30,)
print(f"New coordinates: {new_coordinates}")

# Lists are mutable
coordinates_list = [10, 20]
coordinates_list[0] = 100
print(f"Modified list: {coordinates_list}")
print()

# 10. Practice Problems
print("10. Practice Problems:")


# Problem 1: Calculate distance between two points
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


p1 = (0, 0)
p2 = (3, 4)
distance = calculate_distance(p1, p2)
print(f"Distance between {p1} and {p2}: {distance}")


# Problem 2: Find the center point of multiple coordinates
def find_center(points):
    if not points:
        return None
    x_sum = sum(point[0] for point in points)
    y_sum = sum(point[1] for point in points)
    count = len(points)
    return (x_sum / count, y_sum / count)


points = [(0, 0), (2, 0), (2, 2), (0, 2)]
center = find_center(points)
print(f"Center of points {points}: {center}")


# Problem 3: Convert RGB to grayscale
def rgb_to_grayscale(rgb):
    r, g, b = rgb
    gray = 0.299 * r + 0.587 * g + 0.114 * b
    return int(gray)


color = (255, 128, 0)  # Orange
grayscale = rgb_to_grayscale(color)
print(f"RGB {color} to grayscale: {grayscale}")


# Problem 4: Swap values using tuples
def swap_values(a, b):
    return (b, a)


x, y = 10, 20
print(f"Before swap: x={x}, y={y}")
x, y = swap_values(x, y)
print(f"After swap: x={x}, y={y}")


# Problem 5: Extract data from database records
def process_user_records(records):
    total_age = 0
    cities = set()
    engineers = []

    for name, age, job, city in records:
        total_age += age
        cities.add(city)
        if job == "Engineer":
            engineers.append(name)

    return {
        "average_age": total_age / len(records),
        "unique_cities": len(cities),
        "engineers": engineers,
    }


user_records = [
    ("Alice", 25, "Engineer", "New York"),
    ("Bob", 30, "Designer", "London"),
    ("Charlie", 35, "Engineer", "San Francisco"),
    ("Diana", 28, "Manager", "New York"),
]

result = process_user_records(user_records)
print(f"User records analysis:")
print(f"  Average age: {result['average_age']:.1f}")
print(f"  Unique cities: {result['unique_cities']}")
print(f"  Engineers: {result['engineers']}")


# Problem 6: Create a simple coordinate system
class CoordinateSystem:
    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def get_bounds(self):
        if not self.points:
            return None

        min_x = min(point[0] for point in self.points)
        max_x = max(point[0] for point in self.points)
        min_y = min(point[1] for point in self.points)
        max_y = max(point[1] for point in self.points)

        return ((min_x, min_y), (max_x, max_y))

    def get_points_in_quadrant(self, quadrant):
        if quadrant not in [1, 2, 3, 4]:
            return []

        filtered_points = []
        for point in self.points:
            x, y = point
            if quadrant == 1 and x > 0 and y > 0:
                filtered_points.append(point)
            elif quadrant == 2 and x < 0 and y > 0:
                filtered_points.append(point)
            elif quadrant == 3 and x < 0 and y < 0:
                filtered_points.append(point)
            elif quadrant == 4 and x > 0 and y < 0:
                filtered_points.append(point)

        return filtered_points


# Test the coordinate system
coord_system = CoordinateSystem()
coord_system.add_point((1, 1))
coord_system.add_point((-1, 1))
coord_system.add_point((-1, -1))
coord_system.add_point((1, -1))
coord_system.add_point((0, 0))

bounds = coord_system.get_bounds()
print(f"Coordinate system bounds: {bounds}")

for quadrant in range(1, 5):
    points = coord_system.get_points_in_quadrant(quadrant)
    print(f"Quadrant {quadrant}: {points}")

print("\n=== END OF PRACTICE ===")
