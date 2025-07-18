# CSV Files

print("=== CSV FILES ===\n")

import csv

print("1. Basic CSV Writing:")

# Create CSV data
csv_data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "London"],
    ["Charlie", "35", "Paris"],
    ["Diana", "28", "Tokyo"],
]

# Write CSV file
with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

print("Created people.csv")

# Read CSV file
print("Reading CSV file:")
with open("people.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"  {row}")

print("\n2. CSV with DictReader:")

# Read CSV with DictReader
print("Reading CSV with DictReader:")
with open("people.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"  {row['Name']} is {row['Age']} years old from {row['City']}")

print("\n3. CSV with Custom Delimiters:")

# Create CSV with semicolon delimiter
semicolon_data = [
    ["Product", "Price", "Category"],
    ["Laptop", "999.99", "Electronics"],
    ["Book", "19.99", "Education"],
    ["Phone", "599.99", "Electronics"],
]

with open("products.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerows(semicolon_data)

print("Created products.csv with semicolon delimiter")

# Read CSV with semicolon delimiter
print("Reading semicolon-delimited CSV:")
with open("products.csv", "r") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        print(f"  {row}")

print("\n4. CSV with Quotes:")

# Create CSV with quoted fields
quoted_data = [
    ["Name", "Description", "Price"],
    ["Product A", 'This is a "quoted" description', "10.99"],
    ["Product B", "Another description with, comma", "20.50"],
    ["Product C", "Simple description", "15.75"],
]

with open("quoted_products.csv", "w", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerows(quoted_data)

print("Created quoted_products.csv with all fields quoted")

# Read quoted CSV
print("Reading quoted CSV:")
with open("quoted_products.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"  {row}")

print("\n5. CSV with DictWriter:")

# Create CSV using DictWriter
dict_data = [
    {"Name": "Alice", "Age": 25, "City": "New York", "Occupation": "Engineer"},
    {"Name": "Bob", "Age": 30, "City": "London", "Occupation": "Designer"},
    {"Name": "Charlie", "Age": 35, "City": "Paris", "Occupation": "Manager"},
    {"Name": "Diana", "Age": 28, "City": "Tokyo", "Occupation": "Developer"},
]

with open("employees.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "City", "Occupation"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Write data
    writer.writerows(dict_data)

print("Created employees.csv using DictWriter")

# Read with DictReader
print("Reading employees.csv:")
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(
            f"  {row['Name']} ({row['Age']}) works as {row['Occupation']} in {row['City']}"
        )

print("\n6. CSV with Different Quote Styles:")

# Create CSV with different quote styles
data_with_quotes = [
    ["Name", "Description"],
    ["Item 1", 'Description with "quotes"'],
    ["Item 2", "Description with, comma"],
    ["Item 3", "Simple description"],
]

# QUOTE_MINIMAL (default)
with open("minimal_quotes.csv", "w", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    writer.writerows(data_with_quotes)

# QUOTE_ALL
with open("all_quotes.csv", "w", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerows(data_with_quotes)

# QUOTE_NONNUMERIC
with open("nonnumeric_quotes.csv", "w", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(data_with_quotes)

print("Created CSV files with different quote styles")

print("\n7. CSV with Custom Dialects:")

# Register a custom dialect
csv.register_dialect("custom", delimiter="|", quoting=csv.QUOTE_ALL)

# Use custom dialect
custom_data = [
    ["Name", "Value", "Category"],
    ["Item A", "100", "Category 1"],
    ["Item B", "200", "Category 2"],
]

with open("custom_dialect.csv", "w", newline="") as file:
    writer = csv.writer(file, dialect="custom")
    writer.writerows(custom_data)

print("Created custom_dialect.csv with custom dialect")

# Read with custom dialect
print("Reading custom dialect CSV:")
with open("custom_dialect.csv", "r") as file:
    reader = csv.reader(file, dialect="custom")
    for row in reader:
        print(f"  {row}")

print("\n8. CSV with Error Handling:")


def safe_csv_reader(filename):
    """Safely read CSV file with error handling."""
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            rows = []
            for row_num, row in enumerate(reader, 1):
                try:
                    rows.append(row)
                except csv.Error as e:
                    print(f"Error in row {row_num}: {e}")
            return rows
    except FileNotFoundError:
        print(f"File {filename} not found")
        return []
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return []


# Test safe CSV reader
print("Testing safe CSV reader:")
rows = safe_csv_reader("people.csv")
print(f"Successfully read {len(rows)} rows")

print("\n9. CSV with Data Validation:")


def validate_csv_data(data):
    """Validate CSV data structure."""
    if not data:
        return False, "Empty data"

    # Check if all rows have same number of columns
    expected_columns = len(data[0])
    for i, row in enumerate(data[1:], 1):
        if len(row) != expected_columns:
            return False, f"Row {i} has {len(row)} columns, expected {expected_columns}"

    return True, "Data is valid"


# Test validation
print("Testing CSV data validation:")
is_valid, message = validate_csv_data(csv_data)
print(f"Validation result: {message}")

print("\n10. CSV with Data Transformation:")

# Create CSV with mixed data types
mixed_data = [
    ["Name", "Age", "Salary", "Active"],
    ["Alice", 25, 50000.50, True],
    ["Bob", 30, 60000.75, True],
    ["Charlie", 35, 75000.25, False],
]

with open("mixed_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(mixed_data)

print("Created mixed_data.csv")

# Read and transform data
print("Reading and transforming mixed data:")
with open("mixed_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Transform data types
        name = row["Name"]
        age = int(row["Age"])
        salary = float(row["Salary"])
        active = row["Active"].lower() == "true"

        print(f"  {name}: {age} years old, ${salary:,.2f}, Active: {active}")

print("\n11. CSV with Filtering:")

# Create larger CSV for filtering
large_data = [
    ["Name", "Age", "City", "Department"],
    ["Alice", "25", "New York", "Engineering"],
    ["Bob", "30", "London", "Marketing"],
    ["Charlie", "35", "Paris", "Engineering"],
    ["Diana", "28", "Tokyo", "Sales"],
    ["Eve", "32", "Berlin", "Engineering"],
    ["Frank", "27", "Rome", "Marketing"],
]

with open("employees_large.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(large_data)

print("Created employees_large.csv")

# Filter by department
print("Filtering by department:")
with open("employees_large.csv", "r") as file:
    reader = csv.DictReader(file)
    engineering_employees = [
        row for row in reader if row["Department"] == "Engineering"
    ]

    print("Engineering employees:")
    for emp in engineering_employees:
        print(f"  {emp['Name']} from {emp['City']}")

print("\n12. CSV with Aggregation:")

# Aggregate data by department
print("Aggregating by department:")
with open("employees_large.csv", "r") as file:
    reader = csv.DictReader(file)

    dept_stats = {}
    for row in reader:
        dept = row["Department"]
        age = int(row["Age"])

        if dept not in dept_stats:
            dept_stats[dept] = {"count": 0, "total_age": 0, "employees": []}

        dept_stats[dept]["count"] += 1
        dept_stats[dept]["total_age"] += age
        dept_stats[dept]["employees"].append(row["Name"])

# Print statistics
for dept, stats in dept_stats.items():
    avg_age = stats["total_age"] / stats["count"]
    print(f"  {dept}: {stats['count']} employees, avg age: {avg_age:.1f}")
    print(f"    Employees: {', '.join(stats['employees'])}")

print("\n13. CSV with Export Options:")

# Export filtered data to new CSV
print("Exporting filtered data:")
with open("employees_large.csv", "r") as input_file:
    reader = csv.DictReader(input_file)

    # Filter engineering employees
    engineering_employees = [
        row for row in reader if row["Department"] == "Engineering"
    ]

    # Write to new CSV
    with open("engineering_employees.csv", "w", newline="") as output_file:
        if engineering_employees:
            fieldnames = engineering_employees[0].keys()
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(engineering_employees)

print("Created engineering_employees.csv with filtered data")

print("\n=== END OF CSV FILES ===")
