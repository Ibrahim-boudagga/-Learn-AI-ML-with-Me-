# Python File Handling Practice

print("=== PYTHON FILE HANDLING PRACTICE ===\n")

# 1. Basic File Operations
print("1. Basic File Operations:")

# Create a sample file for practice
sample_content = """This is line 1
This is line 2
This is line 3
This is line 4
This is line 5"""

# Write sample file
with open("sample.txt", "w") as file:
    file.write(sample_content)

print("Created sample.txt with content")

# Read the file
with open("sample.txt", "r") as file:
    content = file.read()
    print(f"File content:\n{content}")

# Read line by line
print("\nReading line by line:")
with open("sample.txt", "r") as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")

# Read all lines as list
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(f"\nAll lines as list: {lines}")
print()

# 2. File Modes
print("2. File Modes:")

# Write mode (overwrites)
with open("test.txt", "w") as file:
    file.write("Original content")

print("Created test.txt with original content")

# Append mode
with open("test.txt", "a") as file:
    file.write("\nAppended content")

print("Appended content to test.txt")

# Read the final file
with open("test.txt", "r") as file:
    final_content = file.read()
    print(f"Final content:\n{final_content}")

# Read and write mode
with open("test.txt", "r+") as file:
    content = file.read()
    file.seek(0)
    file.write("Modified content\n")
    file.write(content)

print("Modified file using r+ mode")
print()

# 3. File Object Methods
print("3. File Object Methods:")

with open("sample.txt", "r") as file:
    # Get initial position
    position = file.tell()
    print(f"Initial position: {position}")

    # Read first 10 characters
    first_10 = file.read(10)
    print(f"First 10 characters: '{first_10}'")

    # Get position after reading
    position = file.tell()
    print(f"Position after reading 10 chars: {position}")

    # Seek to beginning
    file.seek(0)
    print(f"Position after seek(0): {file.tell()}")

    # Seek to middle
    file.seek(20)
    print(f"Position after seek(20): {file.tell()}")

    # Read from current position
    remaining = file.read()
    print(f"Remaining content: '{remaining}'")
print()

# 4. File Information
print("4. File Information:")

import os

# Check if file exists
if os.path.exists("sample.txt"):
    print("sample.txt exists")

    # Get file size
    size = os.path.getsize("sample.txt")
    print(f"File size: {size} bytes")

    # Get file modification time
    mtime = os.path.getmtime("sample.txt")
    print(f"Modified time: {mtime}")

    # Get absolute path
    abs_path = os.path.abspath("sample.txt")
    print(f"Absolute path: {abs_path}")
else:
    print("sample.txt does not exist")
print()

# 5. CSV Files
print("5. CSV Files:")

import csv

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

