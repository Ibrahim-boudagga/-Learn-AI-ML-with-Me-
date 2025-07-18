# Python File Handling

## Overview
File handling in Python allows you to read from and write to files on your computer. Python provides built-in functions and methods to work with different types of files.

## Basic File Operations

### Opening Files
```python
# Basic file opening
file = open("example.txt", "r")
content = file.read()
file.close()

# Using with statement (recommended)
with open("example.txt", "r") as file:
    content = file.read()
```

### File Modes
```python
# Read mode (default)
with open("file.txt", "r") as file:
    content = file.read()

# Write mode (overwrites existing content)
with open("file.txt", "w") as file:
    file.write("Hello, World!")

# Append mode (adds to existing content)
with open("file.txt", "a") as file:
    file.write("\nNew line")

# Read and write mode
with open("file.txt", "r+") as file:
    content = file.read()
    file.write("Additional content")

# Binary mode
with open("image.jpg", "rb") as file:
    binary_data = file.read()
```

## Reading Files

### Reading Entire File
```python
# Read entire file as string
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Read with encoding
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

### Reading Line by Line
```python
# Read all lines as list
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# Read line by line (memory efficient)
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read specific number of characters
with open("example.txt", "r") as file:
    first_100 = file.read(100)
    print(first_100)
```

### Reading with Different Methods
```python
with open("example.txt", "r") as file:
    # Read first line
    first_line = file.readline()
    print(f"First line: {first_line}")
    
    # Read next line
    second_line = file.readline()
    print(f"Second line: {second_line}")
    
    # Read remaining content
    remaining = file.read()
    print(f"Remaining: {remaining}")
```

## Writing Files

### Writing Text
```python
# Write string to file
with open("output.txt", "w") as file:
    file.write("Hello, World!")

# Write multiple lines
lines = ["Line 1", "Line 2", "Line 3"]
with open("output.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")

# Write with writelines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

### Appending to Files
```python
# Append content to existing file
with open("log.txt", "a") as file:
    file.write("New log entry\n")

# Append with timestamp
import datetime
with open("log.txt", "a") as file:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"[{timestamp}] User logged in\n")
```

## File Object Methods

### File Position
```python
with open("example.txt", "r") as file:
    # Get current position
    position = file.tell()
    print(f"Current position: {position}")
    
    # Read some content
    content = file.read(10)
    print(f"Read: {content}")
    
    # Get new position
    position = file.tell()
    print(f"New position: {position}")
    
    # Seek to beginning
    file.seek(0)
    print(f"After seek(0): {file.tell()}")
    
    # Seek to specific position
    file.seek(5)
    print(f"After seek(5): {file.tell()}")
```

### File Information
```python
import os

# Check if file exists
if os.path.exists("example.txt"):
    print("File exists")
    
    # Get file size
    size = os.path.getsize("example.txt")
    print(f"File size: {size} bytes")
    
    # Get file modification time
    mtime = os.path.getmtime("example.txt")
    print(f"Modified: {mtime}")
```

## Working with Different File Types

### CSV Files
```python
import csv

# Reading CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Reading CSV with headers
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['name']}, Age: {row['age']}")

# Writing CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "London"]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

### JSON Files
```python
import json

# Reading JSON
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)

# Writing JSON
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "swimming"]
}

with open("output.json", "w") as file:
    json.dump(data, file, indent=2)
```

### Binary Files
```python
# Reading binary file
with open("image.jpg", "rb") as file:
    binary_data = file.read()
    print(f"File size: {len(binary_data)} bytes")

# Writing binary data
data = b'\x00\x01\x02\x03\x04'
with open("binary.bin", "wb") as file:
    file.write(data)
```

## File and Directory Operations

### Directory Operations
```python
import os

# List directory contents
files = os.listdir(".")
print(f"Files in current directory: {files}")

# Create directory
os.makedirs("new_folder", exist_ok=True)

# Check if path is file or directory
if os.path.isfile("example.txt"):
    print("It's a file")
elif os.path.isdir("new_folder"):
    print("It's a directory")

