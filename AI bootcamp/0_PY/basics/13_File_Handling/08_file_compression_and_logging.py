# File Compression and Logging

print("=== FILE COMPRESSION AND LOGGING ===\n")

print("1. File Compression with ZIP:")

import zipfile
import os
import time

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

print("\n2. Advanced ZIP Operations:")

# Create ZIP with compression
with zipfile.ZipFile(
    "compressed_archive.zip", "w", compression=zipfile.ZIP_DEFLATED
) as zip_file:
    zip_file.write("file1.txt", arcname="folder1/file1.txt")
    zip_file.write("file2.txt", arcname="folder2/file2.txt")

print("Created compressed_archive.zip with folder structure")

# Read ZIP file info
with zipfile.ZipFile("compressed_archive.zip", "r") as zip_file:
    for info in zip_file.infolist():
        print(f"File: {info.filename}")
        print(f"  Size: {info.file_size} bytes")
        print(f"  Compressed size: {info.compress_size} bytes")
        print(f"  Compression ratio: {info.compress_size/info.file_size:.2%}")

print("\n3. ZIP with Password Protection:")

# Create password-protected ZIP (simulated)
print("Creating password-protected ZIP (simulated):")
with zipfile.ZipFile("protected_archive.zip", "w") as zip_file:
    zip_file.write("file1.txt")
    print("Note: zipfile module doesn't support password protection directly")
    print("Use third-party libraries like pyminizip for password protection")

print("\n4. Logging to Files:")

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

print("\n5. Advanced Logging Configuration:")


# Create a more sophisticated logger
def setup_advanced_logger():
    """Set up advanced logging configuration."""
    # Create logger
    logger = logging.getLogger("advanced_app")
    logger.setLevel(logging.DEBUG)

    # Create file handler
    file_handler = logging.FileHandler("advanced_app.log")
    file_handler.setLevel(logging.DEBUG)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Use advanced logger
logger = setup_advanced_logger()
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")

print("\n6. Logging with Different Levels:")


# Create logger with different levels
def create_level_logger():
    """Create logger with different levels for different handlers."""
    logger = logging.getLogger("level_logger")
    logger.setLevel(logging.DEBUG)

    # Error handler (file)
    error_handler = logging.FileHandler("errors.log")
    error_handler.setLevel(logging.ERROR)
    error_formatter = logging.Formatter("%(asctime)s - ERROR - %(message)s")
    error_handler.setFormatter(error_formatter)

    # Info handler (file)
    info_handler = logging.FileHandler("info.log")
    info_handler.setLevel(logging.INFO)
    info_formatter = logging.Formatter("%(asctime)s - INFO - %(message)s")
    info_handler.setFormatter(info_formatter)

    # Debug handler (file)
    debug_handler = logging.FileHandler("debug.log")
    debug_handler.setLevel(logging.DEBUG)
    debug_formatter = logging.Formatter("%(asctime)s - DEBUG - %(message)s")
    debug_handler.setFormatter(debug_formatter)

    logger.addHandler(error_handler)
    logger.addHandler(info_handler)
    logger.addHandler(debug_handler)

    return logger


# Test level logger
level_logger = create_level_logger()
level_logger.debug("Debug message")
level_logger.info("Info message")
level_logger.warning("Warning message")
level_logger.error("Error message")

print("Created separate log files for different levels")

print("\n7. Logging with Rotation:")

import logging.handlers


def setup_rotating_logger():
    """Set up logger with rotating file handler."""
    logger = logging.getLogger("rotating_logger")
    logger.setLevel(logging.INFO)

    # Rotating file handler (5 files, 1KB each)
    rotating_handler = logging.handlers.RotatingFileHandler(
        "rotating_app.log", maxBytes=1024, backupCount=5
    )

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    rotating_handler.setFormatter(formatter)
    logger.addHandler(rotating_handler)

    return logger


# Test rotating logger
rotating_logger = setup_rotating_logger()
for i in range(50):
    rotating_logger.info(f"Log message {i}")

print("Created rotating log files")

print("\n8. Logging with Timed Rotation:")


def setup_timed_rotating_logger():
    """Set up logger with timed rotating file handler."""
    logger = logging.getLogger("timed_logger")
    logger.setLevel(logging.INFO)

    # Timed rotating file handler (daily rotation, 7 backup files)
    timed_handler = logging.handlers.TimedRotatingFileHandler(
        "timed_app.log", when="midnight", interval=1, backupCount=7
    )

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    timed_handler.setFormatter(formatter)
    logger.addHandler(timed_handler)

    return logger


# Test timed logger
timed_logger = setup_timed_rotating_logger()
timed_logger.info("This will be in the current log file")