# Read CSV with DictReader
print("\nReading CSV with DictReader:")
with open("people.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"  {row['Name']} is {row['Age']} years old from {row['City']}")
print()

# 6. JSON Files
print("6. JSON Files:")

import json

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
print()

# 7. Binary Files
print("7. Binary Files:")

# Create binary data
binary_data = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09"

# Write binary file
with open("data.bin", "wb") as file:
    file.write(binary_data)

print("Created data.bin")

# Read binary file
with open("data.bin", "rb") as file:
    loaded_binary = file.read()
    print(f"Binary data: {loaded_binary}")
    print(f"Data length: {len(loaded_binary)} bytes")
    print(f"As integers: {list(loaded_binary)}")
print()

# 8. Directory Operations
print("8. Directory Operations:")

# List current directory
current_files = os.listdir(".")
print(f"Files in current directory: {current_files}")

# Create a new directory
os.makedirs("test_folder", exist_ok=True)
print("Created test_folder")

# Check if it's a directory
if os.path.isdir("test_folder"):
    print("test_folder is a directory")

# Create a file in the new directory
with open("test_folder/test_file.txt", "w") as file:
    file.write("Test content")

print("Created test_file.txt in test_folder")

# List contents of test_folder
folder_contents = os.listdir("test_folder")
print(f"Contents of test_folder: {folder_contents}")
print()

# 9. Error Handling
print("9. Error Handling:")


def safe_read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: Permission denied for '{filename}'"
    except Exception as e:
        return f"Error reading '{filename}': {e}"


def safe_write_file(filename, content):
    try:
        with open(filename, "w") as file:
            file.write(content)
        return f"Successfully wrote to '{filename}'"
    except Exception as e:
        return f"Error writing to '{filename}': {e}"


# Test safe file operations
print(safe_read_file("sample.txt"))
print(safe_read_file("nonexistent.txt"))
print(safe_write_file("new_file.txt", "New content"))
print()

# 10. Working with Large Files
print("10. Working with Large Files:")

# Create a large file for demonstration
large_content = "This is line {}\n" * 1000
with open("large_file.txt", "w") as file:
    file.write(large_content.format(*range(1, 1001)))

print("Created large_file.txt with 1000 lines")


# Read large file in chunks
def read_large_file(filename, chunk_size=1024):
    with open(filename, "r") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk


# Process large file in chunks
chunk_count = 0
total_chars = 0
for chunk in read_large_file("large_file.txt"):
    chunk_count += 1
    total_chars += len(chunk)

print(f"Processed large file in {chunk_count} chunks")
print(f"Total characters: {total_chars}")


# Line by line processing
def process_large_file(filename):
    with open(filename, "r") as file:
        for line_number, line in enumerate(file, 1):
            if line_number <= 5:  # Show first 5 lines
                processed_line = line.strip().upper()
                print(f"Line {line_number}: {processed_line}")
            elif line_number == 1000:  # Show last line
                processed_line = line.strip().upper()
                print(f"Line {line_number}: {processed_line}")


print("Processing large file line by line:")
process_large_file("large_file.txt")
print()

# 11. File Compression
print("11. File Compression:")

import zipfile

# Create files to compress
with open("file1.txt", "w") as file:
    file.write("Content of file 1")

with open("file2.txt", "w") as file:
    file.write("Content of file 2")

print("Created file1.txt and file2.txt")

# Create ZIP file
with zipfile.ZipFile("archive.zip", "w") as zip_file:
    zip_file.write("file1.txt")
    zip_file.write("file2.txt")

print("Created archive.zip")

# List ZIP contents
with zipfile.ZipFile("archive.zip", "r") as zip_file:
    contents = zip_file.namelist()
    print(f"ZIP contents: {contents}")

# Extract ZIP file
os.makedirs("extracted", exist_ok=True)
with zipfile.ZipFile("archive.zip", "r") as zip_file:
    zip_file.extractall("extracted")

print("Extracted files to 'extracted' folder")
extracted_files = os.listdir("extracted")
print(f"Extracted files: {extracted_files}")
print()

# 12. Logging to Files
print("12. Logging to Files:")

import logging

# Configure basic logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Log some messages
logging.info("Application started")
logging.warning("This is a warning message")
logging.error("This is an error message")

print("Logged messages to app.log")

# Read the log file
with open("app.log", "r") as file:
    log_content = file.read()
    print("Log file content:")
    print(log_content)
print()

# 13. Practice Problems
print("13. Practice Problems:")


# Problem 1: File word counter
def count_words_in_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"


word_count = count_words_in_file("sample.txt")
print(f"Word count in sample.txt: {word_count}")


# Problem 2: File line counter
def count_lines_in_file(filename):
    try:
        with open(filename, "r") as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"


line_count = count_lines_in_file("sample.txt")
print(f"Line count in sample.txt: {line_count}")


# Problem 3: Find longest word in file
def find_longest_word(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            if not words:
                return "No words found"
            return max(words, key=len)
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"


longest_word = find_longest_word("sample.txt")
print(f"Longest word in sample.txt: '{longest_word}'")


# Problem 4: Copy file with modifications
def copy_file_with_modifications(source, destination, transform_func):
    try:
        with open(source, "r") as source_file:
            content = source_file.read()

        modified_content = transform_func(content)

        with open(destination, "w") as dest_file:
            dest_file.write(modified_content)

        return f"Successfully copied and modified '{source}' to '{destination}'"
    except FileNotFoundError:
        return f"Error: File '{source}' not found"
    except Exception as e:
        return f"Error: {e}"


# Transform function to uppercase
def to_uppercase(content):
    return content.upper()


result = copy_file_with_modifications(
    "sample.txt", "sample_uppercase.txt", to_uppercase
)
print(result)


# Problem 5: Merge multiple files
def merge_files(filenames, output_filename):
    try:
        with open(output_filename, "w") as output_file:
            for filename in filenames:
                try:
                    with open(filename, "r") as input_file:
                        output_file.write(f"=== {filename} ===\n")
                        output_file.write(input_file.read())
                        output_file.write("\n\n")
                except FileNotFoundError:
                    output_file.write(f"=== {filename} (not found) ===\n\n")

        return f"Successfully merged files to '{output_filename}'"
    except Exception as e:
        return f"Error: {e}"


result = merge_files(["sample.txt", "test.txt"], "merged.txt")
print(result)


# Problem 6: Search and replace in file
def search_and_replace(filename, search_text, replace_text):
    try:
        with open(filename, "r") as file:
            content = file.read()

        modified_content = content.replace(search_text, replace_text)

        with open(filename, "w") as file:
            file.write(modified_content)

        return f"Successfully replaced '{search_text}' with '{replace_text}' in '{filename}'"
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error: {e}"


result = search_and_replace("sample.txt", "line", "LINE")
print(result)


# Problem 7: Create a simple database file
def create_database_file(filename):
    database = {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"},
            {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
        ],
        "settings": {"debug": True, "max_users": 100, "timeout": 30},
    }

    with open(filename, "w") as file:
        json.dump(database, file, indent=2)

    return f"Created database file '{filename}'"


result = create_database_file("database.json")
print(result)


# Problem 8: Read and parse database file
def read_database_file(filename):
    try:
        with open(filename, "r") as file:
            database = json.load(file)

        print("Database contents:")
        print("Users:")
        for user in database["users"]:
            print(f"  ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")

        print("Settings:")
        for key, value in database["settings"].items():
            print(f"  {key}: {value}")

        return "Successfully read database"
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except json.JSONDecodeError:
        return f"Error: Invalid JSON in '{filename}'"


result = read_database_file("database.json")
print(result)


# Problem 9: Create a log analyzer
def analyze_log_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        log_levels = {}
        for line in lines:
            if " - " in line:
                parts = line.split(" - ")
                if len(parts) >= 2:
                    level = parts[1].split(" - ")[0]
                    log_levels[level] = log_levels.get(level, 0) + 1

        print("Log analysis:")
        for level, count in log_levels.items():
            print(f"  {level}: {count} messages")

        return f"Analyzed {len(lines)} log entries"
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"


result = analyze_log_file("app.log")
print(result)


# Problem 10: Create a file backup system
def create_backup(filename):
    import datetime

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"{filename}.backup_{timestamp}"

    try:
        with open(filename, "r") as source_file:
            content = source_file.read()

        with open(backup_filename, "w") as backup_file:
            backup_file.write(content)

        return f"Created backup: {backup_filename}"
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error creating backup: {e}"


result = create_backup("sample.txt")
print(result)

# Clean up created files
files_to_clean = [
    "sample.txt",
    "test.txt",
    "new_file.txt",
    "large_file.txt",
    "people.csv",
    "person.json",
    "data.bin",
    "file1.txt",
    "file2.txt",
    "archive.zip",
    "app.log",
    "sample_uppercase.txt",
    "merged.txt",
    "database.json",
    "sample.txt.backup_*",
]

print("\nCleaning up created files...")
for filename in files_to_clean:
    try:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Removed {filename}")
    except:
        pass

# Clean up directories
import shutil

try:
    shutil.rmtree("test_folder")
    shutil.rmtree("extracted")
    print("Removed test directories")
except:
    pass

print("\n=== END OF PRACTICE ===")
