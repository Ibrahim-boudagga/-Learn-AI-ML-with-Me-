# Error Handling and Large Files

print("=== ERROR HANDLING AND LARGE FILES ===\n")

print("1. Basic Error Handling:")


def safe_read_file(filename):
    """Safely read a file with comprehensive error handling."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: Permission denied for '{filename}'"
    except UnicodeDecodeError as e:
        return f"Error: Unicode decode error in '{filename}': {e}"
    except Exception as e:
        return f"Error reading '{filename}': {e}"


def safe_write_file(filename, content):
    """Safely write to a file with comprehensive error handling."""
    try:
        with open(filename, "w") as file:
            file.write(content)
        return f"Successfully wrote to '{filename}'"
    except PermissionError:
        return f"Error: Permission denied for '{filename}'"
    except UnicodeEncodeError as e:
        return f"Error: Unicode encode error in '{filename}': {e}"
    except OSError as e:
        return f"Error: OS error writing to '{filename}': {e}"
    except Exception as e:
        return f"Error writing to '{filename}': {e}"


# Test safe file operations
print("Testing safe file operations:")
print(safe_read_file("sample.txt"))
print(safe_read_file("nonexistent.txt"))
print(safe_write_file("new_file.txt", "New content"))

print("\n2. Working with Large Files:")

# Create a large file for demonstration
large_content = "This is line {}\n" * 1000
with open("large_file.txt", "w") as file:
    file.write(large_content.format(*range(1, 1001)))

print("Created large_file.txt with 1000 lines")

print("\n3. Reading Large Files in Chunks:")


def read_large_file(filename, chunk_size=1024):
    """Read a large file in chunks to avoid memory issues."""
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

print("\n4. Line by Line Processing:")


def process_large_file(filename):
    """Process a large file line by line."""
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

print("\n5. Memory-Efficient File Processing:")


def count_lines_memory_efficient(filename):
    """Count lines in a file without loading entire file into memory."""
    try:
        with open(filename, "r") as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error counting lines: {e}"


def find_longest_line_memory_efficient(filename):
    """Find the longest line without loading entire file into memory."""
    try:
        with open(filename, "r") as file:
            longest_line = ""
            longest_length = 0
            longest_line_number = 0

            for line_number, line in enumerate(file, 1):
                line = line.strip()
                if len(line) > longest_length:
                    longest_line = line
                    longest_length = len(line)
                    longest_line_number = line_number

            return longest_line, longest_length, longest_line_number
    except FileNotFoundError:
        return f"Error: File '{filename}' not found", 0, 0
    except Exception as e:
        return f"Error finding longest line: {e}", 0, 0


# Test memory-efficient functions
line_count = count_lines_memory_efficient("large_file.txt")
print(f"Line count: {line_count}")

longest_line, length, line_num = find_longest_line_memory_efficient("large_file.txt")
print(f"Longest line ({length} chars) at line {line_num}: '{longest_line[:50]}...'")

print("\n6. File Processing with Progress Tracking:")

import os


def process_file_with_progress(filename, chunk_size=1024):
    """Process file with progress tracking."""
    try:
        # Get file size
        file_size = os.path.getsize(filename)
        processed = 0

        with open(filename, "r") as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break

                processed += len(chunk)
                progress = (processed / file_size) * 100
                print(f"\rProgress: {progress:.1f}%", end="")

                # Process chunk here
                # yield chunk  # Uncomment to yield chunks

        print(f"\nCompleted processing {filename}")
        return True
    except Exception as e:
        print(f"\nError processing {filename}: {e}")
        return False


# Test progress tracking
process_file_with_progress("large_file.txt")

print("\n7. File Processing with Error Recovery:")


def robust_file_processor(filename, process_func):
    """Process file with error recovery."""
    try:
        with open(filename, "r") as file:
            line_number = 0
            errors = []

            for line in file:
                line_number += 1
                try:
                    result = process_func(line.strip(), line_number)
                    # Process result here
                except Exception as e:
                    errors.append(f"Line {line_number}: {e}")
                    continue

            if errors:
                print(f"Encountered {len(errors)} errors:")
                for error in errors[:5]:  # Show first 5 errors
                    print(f"  {error}")
                if len(errors) > 5:
                    print(f"  ... and {len(errors) - 5} more errors")

            return True
    except FileNotFoundError:
        print(f"File {filename} not found")
        return False
    except Exception as e:
        print(f"Error processing file: {e}")
        return False


# Example processing function
def example_process_func(line, line_number):
    """Example function that might raise errors."""
    if line_number % 100 == 0:
        raise ValueError(f"Simulated error at line {line_number}")
    return line.upper()


# Test robust processing
print("Testing robust file processing:")
robust_file_processor("large_file.txt", example_process_func)

print("\n8. File Processing with Timeout:")

import signal
import time


class TimeoutError(Exception):
    pass


def timeout_handler(signum, frame):
    raise TimeoutError("Operation timed out")


def process_file_with_timeout(filename, timeout_seconds=5):
    """Process file with timeout protection."""
    start_time = None
    try:
        # Set up timeout handler
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(timeout_seconds)

        start_time = time.time()
        line_count = 0

        with open(filename, "r") as file:
            for line in file:
                line_count += 1
                # Simulate some processing
                time.sleep(0.001)

                # Check if we're taking too long
                if start_time and time.time() - start_time > timeout_seconds:
                    print("Processing taking too long, stopping...")
                    break

        signal.alarm(0)  # Cancel alarm
        return line_count
    except TimeoutError:
        print("File processing timed out")
        return -1
    except Exception as e:
        print(f"Error processing file: {e}")
        return -1


# Test timeout processing
print("Testing file processing with timeout:")
result = process_file_with_timeout("large_file.txt", timeout_seconds=2)
print(f"Processed {result} lines before timeout")

print("\n9. File Processing with Resource Management:")

import psutil
import gc


def monitor_memory_usage():
    """Monitor current memory usage."""
    process = psutil.Process()
    memory_info = process.memory_info()
    return memory_info.rss / 1024 / 1024  # Convert to MB


def process_file_with_memory_monitoring(filename):
    """Process file while monitoring memory usage."""
    initial_memory = monitor_memory_usage()
    print(f"Initial memory usage: {initial_memory:.2f} MB")

    try:
        with open(filename, "r") as file:
            line_count = 0
            for line in file:
                line_count += 1

                # Check memory every 100 lines
                if line_count % 100 == 0:
                    current_memory = monitor_memory_usage()
                    print(f"Line {line_count}, Memory: {current_memory:.2f} MB")

                    # Force garbage collection if memory usage is high
                    if current_memory > initial_memory * 2:
                        gc.collect()
                        print("Garbage collection performed")

        final_memory = monitor_memory_usage()
        print(f"Final memory usage: {final_memory:.2f} MB")
        return line_count
    except Exception as e:
        print(f"Error processing file: {e}")
        return -1


# Test memory monitoring
print("Testing file processing with memory monitoring:")
result = process_file_with_memory_monitoring("large_file.txt")
print(f"Processed {result} lines")

print("\n10. File Processing with Parallel Processing:")

import concurrent.futures
import threading


def process_chunk(chunk_data):
    """Process a chunk of data."""
    lines = chunk_data.split("\n")
    return len(lines), sum(len(line) for line in lines)


def process_file_parallel(filename, num_workers=4):
    """Process file using parallel processing."""
    try:
        # Read file in chunks
        chunk_size = 1024 * 1024  # 1MB chunks
        chunks = []

        with open(filename, "r") as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                chunks.append(chunk)

        # Process chunks in parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = [executor.submit(process_chunk, chunk) for chunk in chunks]

            total_lines = 0
            total_chars = 0

            for future in concurrent.futures.as_completed(futures):
                lines, chars = future.result()
                total_lines += lines
                total_chars += chars

        return total_lines, total_chars
    except Exception as e:
        print(f"Error in parallel processing: {e}")
        return -1, -1


# Test parallel processing
print("Testing parallel file processing:")
lines, chars = process_file_parallel("large_file.txt")
print(f"Parallel processing results: {lines} lines, {chars} characters")

print("\n11. File Processing with Caching:")

import hashlib


class FileProcessor:
    def __init__(self):
        self.cache = {}

    def get_file_hash(self, filename):
        """Get hash of file for caching."""
        try:
            with open(filename, "rb") as file:
                content = file.read()
                return hashlib.md5(content).hexdigest()
        except Exception:
            return None

    def process_file_cached(self, filename, process_func):
        """Process file with caching."""
        file_hash = self.get_file_hash(filename)

        if file_hash and file_hash in self.cache:
            print(f"Using cached result for {filename}")
            return self.cache[file_hash]

        print(f"Processing {filename} (not cached)")
        try:
            result = process_func(filename)
            if file_hash:
                self.cache[file_hash] = result
            return result
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            return None


# Test caching
processor = FileProcessor()


def count_words(filename):
    """Count words in file."""
    try:
        with open(filename, "r") as file:
            content = file.read()
            return len(content.split())
    except Exception as e:
        print(f"Error counting words: {e}")
        return 0


# Test cached processing
print("Testing cached file processing:")
result1 = processor.process_file_cached("large_file.txt", count_words)
result2 = processor.process_file_cached(
    "large_file.txt", count_words
)  # Should use cache
print(f"Word count: {result1}")

print("\n=== END OF ERROR HANDLING AND LARGE FILES ===")