# Get absolute path
abs_path = os.path.abspath("example.txt")
print(f"Absolute path: {abs_path}")
```

### File Operations
```python
import shutil

# Copy file
shutil.copy("source.txt", "destination.txt")

# Move file
shutil.move("old_name.txt", "new_name.txt")

# Remove file
os.remove("file_to_delete.txt")

# Remove directory
shutil.rmtree("directory_to_delete")
```

## Error Handling

### File Not Found
```python
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f"Error: {e}")
```

### Safe File Operations
```python
def safe_read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error reading file: {e}"

def safe_write_file(filename, content):
    try:
        with open(filename, "w") as file:
            file.write(content)
        return f"Successfully wrote to '{filename}'"
    except Exception as e:
        return f"Error writing file: {e}"
```

## Working with Large Files

### Memory Efficient Reading
```python
# Read large file in chunks
def read_large_file(filename, chunk_size=1024):
    with open(filename, "r") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Process large file
for chunk in read_large_file("large_file.txt"):
    # Process chunk
    print(f"Processing chunk of size: {len(chunk)}")
```

### Line by Line Processing
```python
def process_large_file(filename):
    with open(filename, "r") as file:
        for line_number, line in enumerate(file, 1):
            # Process each line
            processed_line = line.strip().upper()
            print(f"Line {line_number}: {processed_line}")
```

## File Compression

### Working with ZIP Files
```python
import zipfile

# Create ZIP file
with zipfile.ZipFile("archive.zip", "w") as zip_file:
    zip_file.write("file1.txt")
    zip_file.write("file2.txt")

# Extract ZIP file
with zipfile.ZipFile("archive.zip", "r") as zip_file:
    zip_file.extractall("extracted_folder")

# List ZIP contents
with zipfile.ZipFile("archive.zip", "r") as zip_file:
    print(zip_file.namelist())
```

## Logging to Files

### Basic Logging
```python
import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Log messages
logging.info("Application started")
logging.warning("Warning message")
logging.error("Error message")
```

### Advanced Logging
```python
import logging
from logging.handlers import RotatingFileHandler

# Create logger
logger = logging.getLogger("my_app")
logger.setLevel(logging.INFO)

# Create rotating file handler
handler = RotatingFileHandler(
    "app.log",
    maxBytes=1024*1024,  # 1MB
    backupCount=5
)

# Create formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(handler)

# Log messages
logger.info("Application started")
logger.warning("Warning message")
logger.error("Error message")
```

## Best Practices

### Always Use Context Managers
```python
# Good
with open("file.txt", "r") as file:
    content = file.read()

# Bad
file = open("file.txt", "r")
content = file.read()
file.close()  # Might be forgotten
```

### Specify Encoding
```python
# Good - explicit encoding
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Bad - relies on system default
with open("file.txt", "r") as file:
    content = file.read()
```

### Handle Exceptions
```python
def read_file_safely(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Permission denied for '{filename}'")
        return None
    except Exception as e:
        print(f"Error reading '{filename}': {e}")
        return None
```

### Use Path Objects
```python
from pathlib import Path

# Create Path object
file_path = Path("folder/subfolder/file.txt")

# Check if exists
if file_path.exists():
    print("File exists")

# Read file
content = file_path.read_text()

# Write file
file_path.write_text("New content")

# Create parent directories
file_path.parent.mkdir(parents=True, exist_ok=True)
```

## Common File Patterns

### Configuration Files
```python
import configparser

# Read INI file
config = configparser.ConfigParser()
config.read("config.ini")

# Get values
database_url = config.get("database", "url")
debug_mode = config.getboolean("app", "debug")

# Write INI file
config["database"] = {
    "url": "sqlite:///app.db",
    "pool_size": "10"
}

with open("config.ini", "w") as configfile:
    config.write(configfile)
```

### Temporary Files
```python
import tempfile

# Create temporary file
with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
    temp_file.write("Temporary content")
    temp_filename = temp_file.name

# Use temporary file
with open(temp_filename, "r") as file:
    content = file.read()

# Clean up
import os
os.unlink(temp_filename)
```

## Practice Examples
See `practice.py` for hands-on exercises with file handling! 