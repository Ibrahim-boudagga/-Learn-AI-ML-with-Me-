# Practice Problems 1

print("=== PRACTICE PROBLEMS 1 ===\n")

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

print("\n=== END ===")
