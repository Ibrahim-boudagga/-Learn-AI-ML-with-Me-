# Practice Problems - Part 2

print("=== PRACTICE PROBLEMS - PART 2 ===\n")

print("Problem 13: File content deduplicator")


def remove_duplicate_lines(filename, output_filename):
    """Remove duplicate lines from a file."""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        # Remove duplicates while preserving order
        seen = set()
        unique_lines = []
        for line in lines:
            if line not in seen:
                seen.add(line)
                unique_lines.append(line)

        with open(output_filename, "w") as file:
            file.writelines(unique_lines)

        removed_count = len(lines) - len(unique_lines)
        return f"Removed {removed_count} duplicate lines, saved to '{output_filename}'"
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error: {e}"


# Create a file with duplicate lines for testing
with open("duplicate_test.txt", "w") as file:
    file.write("Line 1\nLine 2\nLine 1\nLine 3\nLine 2\nLine 4\n")

result = remove_duplicate_lines("duplicate_test.txt", "deduplicated.txt")
print(result)

print("\nProblem 14: File content sorter")


def sort_file_lines(filename, output_filename, reverse=False):
    """Sort lines in a file."""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        # Sort lines
        sorted_lines = sorted(lines, reverse=reverse)

        with open(output_filename, "w") as file:
            file.writelines(sorted_lines)

        return f"Sorted {len(lines)} lines, saved to '{output_filename}'"
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error: {e}"


result = sort_file_lines("sample.txt", "sorted_sample.txt")
print(result)

result = sort_file_lines("sample.txt", "reverse_sorted_sample.txt", reverse=True)
print(result)

print("\nProblem 15: File content filter")


def filter_file_lines(filename, output_filename, filter_func):
    """Filter lines in a file based on a function."""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        # Filter lines
        filtered_lines = [line for line in lines if filter_func(line.strip())]

        with open(output_filename, "w") as file:
            file.writelines(filtered_lines)

        return f"Filtered {len(lines)} lines to {len(filtered_lines)} lines, saved to '{output_filename}'"
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error: {e}"


# Filter functions
def contains_word(word):
    """Return a filter function that checks if line contains a word."""
    return lambda line: word in line


def line_length_greater_than(length):
    """Return a filter function that checks if line length is greater than specified."""
    return lambda line: len(line) > length


result = filter_file_lines("sample.txt", "filtered_sample.txt", contains_word("line"))
print(result)

result = filter_file_lines("sample.txt", "long_lines.txt", line_length_greater_than(10))
print(result)

print("\nProblem 16: File content splitter")


def split_file_by_size(filename, chunk_size, output_prefix):
    """Split a file into smaller files based on size."""
    try:
        with open(filename, "r") as file:
            content = file.read()

        # Split content into chunks
        chunks = [
            content[i : i + chunk_size] for i in range(0, len(content), chunk_size)
        ]

        # Write chunks to separate files
        for i, chunk in enumerate(chunks, 1):
            output_filename = f"{output_prefix}_{i:03d}.txt"
            with open(output_filename, "w") as file:
                file.write(chunk)

        return f"Split file into {len(chunks)} chunks"
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error: {e}"


result = split_file_by_size("sample.txt", 20, "chunk")
print(result)

print("\nProblem 17: File content merger with headers")


def merge_files_with_headers(
    filenames, output_filename, header_format="=== {filename} ==="
):
    """Merge multiple files with headers."""
    try:
        with open(output_filename, "w") as output_file:
            for filename in filenames:
                try:
                    with open(filename, "r") as input_file:
                        content = input_file.read()
                        header = header_format.format(filename=filename)
                        output_file.write(f"{header}\n")
                        output_file.write(content)
                        if not content.endswith("\n"):
                            output_file.write("\n")
                        output_file.write("\n")
                except FileNotFoundError:
                    header = header_format.format(filename=filename)
                    output_file.write(f"{header} (NOT FOUND)\n\n")

        return f"Successfully merged {len(filenames)} files to '{output_filename}'"
    except Exception as e:
        return f"Error: {e}"


result = merge_files_with_headers(
    ["sample.txt", "test.txt"], "merged_with_headers.txt", "--- {filename} ---"
)
print(result)

print("\nProblem 18: File content diff checker")


def compare_files(file1, file2):
    """Compare two files and show differences."""
    try:
        with open(file1, "r") as f1:
            content1 = f1.readlines()

        with open(file2, "r") as f2:
            content2 = f2.readlines()

        differences = []

        # Find differences
        for i, (line1, line2) in enumerate(zip(content1, content2), 1):
            if line1 != line2:
                differences.append(f"Line {i}: '{line1.strip()}' != '{line2.strip()}'")

        # Handle different file lengths
        if len(content1) != len(content2):
            differences.append(
                f"File lengths differ: {len(content1)} vs {len(content2)} lines"
            )

        if differences:
            return False, differences
        else:
            return True, "Files are identical"

    except FileNotFoundError as e:
        return False, [f"File not found: {e}"]
    except Exception as e:
        return False, [f"Error comparing files: {e}"]


# Create a slightly different file for comparison
with open("sample_modified.txt", "w") as file:
    file.write(
        "This is line 1\nThis is line 2\nThis is line 3\nThis is line 4\nThis is line 5\nModified line 6\n"
    )