print("Created timed rotating logger")

print("\n9. Compression with GZIP:")

import gzip

# Compress a file with gzip
with open("file1.txt", "rb") as file_in:
    with gzip.open("file1.txt.gz", "wb") as file_out:
        file_out.write(file_in.read())

print("Created file1.txt.gz")

# Decompress gzip file
with gzip.open("file1.txt.gz", "rb") as file_in:
    with open("file1_decompressed.txt", "wb") as file_out:
        file_out.write(file_in.read())

print("Decompressed to file1_decompressed.txt")

print("\n10. Compression with BZIP2:")

import bz2

# Compress with bzip2
with open("file2.txt", "rb") as file_in:
    with bz2.open("file2.txt.bz2", "wb") as file_out:
        file_out.write(file_in.read())

print("Created file2.txt.bz2")

# Decompress bzip2 file
with bz2.open("file2.txt.bz2", "rb") as file_in:
    with open("file2_decompressed.txt", "wb") as file_out:
        file_out.write(file_in.read())

print("Decompressed to file2_decompressed.txt")

print("\n11. Compression Comparison:")

# Create a larger file for compression testing
large_content = "This is a test line with some content. " * 1000
with open("large_test.txt", "w") as file:
    file.write(large_content)

# Compress with different methods
original_size = os.path.getsize("large_test.txt")

# GZIP compression
with open("large_test.txt", "rb") as file_in:
    with gzip.open("large_test.txt.gz", "wb") as file_out:
        file_out.write(file_in.read())

# BZIP2 compression
with open("large_test.txt", "rb") as file_in:
    with bz2.open("large_test.txt.bz2", "wb") as file_out:
        file_out.write(file_in.read())

# ZIP compression
with zipfile.ZipFile(
    "large_test.zip", "w", compression=zipfile.ZIP_DEFLATED
) as zip_file:
    zip_file.write("large_test.txt")

# Compare sizes
gzip_size = os.path.getsize("large_test.txt.gz")
bzip2_size = os.path.getsize("large_test.txt.bz2")
zip_size = os.path.getsize("large_test.zip")

print("Compression comparison:")
print(f"Original size: {original_size} bytes")
print(f"GZIP size: {gzip_size} bytes ({gzip_size/original_size:.2%})")
print(f"BZIP2 size: {bzip2_size} bytes ({bzip2_size/original_size:.2%})")
print(f"ZIP size: {zip_size} bytes ({zip_size/original_size:.2%})")

print("\n12. Logging with Custom Formatters:")


class CustomFormatter(logging.Formatter):
    """Custom formatter with colors and additional info."""

    def format(self, record):
        # Add custom fields
        record.filename = os.path.basename(record.pathname)
        record.function = record.funcName

        # Format based on level
        if record.levelno >= logging.ERROR:
            color = "\033[91m"  # Red
        elif record.levelno >= logging.WARNING:
            color = "\033[93m"  # Yellow
        elif record.levelno >= logging.INFO:
            color = "\033[92m"  # Green
        else:
            color = "\033[94m"  # Blue

        reset = "\033[0m"

        # Create formatted message
        formatted = super().format(record)
        return f"{color}{formatted}{reset}"


def setup_custom_logger():
    """Set up logger with custom formatter."""
    logger = logging.getLogger("custom_logger")
    logger.setLevel(logging.DEBUG)

    # Console handler with custom formatter
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    custom_formatter = CustomFormatter(
        "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
    )
    console_handler.setFormatter(custom_formatter)

    logger.addHandler(console_handler)
    return logger


# Test custom logger
custom_logger = setup_custom_logger()
custom_logger.debug("Debug message")
custom_logger.info("Info message")
custom_logger.warning("Warning message")
custom_logger.error("Error message")

print("\n13. Logging with Context Managers:")


class LoggingContext:
    """Context manager for logging operations."""

    def __init__(self, logger, operation):
        self.logger = logger
        self.operation = operation
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        self.logger.info(f"Starting {self.operation}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.start_time is not None:
            duration = time.time() - self.start_time
            if exc_type:
                self.logger.error(f"Error in {self.operation}: {exc_val}")
            else:
                self.logger.info(f"Completed {self.operation} in {duration:.2f}s")
        else:
            if exc_type:
                self.logger.error(f"Error in {self.operation}: {exc_val}")
            else:
                self.logger.info(f"Completed {self.operation}")


# Test logging context
test_logger = logging.getLogger("context_logger")
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logging.StreamHandler())

with LoggingContext(test_logger, "file processing"):
    # Simulate some work
    time.sleep(0.1)
    print("Processing file...")

print("\n=== END OF FILE COMPRESSION AND LOGGING ===")
