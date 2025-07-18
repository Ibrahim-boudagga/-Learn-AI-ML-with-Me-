# Accessing Dictionary Elements

print("=== ACCESSING DICTIONARY ELEMENTS ===\n")

# 2. Accessing Dictionary Elements
print("2. Accessing Dictionary Elements:")
student = {"name": "Alice", "age": 20, "grade": "A", "subjects": ["Math", "Physics"]}

# Using square brackets
name = student["name"]
print(f"Name: {name}")

# Using get() method
age = student.get("age")
grade = student.get("grade")
job = student.get("job")  # Returns None
job_safe = student.get("job", "Student")  # Returns default value

print(f"Age: {age}")
print(f"Grade: {grade}")
print(f"Job (not found): {job}")
print(f"Job with default: {job_safe}")

# Checking if key exists
print(f"'name' in student: {'name' in student}")
print(f"'job' in student: {'job' in student}")

# Getting all keys, values, and items
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")
print()

# Additional access methods
print("More access methods:")

# Accessing nested dictionaries
nested = {
    "user": {"name": "Alice", "profile": {"age": 25, "city": "NYC"}},
    "settings": {"theme": "dark"},
}

user_name = nested["user"]["name"]
user_age = nested["user"]["profile"]["age"]
print(f"User name: {user_name}")
print(f"User age: {user_age}")

# Safe nested access
try:
    theme = nested["settings"]["theme"]
    print(f"Theme: {theme}")
except KeyError:
    print("Theme not found")

# Using get() for nested access
user_city = nested.get("user", {}).get("profile", {}).get("city", "Unknown")
print(f"User city: {user_city}")

# Iterating through dictionary
print("\nIterating through dictionary:")
for key in student:
    print(f"  {key}: {student[key]}")

print("\nIterating through items:")
for key, value in student.items():
    print(f"  {key}: {value}")

print("\n=== END ===")
