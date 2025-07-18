# JSON Files

print("=== JSON FILES ===\n")

import json

print("1. Basic JSON Writing and Reading:")

# Create JSON data
json_data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "swimming", "coding"],
    "active": True,
    "scores": {"math": 95, "science": 88, "english": 92},
}

# Write JSON file
with open("person.json", "w") as file:
    json.dump(json_data, file, indent=2)

print("Created person.json")

# Read JSON file
with open("person.json", "r") as file:
    loaded_data = json.load(file)
    print("Loaded JSON data:")
    print(f"  Name: {loaded_data['name']}")
    print(f"  Age: {loaded_data['age']}")
    print(f"  City: {loaded_data['city']}")
    print(f"  Hobbies: {loaded_data['hobbies']}")
    print(f"  Active: {loaded_data['active']}")
    print(f"  Scores: {loaded_data['scores']}")

print("\n2. JSON with Different Data Types:")

# JSON with various data types
complex_data = {
    "string": "Hello, World!",
    "number": 42,
    "float": 3.14159,
    "boolean": True,
    "null": None,
    "list": [1, 2, 3, "four", True, None],
    "nested_dict": {"inner": "value", "numbers": [1, 2, 3]},
    "empty_list": [],
    "empty_dict": {},
}

with open("complex_data.json", "w") as file:
    json.dump(complex_data, file, indent=2)

print("Created complex_data.json")

# Read and display all data types
with open("complex_data.json", "r") as file:
    loaded_complex = json.load(file)
    print("Complex data types:")
    for key, value in loaded_complex.items():
        print(f"  {key}: {value} ({type(value).__name__})")

print("\n3. JSON with Custom Objects:")


# Custom class with to_dict method
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def to_dict(self):
        return {"name": self.name, "age": self.age, "city": self.city}

    def __repr__(self):
        return f"Person({self.name}, {self.age}, {self.city})"


# Custom JSON encoder
class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return obj.to_dict()
        return super().default(obj)


# Create and serialize Person objects
people = [
    Person("Alice", 25, "New York"),
    Person("Bob", 30, "London"),
    Person("Charlie", 35, "Paris"),
]

with open("people_objects.json", "w") as file:
    json.dump(people, file, cls=PersonEncoder, indent=2)

print("Created people_objects.json with custom objects")

# Read and reconstruct objects
with open("people_objects.json", "r") as file:
    people_data = json.load(file)
    print("Loaded people data:")
    for person_data in people_data:
        person = Person(person_data["name"], person_data["age"], person_data["city"])
        print(f"  {person}")

print("\n4. JSON with Pretty Printing:")

# Different formatting options
data_to_format = {
    "name": "Alice",
    "details": {"age": 25, "hobbies": ["reading", "swimming"]},
}

# Compact JSON
compact_json = json.dumps(data_to_format, separators=(",", ":"))
print("Compact JSON:")
print(compact_json)

# Pretty JSON with 2 spaces
pretty_json = json.dumps(data_to_format, indent=2)
print("\nPretty JSON (2 spaces):")
print(pretty_json)

# Pretty JSON with 4 spaces
pretty_json_4 = json.dumps(data_to_format, indent=4)
print("\nPretty JSON (4 spaces):")
print(pretty_json_4)

print("\n5. JSON with Sorting:")

# JSON with sorted keys
sorted_json = json.dumps(data_to_format, indent=2, sort_keys=True)
print("JSON with sorted keys:")
print(sorted_json)

print("\n6. JSON with Error Handling:")


