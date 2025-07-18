# Practice Problems - Part 1

import json

print("=== PRACTICE PROBLEMS - PART 1 ===\n")

print("Problem 1: File word counter")


def count_words_in_file(filename):
    """Count words in a file."""
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error counting words: {e}"


word_count = count_words_in_file("sample.txt")
print(f"Word count in sample.txt: {word_count}")

print("\nProblem 2: File line counter")


def count_lines_in_file(filename):
    """Count lines in a file."""
    try:
        with open(filename, "r") as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error counting lines: {e}"


line_count = count_lines_in_file("sample.txt")
print(f"Line count in sample.txt: {line_count}")

print("\nProblem 3: Find longest word in file")


def find_longest_word(filename):
    """Find the longest word in a file."""
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            if not words:
                return "No words found"
            return max(words, key=len)
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error finding longest word: {e}"


longest_word = find_longest_word("sample.txt")
print(f"Longest word in sample.txt: '{longest_word}'")

print("\nProblem 4: Copy file with modifications")


def copy_file_with_modifications(source, destination, transform_func):
    """Copy a file with modifications applied."""
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


# Transform function to lowercase
def to_lowercase(content):
    return content.lower()


# Transform function to reverse lines
def reverse_lines(content):
    lines = content.split("\n")
    return "\n".join(lines[::-1])


result = copy_file_with_modifications(
    "sample.txt", "sample_uppercase.txt", to_uppercase
)
print(result)

result = copy_file_with_modifications(
    "sample.txt", "sample_lowercase.txt", to_lowercase
)
print(result)

result = copy_file_with_modifications(
    "sample.txt", "sample_reversed.txt", reverse_lines
)
print(result)

print("\nProblem 5: Merge multiple files")


def merge_files(filenames, output_filename):
    """Merge multiple files into one."""
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

print("\nProblem 6: Search and replace in file")


def search_and_replace(filename, search_text, replace_text):
    """Search and replace text in a file."""
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

print("\nProblem 7: Create a simple database file")


def create_database_file(filename: str):
    """Create a simple JSON database file."""
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

print("\nProblem 8: Read and parse database file")


def read_database_file(filename):
    """Read and parse a JSON database file."""
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
    except Exception as e:
        return f"Error: {e}"


result = read_database_file("database.json")
print(result)

print("\nProblem 9: Create a log analyzer")


def analyze_log_file(filename):
    """Analyze a log file and count log levels."""
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
    except Exception as e:
        return f"Error: {e}"


result = analyze_log_file("app.log")
print(result)

print("\nProblem 10: Create a file backup system")


def create_backup(filename):
    """Create a backup of a file with timestamp."""
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

print("\nProblem 11: File content validator")


def validate_file_content(filename, required_content=None, min_lines=0, max_lines=None):
    """Validate file content based on various criteria."""
    try:
        with open(filename, "r") as file:
            content = file.read()
            lines = content.split("\n")

        validation_results = []

        # Check if file is not empty
        if not content.strip():
            validation_results.append("File is empty")

        # Check line count
        if len(lines) < min_lines:
            validation_results.append(
                f"File has {len(lines)} lines, minimum required: {min_lines}"
            )

        if max_lines and len(lines) > max_lines:
            validation_results.append(
                f"File has {len(lines)} lines, maximum allowed: {max_lines}"
            )

        # Check for required content
        if required_content and required_content not in content:
            validation_results.append(
                f"Required content '{required_content}' not found"
            )

        if validation_results:
            return False, validation_results
        else:
            return True, "File content is valid"

    except FileNotFoundError:
        return False, [f"File '{filename}' not found"]
    except Exception as e:
        return False, [f"Error validating file: {e}"]


# Test file validation
is_valid, message = validate_file_content(
    "sample.txt", min_lines=3, required_content="line"
)
print(f"File validation: {message}")

print("\nProblem 12: File statistics calculator")


def calculate_file_stats(filename):
    """Calculate various statistics for a file."""
    try:
        with open(filename, "r") as file:
            content = file.read()
            lines = content.split("\n")
            words = content.split()
            characters = len(content)
            characters_no_spaces = len(content.replace(" ", "").replace("\n", ""))

        stats = {
            "lines": len(lines),
            "words": len(words),
            "characters": characters,
            "characters_no_spaces": characters_no_spaces,
            "average_line_length": characters / len(lines) if lines else 0,
            "average_word_length": (
                sum(len(word) for word in words) / len(words) if words else 0
            ),
        }

        return stats
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error: {e}"


stats = calculate_file_stats("sample.txt")
if isinstance(stats, dict):
    print("File statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
else:
    print(stats)

print("\n=== END OF PRACTICE PROBLEMS - PART 1 ===")