is_identical, differences = compare_files("sample.txt", "sample_modified.txt")
if is_identical:
    print("Files are identical")
else:
    print("Files are different:")
    for diff in differences:
        print(f"  {diff}")

print("\nProblem 19: File content encryption (basic)")


def simple_encrypt_file(filename, output_filename, key):
    """Simple XOR encryption of file content."""
    try:
        with open(filename, "rb") as file:
            content = file.read()

        # XOR encryption
        encrypted_content = bytes(b ^ key for b in content)

        with open(output_filename, "wb") as file:
            file.write(encrypted_content)

        return f"Encrypted file saved to '{output_filename}'"
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error: {e}"


def simple_decrypt_file(filename, output_filename, key):
    """Simple XOR decryption of file content."""
    return simple_encrypt_file(filename, output_filename, key)  # XOR is symmetric


# Test encryption
result = simple_encrypt_file("sample.txt", "encrypted_sample.txt", 42)
print(result)

result = simple_decrypt_file("encrypted_sample.txt", "decrypted_sample.txt", 42)
print(result)

print("\nProblem 20: File content compression utility")

import os
import gzip


def compress_text_file(filename, output_filename):
    """Compress a text file using gzip."""
    try:
        with open(filename, "rb") as file_in:
            content = file_in.read()
            with gzip.open(output_filename, "wb") as file_out:
                file_out.write(content)  # type: ignore

        original_size = os.path.getsize(filename)
        compressed_size = os.path.getsize(output_filename)
        compression_ratio = compressed_size / original_size

        return f"Compressed file: {original_size} -> {compressed_size} bytes ({compression_ratio:.2%})"
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error: {e}"


def decompress_text_file(filename, output_filename):
    """Decompress a gzipped text file."""
    try:
        with gzip.open(filename, "rb") as file_in:
            content = file_in.read()
            with open(output_filename, "wb") as file_out:
                file_out.write(content)  # type: ignore

        return f"Decompressed file saved to '{output_filename}'"
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error: {e}"


result = compress_text_file("sample.txt", "sample.txt.gz")
print(result)

result = decompress_text_file("sample.txt.gz", "decompressed_sample.txt")
print(result)

print("\nProblem 21: File content validator with schema")


def validate_file_schema(filename, schema):
    """Validate file content against a schema."""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        errors = []

        for line_num, line in enumerate(lines, 1):
            line = line.strip()

            # Check required fields
            for field in schema.get("required_fields", []):
                if field not in line:
                    errors.append(f"Line {line_num}: Missing required field '{field}'")

            # Check line length
            min_length = schema.get("min_line_length", 0)
            if len(line) < min_length:
                errors.append(
                    f"Line {line_num}: Too short ({len(line)} chars, min {min_length})"
                )

            max_length = schema.get("max_line_length")
            if max_length and len(line) > max_length:
                errors.append(
                    f"Line {line_num}: Too long ({len(line)} chars, max {max_length})"
                )

            # Check for forbidden characters
            forbidden_chars = schema.get("forbidden_chars", [])
            for char in forbidden_chars:
                if char in line:
                    errors.append(
                        f"Line {line_num}: Contains forbidden character '{char}'"
                    )

        if errors:
            return False, errors
        else:
            return True, "File passes schema validation"

    except FileNotFoundError:
        return False, [f"File '{filename}' not found"]
    except Exception as e:
        return False, [f"Error validating schema: {e}"]


# Test schema validation
schema = {
    "required_fields": ["line"],
    "min_line_length": 5,
    "max_line_length": 50,
    "forbidden_chars": ["#", "$"],
}

is_valid, messages = validate_file_schema("sample.txt", schema)
if is_valid:
    print("File passes schema validation")
else:
    print("File fails schema validation:")
    for message in messages:
        print(f"  {message}")

print("\nProblem 22: File content statistics generator")


def generate_file_statistics(filename):
    """Generate comprehensive statistics for a file."""
    try:
        with open(filename, "r") as file:
            content = file.read()
            lines = content.split("\n")
            words = content.split()

        # Basic statistics
        stats = {
            "file_size": len(content),
            "line_count": len(lines),
            "word_count": len(words),
            "character_count": len(content),
            "character_count_no_spaces": len(
                content.replace(" ", "").replace("\n", "")
            ),
            "empty_lines": sum(1 for line in lines if not line.strip()),
            "average_line_length": len(content) / len(lines) if lines else 0,
            "average_word_length": (
                sum(len(word) for word in words) / len(words) if words else 0
            ),
        }

        # Word frequency
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        stats["unique_words"] = len(word_freq)
        stats["most_common_word"] = (
            max(word_freq.items(), key=lambda x: x[1]) if word_freq else None
        )

        # Character frequency
        char_freq = {}
        for char in content:
            if char.isalpha():
                char_freq[char] = char_freq.get(char, 0) + 1

        stats["unique_characters"] = len(char_freq)
        stats["most_common_character"] = (
            max(char_freq.items(), key=lambda x: x[1]) if char_freq else None
        )

        return stats

    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error: {e}"


stats = generate_file_statistics("sample.txt")
if isinstance(stats, dict):
    print("File statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
else:
    print(stats)

print("\n=== END OF PRACTICE PROBLEMS - PART 2 ===")