def safe_json_load(filename):
    """Safely load JSON file with error handling."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {filename}: {e}")
        return None
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None


def safe_json_dump(data, filename):
    """Safely dump JSON data to file."""
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=2)
        return True
    except Exception as e:
        print(f"Error writing {filename}: {e}")
        return False


# Test safe JSON operations
print("Testing safe JSON operations:")
result = safe_json_load("person.json")
if result:
    print("Successfully loaded person.json")

result = safe_json_load("nonexistent.json")
if result is None:
    print("Handled missing file correctly")

print("\n7. JSON with Validation:")


def validate_json_structure(data, required_fields):
    """Validate JSON structure has required fields."""
    if not isinstance(data, dict):
        return False, "Data is not a dictionary"

    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)

    if missing_fields:
        return False, f"Missing fields: {missing_fields}"

    return True, "Valid structure"


# Test validation
required_fields = ["name", "age", "city"]
is_valid, message = validate_json_structure(loaded_data, required_fields)
print(f"JSON validation: {message}")

print("\n8. JSON with Nested Structures:")

# Complex nested structure
nested_data = {
    "company": {
        "name": "TechCorp",
        "employees": [
            {
                "id": 1,
                "name": "Alice",
                "department": "Engineering",
                "skills": ["Python", "JavaScript", "SQL"],
                "projects": [
                    {"name": "Project A", "status": "active"},
                    {"name": "Project B", "status": "completed"},
                ],
            },
            {
                "id": 2,
                "name": "Bob",
                "department": "Marketing",
                "skills": ["SEO", "Content Writing"],
                "projects": [{"name": "Campaign X", "status": "active"}],
            },
        ],
        "departments": {
            "Engineering": {"head": "Alice", "size": 50},
            "Marketing": {"head": "Bob", "size": 20},
        },
    }
}

with open("nested_structure.json", "w") as file:
    json.dump(nested_data, file, indent=2)

print("Created nested_structure.json")

# Navigate nested structure
with open("nested_structure.json", "r") as file:
    nested_loaded = json.load(file)

    company_name = nested_loaded["company"]["name"]
    print(f"Company: {company_name}")

    employees = nested_loaded["company"]["employees"]
    print(f"Number of employees: {len(employees)}")

    for emp in employees:
        print(f"  {emp['name']} ({emp['department']})")
        print(f"    Skills: {', '.join(emp['skills'])}")
        print(f"    Projects: {len(emp['projects'])}")

print("\n9. JSON with Date Handling:")

import datetime

# JSON with date objects
date_data = {
    "created_at": datetime.datetime.now().isoformat(),
    "updated_at": datetime.datetime.now().isoformat(),
    "events": [
        {"date": "2023-01-01", "description": "New Year"},
        {"date": "2023-12-25", "description": "Christmas"},
    ],
}

with open("date_data.json", "w") as file:
    json.dump(date_data, file, indent=2)

print("Created date_data.json with date information")


# Custom date encoder
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super().default(obj)


# Use custom encoder
datetime_data = {"created": datetime.datetime.now(), "updated": datetime.datetime.now()}

with open("datetime_data.json", "w") as file:
    json.dump(datetime_data, file, cls=DateTimeEncoder, indent=2)

print("Created datetime_data.json with custom date encoding")

print("\n10. JSON with Streaming (Large Files):")

# Create large JSON data
large_data = {
    "items": [{"id": i, "name": f"Item {i}", "value": i * 10} for i in range(1000)]
}

with open("large_data.json", "w") as file:
    json.dump(large_data, file, indent=2)

print("Created large_data.json with 1000 items")


# Read large JSON in chunks (simulated)
def process_large_json(filename):
    """Process large JSON file efficiently."""
    with open(filename, "r") as file:
        data = json.load(file)

        # Process items in batches
        items = data.get("items", [])
        batch_size = 100

        for i in range(0, len(items), batch_size):
            batch = items[i : i + batch_size]
            print(f"Processing batch {i//batch_size + 1}: {len(batch)} items")


process_large_json("large_data.json")

print("\n11. JSON with Compression:")

import gzip

# Compress JSON data
with open("person.json", "r") as file:
    data = json.load(file)

# Write compressed JSON
with gzip.open("person.json.gz", "wt") as file:
    json.dump(data, file, indent=2)

print("Created compressed person.json.gz")

# Read compressed JSON
with gzip.open("person.json.gz", "rt") as file:
    compressed_data = json.load(file)
    print("Read compressed JSON:")
    print(f"  Name: {compressed_data['name']}")

print("\n12. JSON with Schema Validation (Basic):")


def validate_person_schema(data):
    """Basic schema validation for person data."""
    if not isinstance(data, dict):
        return False, "Data must be an object"

    required_fields = ["name", "age", "city"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"

    if not isinstance(data["name"], str):
        return False, "Name must be a string"

    if not isinstance(data["age"], int):
        return False, "Age must be an integer"

    if not isinstance(data["city"], str):
        return False, "City must be a string"

    return True, "Valid person data"


# Test schema validation
test_person = {"name": "Alice", "age": 25, "city": "New York"}
is_valid, message = validate_person_schema(test_person)
print(f"Schema validation: {message}")

invalid_person = {"name": "Bob", "age": "thirty", "city": "London"}
is_valid, message = validate_person_schema(invalid_person)
print(f"Invalid schema validation: {message}")

print("\n=== END OF JSON FILES ===")
