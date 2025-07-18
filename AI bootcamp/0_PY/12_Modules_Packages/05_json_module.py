# JSON Module

print("=== JSON MODULE ===\n")

import json

print("1. Basic JSON Operations:")

# Python object to JSON
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "swimming"],
    "active": True,
    "score": 95.5,
    "address": {"street": "123 Main St", "zipcode": "10001"},
}

# Convert Python object to JSON string
json_string = json.dumps(data, indent=2)
print("Python to JSON:")
print(json_string)

# Convert JSON string to Python object
parsed_data = json.loads(json_string)
print(f"\nJSON to Python - name: {parsed_data['name']}")
print(f"JSON to Python - age: {parsed_data['age']}")
print(f"JSON to Python - hobbies: {parsed_data['hobbies']}")

print("\n2. JSON with Different Data Types:")

# Lists
numbers = [1, 2, 3, 4, 5]
numbers_json = json.dumps(numbers)
print(f"List to JSON: {numbers_json}")

# Tuples (converted to lists)
coordinates = (10, 20)
coordinates_json = json.dumps(coordinates)
print(f"Tuple to JSON: {coordinates_json}")

# Sets (not directly serializable)
try:
    unique_numbers = {1, 2, 3, 4, 5}
    json.dumps(unique_numbers)
except TypeError as e:
    print(f"Error serializing set: {e}")
    # Convert set to list for JSON
    set_json = json.dumps(list(unique_numbers))
    print(f"Set as list to JSON: {set_json}")

print("\n3. JSON with Custom Objects:")


# Custom class with to_dict method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {"name": self.name, "age": self.age}


person = Person("Bob", 30)
person_dict = person.to_dict()
person_json = json.dumps(person_dict)
print(f"Custom object to JSON: {person_json}")


# Custom JSON encoder
class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return obj.to_dict()
        return super().default(obj)


person_json_custom = json.dumps(person, cls=PersonEncoder)
print(f"Custom encoder JSON: {person_json_custom}")

print("\n4. JSON File Operations:")

# Working with JSON files
sample_data = {
    "users": [
        {"name": "Alice", "age": 25, "city": "New York"},
        {"name": "Bob", "age": 30, "city": "London"},
        {"name": "Charlie", "age": 35, "city": "Paris"},
    ],
    "settings": {"theme": "dark", "language": "en", "notifications": True},
}

# Write to JSON file (simulated)
print("Data to write to file:")
print(json.dumps(sample_data, indent=2))

# Read from JSON file (simulated)
print(f"\nData read from file: {sample_data}")

print("\n5. JSON with Pretty Printing:")

# Pretty printing with different indent levels
compact_json = json.dumps(data)
print(f"Compact JSON: {compact_json}")

indent_2_json = json.dumps(data, indent=2)
print(f"\nIndent 2 JSON:\n{indent_2_json}")

indent_4_json = json.dumps(data, indent=4)
print(f"\nIndent 4 JSON:\n{indent_4_json}")

print("\n6. JSON with Sorting:")

# Sort keys
sorted_json = json.dumps(data, indent=2, sort_keys=True)
print("JSON with sorted keys:")
print(sorted_json)

print("\n7. JSON with Custom Separators:")

# Custom separators
custom_json = json.dumps(data, separators=(",", ": "))
print("JSON with custom separators:")
print(custom_json)

print("\n8. JSON with Unicode Handling:")

# Unicode data
unicode_data = {
    "message": "Hello, 世界!",
    "emoji": "🚀",
    "special_chars": "café résumé naïve",
}

unicode_json = json.dumps(unicode_data, ensure_ascii=False)
print("JSON with Unicode:")
print(unicode_json)

print("\n9. JSON Validation:")

# Valid JSON
valid_json = '{"name": "Alice", "age": 25}'
try:
    parsed = json.loads(valid_json)
    print(f"Valid JSON parsed: {parsed}")
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")

# Invalid JSON
invalid_json = '{"name": "Alice", "age": 25,}'  # Trailing comma
try:
    parsed = json.loads(invalid_json)
    print(f"Valid JSON parsed: {parsed}")
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")

print("\n10. JSON with Nested Structures:")

# Complex nested structure
complex_data = {
    "company": {
        "name": "TechCorp",
        "employees": [
            {
                "id": 1,
                "name": "Alice",
                "department": "Engineering",
                "skills": ["Python", "JavaScript", "SQL"],
            },
            {
                "id": 2,
                "name": "Bob",
                "department": "Marketing",
                "skills": ["SEO", "Content Writing"],
            },
        ],
        "departments": {
            "Engineering": {"head": "Alice", "size": 50},
            "Marketing": {"head": "Bob", "size": 20},
        },
    }
}

complex_json = json.dumps(complex_data, indent=2)
print("Complex nested JSON:")
print(complex_json)

print("\n11. JSON with Date Handling:")

import datetime

# Date object (not directly serializable)
date_obj = datetime.datetime.now()
print(f"Date object: {date_obj}")

# Convert date to string for JSON
date_data = {"created_at": date_obj.isoformat(), "timestamp": date_obj.timestamp()}

date_json = json.dumps(date_data, indent=2)
print("Date in JSON:")
print(date_json)

print("\n12. JSON with Error Handling:")


def safe_json_loads(json_string):
    """Safely parse JSON string"""
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


# Test safe parsing
test_cases = [
    '{"name": "Alice", "age": 25}',
    '{"name": "Alice", "age": 25,}',  # Invalid
    '{"name": "Alice", "age": "invalid"}',  # Valid but age is string
    "not json at all",
]

for i, test_case in enumerate(test_cases, 1):
    result = safe_json_loads(test_case)
    print(f"Test {i}: {result}")

print("\n=== END OF JSON MODULE ===")
