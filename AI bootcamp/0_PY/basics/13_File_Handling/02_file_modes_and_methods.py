# File Modes and Methods

print("=== FILE MODES AND METHODS ===\n")

print("1. File Modes:")

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

print("\n2. Read and Write Mode (r+):")

# Read and write mode
with open("test.txt", "r+") as file:
    content = file.read()
    print(f"Original content: {content}")

    # Go back to beginning
    file.seek(0)
    file.write("Modified content\n")
    file.write(content)

print("Modified file using r+ mode")

# Read the modified file
with open("test.txt", "r") as file:
    modified_content = file.read()
    print(f"Modified content:\n{modified_content}")

print("\n3. Write and Read Mode (w+):")

# Write and read mode (truncates file)
with open("test.txt", "w+") as file:
    file.write("New content with w+ mode\n")
    file.write("Second line\n")

    # Go back to beginning to read
    file.seek(0)
    content = file.read()
    print(f"Content written and read: {content}")

print("\n4. Append and Read Mode (a+):")

# Append and read mode
with open("test.txt", "a+") as file:
    file.write("Appended with a+ mode\n")

    # Go back to beginning to read everything
    file.seek(0)
    content = file.read()
    print(f"All content with a+ mode:\n{content}")

print("\n5. File Object Methods:")

with open("sample.txt", "w") as file:
    file.write("This is a sample file for testing file methods.")

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

    # Seek to end
    file.seek(0, 2)  # 2 means from end
    print(f"Position at end: {file.tell()}")

print("\n6. File Seek Methods:")

with open("seek_test.txt", "w") as file:
    file.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

with open("seek_test.txt", "r") as file:
    print("Seek demonstration:")

    # Seek from beginning (default)
    file.seek(5)
    print(f"After seek(5): '{file.read(5)}'")

    # Seek from current position
    file.seek(3, 1)  # 1 means from current position
    print(f"After seek(3, 1): '{file.read(5)}'")

    # Seek from end
    file.seek(-5, 2)  # 2 means from end
    print(f"After seek(-5, 2): '{file.read()}'")

print("\n7. File Truncate Method:")

# Create a file for truncate testing
with open("truncate_test.txt", "w") as file:
    file.write("This is a long line that will be truncated.")

# Truncate to 10 characters
with open("truncate_test.txt", "r+") as file:
    file.truncate(10)
    content = file.read()
    print(f"After truncate(10): '{content}'")

# Truncate to current position
with open("truncate_test.txt", "r+") as file:
    file.seek(5)
    file.truncate()  # Truncate at current position
    content = file.read()
    print(f"After seek(5) and truncate(): '{content}'")

print("\n8. File Flush Method:")

# Demonstrate flush
with open("flush_test.txt", "w") as file:
    file.write("First line\n")
    file.flush()  # Force write to disk
    print("Flushed first line to disk")

    file.write("Second line\n")
    file.flush()
    print("Flushed second line to disk")

print("\n9. File Readline and Readlines:")

# Create a multi-line file
with open("multiline.txt", "w") as file:
    file.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5")

# Read line by line with readline
print("Reading with readline():")
with open("multiline.txt", "r") as file:
    line = file.readline()
    while line:
        print(f"  '{line.strip()}'")
        line = file.readline()

# Read all lines with readlines
print("\nReading with readlines():")
with open("multiline.txt", "r") as file:
    lines = file.readlines()
    for i, line in enumerate(lines, 1):
        print(f"  Line {i}: '{line.strip()}'")

print("\n10. File Write and Writelines:")

# Write single strings
with open("write_test.txt", "w") as file:
    file.write("First line\n")
    file.write("Second line\n")
    file.write("Third line\n")

# Write list of strings with writelines
lines_to_write = ["Line A\n", "Line B\n", "Line C\n", "Line D\n"]
with open("writelines_test.txt", "w") as file:
    file.writelines(lines_to_write)

print("Created write_test.txt and writelines_test.txt")

print("\n11. File Modes with Binary:")

# Binary write mode
binary_data = b"Hello, Binary World!\x00\x01\x02\x03"
with open("binary_test.bin", "wb") as file:
    file.write(binary_data)

# Binary read mode
with open("binary_test.bin", "rb") as file:
    read_data = file.read()
    print(f"Binary data: {read_data}")

# Binary append mode
with open("binary_test.bin", "ab") as file:
    file.write(b"Appended data")

# Binary read and write mode
with open("binary_test.bin", "rb+") as file:
    # Read first 5 bytes
    first_5 = file.read(5)
    print(f"First 5 bytes: {first_5}")

    # Write at position 10
    file.seek(10)
    file.write(b"INSERTED")

print("\n12. File Modes with Text and Binary Conversion:")

# Write text, read as binary
text_content = "Hello, Text World!"
with open("text_binary.txt", "w") as file:
    file.write(text_content)

# Read as binary
with open("text_binary.txt", "rb") as file:
    binary_content = file.read()
    print(f"Text as binary: {binary_content}")
    print(f"Decoded back to text: {binary_content.decode('utf-8')}")

# Write binary, read as text
binary_text = "Hello, Binary Text!".encode("utf-8")
with open("binary_text.txt", "wb") as file:
    file.write(binary_text)

# Read as text
with open("binary_text.txt", "r") as file:
    text_content = file.read()
    print(f"Binary as text: {text_content}")

print("\n13. File Modes with Different Encodings:")

# Write with specific encoding
with open("latin1.txt", "w", encoding="latin-1") as file:
    file.write("Hello, Latin-1 World!")

# Read with specific encoding
with open("latin1.txt", "r", encoding="latin-1") as file:
    content = file.read()
    print(f"Latin-1 content: {content}")

# Write with UTF-8
with open("utf8_test.txt", "w", encoding="utf-8") as file:
    file.write("Hello, UTF-8 World! 你好，世界！")

# Read with UTF-8
with open("utf8_test.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(f"UTF-8 content: {content}")

print("\n14. File Modes with Error Handling:")

# Handle encoding errors
try:
    with open("utf8_test.txt", "r", encoding="ascii") as file:
        content = file.read()
except UnicodeDecodeError as e:
    print(f"Encoding error: {e}")

# Handle encoding errors with error handler
with open("utf8_test.txt", "r", encoding="ascii", errors="ignore") as file:
    content = file.read()
    print(f"Content with ignored errors: {content}")

with open("utf8_test.txt", "r", encoding="ascii", errors="replace") as file:
    content = file.read()
    print(f"Content with replaced errors: {content}")

print("\n=== END OF FILE MODES AND METHODS ===")
