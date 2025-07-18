# Practice Problems 2

print("=== PRACTICE PROBLEMS 2 ===\n")


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


# Additional practice problems
print("\nAdditional Practice Problems:")


# Problem 7: Calculate area of triangle using coordinates
def calculate_triangle_area(point1, point2, point3):
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3

    area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
    return area


triangle_points = [(0, 0), (4, 0), (2, 3)]
area = calculate_triangle_area(*triangle_points)
print(f"Triangle area with points {triangle_points}: {area}")


# Problem 8: Find closest point to origin
def find_closest_to_origin(points):
    if not points:
        return None

    def distance_to_origin(point):
        x, y = point
        return (x**2 + y**2) ** 0.5

    return min(points, key=distance_to_origin)


test_points = [(3, 4), (1, 1), (5, 0), (2, 2)]
closest = find_closest_to_origin(test_points)
print(f"Closest point to origin from {test_points}: {closest}")


# Problem 9: Convert between coordinate systems
def cartesian_to_polar(point):
    import math

    x, y = point
    r = (x**2 + y**2) ** 0.5
    theta = math.atan2(y, x)
    return (r, theta)


def polar_to_cartesian(point):
    import math

    r, theta = point
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)


# Test coordinate conversion
cartesian_point = (3, 4)
polar_point = cartesian_to_polar(cartesian_point)
back_to_cartesian = polar_to_cartesian(polar_point)

print(f"Cartesian {cartesian_point} -> Polar {polar_point}")
print(f"Polar {polar_point} -> Cartesian {back_to_cartesian}")


# Problem 10: Validate coordinate data
def validate_coordinates(coordinates):
    valid_points = []
    invalid_points = []

    for point in coordinates:
        if len(point) == 2:
            x, y = point
            if isinstance(x, (int, float)) and isinstance(y, (int, float)):
                valid_points.append(point)
            else:
                invalid_points.append(point)
        else:
            invalid_points.append(point)

    return valid_points, invalid_points


test_coords = [(1, 2), (3, 4), (5,), (6, 7, 8), ("a", "b"), (1.5, 2.5)]
valid, invalid = validate_coordinates(test_coords)
print(f"Valid coordinates: {valid}")
print(f"Invalid coordinates: {invalid}")

print("\n=== END ===")
