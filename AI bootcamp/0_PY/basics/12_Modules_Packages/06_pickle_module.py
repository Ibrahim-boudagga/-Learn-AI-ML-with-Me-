# Pickle Module

print("=== PICKLE MODULE ===\n")

import pickle

print("1. Basic Pickle Operations:")

# Python object to pickle
data_to_pickle = {
    "name": "Alice",
    "scores": [85, 92, 78],
    "grades": {"math": "A", "science": "B"},
    "active": True,
    "score": 95.5,
}

# Serialize Python object to pickle
pickled_data = pickle.dumps(data_to_pickle)
print(f"Pickled data size: {len(pickled_data)} bytes")
print(f"Pickled data type: {type(pickled_data)}")

# Deserialize pickle to Python object
unpickled_data = pickle.loads(pickled_data)
print(f"Unpickled data: {unpickled_data}")
print(f"Data types preserved: {type(unpickled_data)}")

print("\n2. Pickle with Different Data Types:")

# Lists
numbers = [1, 2, 3, 4, 5]
pickled_numbers = pickle.dumps(numbers)
unpickled_numbers = pickle.loads(pickled_numbers)
print(f"List - Original: {numbers}")
print(f"List - Unpickled: {unpickled_numbers}")

# Tuples
coordinates = (10, 20, 30)
pickled_coords = pickle.dumps(coordinates)
unpickled_coords = pickle.loads(pickled_coords)
print(f"Tuple - Original: {coordinates}")
print(f"Tuple - Unpickled: {unpickled_coords}")

# Sets
unique_numbers = {1, 2, 3, 4, 5}
pickled_set = pickle.dumps(unique_numbers)
unpickled_set = pickle.loads(pickled_set)
print(f"Set - Original: {unique_numbers}")
print(f"Set - Unpickled: {unpickled_set}")


# Custom objects
class Student:
    def __init__(self, name, age, courses):
        self.name = name
        self.age = age
        self.courses = courses

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, courses={self.courses})"


student = Student("Bob", 20, ["Math", "Physics", "Chemistry"])
pickled_student = pickle.dumps(student)
unpickled_student = pickle.loads(pickled_student)
print(f"Custom object - Original: {student}")
print(f"Custom object - Unpickled: {unpickled_student}")

print("\n3. Pickle with Functions:")


# Functions (with limitations)
def greet(name):
    return f"Hello, {name}!"


try:
    pickled_function = pickle.dumps(greet)
    unpickled_function = pickle.loads(pickled_function)
    result = unpickled_function("Alice")
    print(f"Function - Original: {greet('Alice')}")
    print(f"Function - Unpickled: {result}")
except Exception as e:
    print(f"Function pickling error: {e}")

print("\n4. Pickle with Lambda Functions:")

# Lambda functions
square = lambda x: x**2

try:
    pickled_lambda = pickle.dumps(square)
    unpickled_lambda = pickle.loads(pickled_lambda)
    result = unpickled_lambda(5)
    print(f"Lambda - Original: {square(5)}")
    print(f"Lambda - Unpickled: {result}")
except Exception as e:
    print(f"Lambda pickling error: {e}")

print("\n5. Pickle with Classes:")


# Class definition
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


point = Point(3, 4)
pickled_point = pickle.dumps(point)
unpickled_point = pickle.loads(pickled_point)
print(f"Class instance - Original: {point}")
print(f"Class instance - Unpickled: {unpickled_point}")
print(f"Distance - Original: {point.distance()}")
print(f"Distance - Unpickled: {unpickled_point.distance()}")

print("\n6. Pickle with Nested Structures:")

# Complex nested structure
nested_data = {
    "students": [
        Student("Alice", 20, ["Math", "Physics"]),
        Student("Bob", 22, ["Chemistry", "Biology"]),
    ],
    "courses": {
        "Math": {"credits": 3, "instructor": "Dr. Smith"},
        "Physics": {"credits": 4, "instructor": "Dr. Johnson"},
    },
    "metadata": {"semester": "Fall 2023", "total_students": 2},
}

pickled_nested = pickle.dumps(nested_data)
unpickled_nested = pickle.loads(pickled_nested)
print(f"Nested structure - Original keys: {list(nested_data.keys())}")
print(f"Nested structure - Unpickled keys: {list(unpickled_nested.keys())}")

print("\n7. Pickle with Error Handling:")


def safe_pickle_dumps(obj):
    """Safely serialize object to pickle"""
    try:
        return pickle.dumps(obj)
    except pickle.PicklingError as e:
        print(f"Pickling error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def safe_pickle_loads(pickled_data):
    """Safely deserialize pickle data"""
    try:
        return pickle.loads(pickled_data)
    except pickle.UnpicklingError as e:
        print(f"Unpickling error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


# Test safe pickling
test_objects = [
    {"name": "Alice", "age": 25},
    [1, 2, 3, 4, 5],
    "Hello, World!",
    lambda x: x * 2,  # This might fail
]

for i, obj in enumerate(test_objects, 1):
    print(f"\nTest {i}: {type(obj).__name__}")
    pickled = safe_pickle_dumps(obj)
    if pickled:
        unpickled = safe_pickle_loads(pickled)
        print(f"  Success: {unpickled}")
    else:
        print("  Failed to pickle")

print("\n8. Pickle with Different Protocols:")

# Different pickle protocols
data = {"name": "Alice", "scores": [85, 92, 78]}

for protocol in [0, 1, 2, 3, 4, 5]:
    try:
        pickled = pickle.dumps(data, protocol=protocol)
        unpickled = pickle.loads(pickled)
        print(f"Protocol {protocol}: {len(pickled)} bytes")
    except Exception as e:
        print(f"Protocol {protocol}: Error - {e}")

print("\n9. Pickle with File Operations (Simulated):")


# Simulate file operations
def save_to_pickle_file(data, filename):
    """Simulate saving data to pickle file"""
    pickled_data = pickle.dumps(data)
    print(f"Would save {len(pickled_data)} bytes to {filename}")
    return pickled_data


def load_from_pickle_file(filename):
    """Simulate loading data from pickle file"""
    # Simulate file content
    sample_data = {"name": "Alice", "age": 25}
    pickled_data = pickle.dumps(sample_data)
    unpickled_data = pickle.loads(pickled_data)
    print(f"Would load data from {filename}")
    return unpickled_data


# Test file operations
data_to_save = {"users": [{"name": "Alice"}, {"name": "Bob"}]}
saved_data = save_to_pickle_file(data_to_save, "users.pkl")
loaded_data = load_from_pickle_file("users.pkl")
print(f"Loaded data: {loaded_data}")

print("\n10. Pickle Security Considerations:")

# Warning about security
print("⚠️  Security Warning:")
print("- Never unpickle data from untrusted sources")
print("- Pickle can execute arbitrary code")
print("- Use JSON for data exchange with untrusted sources")
print("- Pickle is Python-specific and not portable")

print("\n11. Pickle vs JSON Comparison:")

# Compare pickle and JSON
complex_data = {
    "name": "Alice",
    "scores": [85, 92, 78],
    "active": True,
    "metadata": {"created": "2023-01-01"},
}

# Pickle
pickled_size = len(pickle.dumps(complex_data))
print(f"Pickle size: {pickled_size} bytes")

# JSON
import json

json_size = len(json.dumps(complex_data))
print(f"JSON size: {json_size} bytes")

print(f"Pickle is {pickled_size/json_size:.1f}x larger than JSON")

print("\n=== END OF PICKLE MODULE ===")
