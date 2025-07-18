# Basic File Operations

print("=== BASIC FILE OPERATIONS ===\n")

print("1. Creating and Writing Files:")

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

# Write with encoding
with open("sample_utf8.txt", "w", encoding="utf-8") as file:
    file.write("Hello, 世界! 🌍")

print("Created sample_utf8.txt with UTF-8 encoding")

print("\n2. Reading Files:")

# Read the entire file
with open("sample.txt", "r") as file:
    content = file.read()
    print(f"File content:\n{content}")

# Read with encoding
with open("sample_utf8.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(f"UTF-8 file content: {content}")

print("\n3. Reading Line by Line:")

# Read line by line
print("Reading line by line:")
with open("sample.txt", "r") as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")

# Read with line numbers and strip whitespace
print("\nReading with line numbers:")
with open("sample.txt", "r") as file:
    for line_number, line in enumerate(file, 1):
        stripped_line = line.strip()
        if stripped_line:  # Skip empty lines
            print(f"Line {line_number}: '{stripped_line}'")

print("\n4. Reading All Lines as List:")

# Read all lines as list
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(f"All lines as list: {lines}")

# Process lines list
print("\nProcessing lines list:")
for i, line in enumerate(lines, 1):
    print(f"Line {i}: '{line.strip()}'")

print("\n5. File Reading Methods:")

# Read specific number of characters
with open("sample.txt", "r") as file:
    first_10 = file.read(10)
    print(f"First 10 characters: '{first_10}'")

    # Reset to beginning
    file.seek(0)

    # Read line by line
    first_line = file.readline()
    print(f"First line: '{first_line.strip()}'")

    # Read remaining lines
    remaining_lines = file.readlines()
    print(f"Remaining lines: {len(remaining_lines)}")

print("\n6. File Writing Methods:")

# Write single line
with open("single_line.txt", "w") as file:
    file.write("This is a single line")

# Write multiple lines
with open("multiple_lines.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")

# Write with writelines
lines_to_write = ["Line A\n", "Line B\n", "Line C\n"]
with open("writelines.txt", "w") as file:
    file.writelines(lines_to_write)

print("Created single_line.txt, multiple_lines.txt, and writelines.txt")

print("\n7. File Context Managers:")


# Demonstrate context manager benefits
def read_file_safely(filename):
    """Read file with proper error handling."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: Permission denied for '{filename}'"
    except Exception as e:
        return f"Error reading '{filename}': {e}"


def write_file_safely(filename, content):
    """Write file with proper error handling."""
    try:
        with open(filename, "w") as file:
            file.write(content)
        return f"Successfully wrote to '{filename}'"
    except PermissionError:
        return f"Error: Permission denied for '{filename}'"
    except Exception as e:
        return f"Error writing to '{filename}': {e}"


# Test safe file operations
print("Testing safe file operations:")
print(read_file_safely("sample.txt"))
print(read_file_safely("nonexistent.txt"))
print(write_file_safely("new_file.txt", "New content"))

print("\n8. File Operations with Different Encodings:")

# Create files with different encodings
text_content = "Hello, World! 你好，世界！ 🌍"

# UTF-8 encoding
with open("utf8_file.txt", "w", encoding="utf-8") as file:
    file.write(text_content)

# ASCII encoding (will fail for non-ASCII characters)
try:
    with open("ascii_file.txt", "w", encoding="ascii") as file:
        file.write(text_content)
except UnicodeEncodeError as e:
    print(f"ASCII encoding error: {e}")

# Read files with different encodings
with open("utf8_file.txt", "r", encoding="utf-8") as file:
    utf8_content = file.read()
    print(f"UTF-8 content: {utf8_content}")

print("\n9. File Operations with Binary Mode:")

# Write binary data
binary_data = b"Hello, Binary World!\x00\x01\x02\x03"

with open("binary_file.bin", "wb") as file:
    file.write(binary_data)

# Read binary data
with open("binary_file.bin", "rb") as file:
    read_binary = file.read()
    print(f"Binary data: {read_binary}")
    print(f"Data length: {len(read_binary)} bytes")
    print(f"As integers: {list(read_binary)}")

print("\n10. File Operations with Text and Binary:")

# Write text and read as binary
text_to_write = "Hello, Text World!"
with open("text_file.txt", "w") as file:
    file.write(text_to_write)

# Read as binary
with open("text_file.txt", "rb") as file:
    binary_content = file.read()
    print(f"Text as binary: {binary_content}")
    print(f"Decoded: {binary_content.decode('utf-8')}")

print("\n11. File Operations with Different Line Endings:")

# Write with different line endings
lines = ["Line 1", "Line 2", "Line 3"]

# Unix line endings
with open("unix_file.txt", "w", newline="\n") as file:
    file.write("\n".join(lines))

# Windows line endings
with open("windows_file.txt", "w", newline="\r\n") as file:
    file.write("\r\n".join(lines))

# Auto line endings (platform default)
with open("auto_file.txt", "w") as file:
    file.write("\n".join(lines))

print("Created files with different line endings")

print("\n12. File Operations with Buffering:")

# Write with different buffer sizes
large_content = "X" * 10000

# Unbuffered
with open("unbuffered.txt", "w", buffering=0) as file:
    file.write(large_content)

# Line buffered
with open("line_buffered.txt", "w", buffering=1) as file:
    for i in range(10):
        file.write(f"Line {i}\n")

# Custom buffer size
with open("custom_buffer.txt", "w", buffering=1024) as file:
    file.write(large_content)

print("Created files with different buffering options")

print("\n=== END OF BASIC FILE OPERATIONS ===")
