# File Information and Directory Operations

print("=== FILE INFORMATION AND DIRECTORY OPERATIONS ===\n")

import os
import shutil
import stat
import time

print("1. File Information:")

# Create a test file
with open("test_info.txt", "w") as file:
    file.write("This is a test file for information gathering.")

# Check if file exists
if os.path.exists("test_info.txt"):
    print("test_info.txt exists")

    # Get file size
    size = os.path.getsize("test_info.txt")
    print(f"File size: {size} bytes")

    # Get file modification time
    mtime = os.path.getmtime("test_info.txt")
    print(f"Modified time: {mtime}")
    print(f"Modified time (formatted): {time.ctime(mtime)}")

    # Get file creation time (platform dependent)
    try:
        ctime = os.path.getctime("test_info.txt")
        print(f"Created time: {time.ctime(ctime)}")
    except AttributeError:
        print("Creation time not available on this platform")

    # Get absolute path
    abs_path = os.path.abspath("test_info.txt")
    print(f"Absolute path: {abs_path}")

    # Get relative path
    rel_path = os.path.relpath("test_info.txt")
    print(f"Relative path: {rel_path}")

    # Get directory name
    dir_name = os.path.dirname(abs_path)
    print(f"Directory: {dir_name}")

    # Get file name
    file_name = os.path.basename(abs_path)
    print(f"File name: {file_name}")

    # Split path
    path_parts = os.path.split(abs_path)
    print(f"Path parts: {path_parts}")

    # Split extension
    name, ext = os.path.splitext(file_name)
    print(f"Name: {name}, Extension: {ext}")

else:
    print("test_info.txt does not exist")

print("\n2. File Permissions and Attributes:")

# Get file permissions
if os.path.exists("test_info.txt"):
    # Get file mode
    mode = os.stat("test_info.txt").st_mode
    print(f"File mode: {oct(mode)}")

    # Check if file is readable
    if os.access("test_info.txt", os.R_OK):
        print("File is readable")

    # Check if file is writable
    if os.access("test_info.txt", os.W_OK):
        print("File is writable")

    # Check if file is executable
    if os.access("test_info.txt", os.X_OK):
        print("File is executable")
    else:
        print("File is not executable")

print("\n3. Directory Operations:")

# List current directory
current_files = os.listdir(".")
print(f"Files in current directory: {current_files}")

# Create a new directory
os.makedirs("test_folder", exist_ok=True)
print("Created test_folder")

# Check if it's a directory
if os.path.isdir("test_folder"):
    print("test_folder is a directory")

# Create nested directories
os.makedirs("test_folder/nested/deep", exist_ok=True)
print("Created nested directory structure")

# Create a file in the new directory
with open("test_folder/test_file.txt", "w") as file:
    file.write("Test content")

print("Created test_file.txt in test_folder")

# List contents of test_folder
folder_contents = os.listdir("test_folder")
print(f"Contents of test_folder: {folder_contents}")

print("\n4. Directory Information:")

# Get current working directory
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# Change directory
os.chdir("test_folder")
print(f"Changed to directory: {os.getcwd()}")

# List contents of current directory
current_contents = os.listdir(".")
print(f"Contents of current directory: {current_contents}")

# Go back to original directory
os.chdir("..")
print(f"Back to original directory: {os.getcwd()}")

print("\n5. File and Directory Walking:")

# Create some test files
os.makedirs("walk_test/dir1", exist_ok=True)
os.makedirs("walk_test/dir2", exist_ok=True)

with open("walk_test/file1.txt", "w") as file:
    file.write("File 1 content")

with open("walk_test/dir1/file2.txt", "w") as file:
    file.write("File 2 content")

with open("walk_test/dir2/file3.txt", "w") as file:
    file.write("File 3 content")

print("Walking through directory structure:")
for root, dirs, files in os.walk("walk_test"):
    print(f"Directory: {root}")
    print(f"  Subdirectories: {dirs}")
    print(f"  Files: {files}")

print("\n6. File Copying and Moving:")

# Copy a file
shutil.copy("test_info.txt", "test_info_copy.txt")
print("Copied test_info.txt to test_info_copy.txt")

# Copy with metadata
shutil.copy2("test_info.txt", "test_info_copy2.txt")
print("Copied test_info.txt with metadata")

# Copy directory
shutil.copytree("walk_test", "walk_test_copy")
print("Copied walk_test directory")

# Move a file
shutil.move("test_info_copy.txt", "test_folder/moved_file.txt")
print("Moved test_info_copy.txt to test_folder")

print("\n7. File and Directory Removal:")

# Remove a file
os.remove("test_info_copy2.txt")
print("Removed test_info_copy2.txt")

# Remove empty directory
os.rmdir("walk_test_copy/dir1")
print("Removed empty directory dir1")

# Remove directory tree
shutil.rmtree("walk_test_copy")
print("Removed walk_test_copy directory tree")

print("\n8. File Path Operations:")

# Join paths
path1 = "folder"
path2 = "subfolder"
path3 = "file.txt"
full_path = os.path.join(path1, path2, path3)
print(f"Joined path: {full_path}")

# Normalize path
normalized_path = os.path.normpath("folder/../folder/subfolder/./file.txt")
print(f"Normalized path: {normalized_path}")

# Expand user path
user_path = os.path.expanduser("~/test_file.txt")
print(f"User path: {user_path}")

# Expand environment variables
env_path = os.path.expandvars("$HOME/test_file.txt")
print(f"Environment path: {env_path}")

print("\n9. File Type Checking:")

# Check if path is file
if os.path.isfile("test_info.txt"):
    print("test_info.txt is a file")

# Check if path is directory
if os.path.isdir("test_folder"):
    print("test_folder is a directory")

# Check if path is link
if os.path.islink("test_info.txt"):
    print("test_info.txt is a symbolic link")
else:
    print("test_info.txt is not a symbolic link")

# Check if path is mount point
if os.path.ismount("/"):
    print("/ is a mount point")

print("\n10. File Size and Space:")

# Get file size
if os.path.exists("test_info.txt"):
    size = os.path.getsize("test_info.txt")
    print(f"File size: {size} bytes")
    print(f"File size: {size / 1024:.2f} KB")

# Get disk usage (platform dependent)
try:
    disk_usage = shutil.disk_usage(".")
    print(f"Disk usage: {disk_usage}")
    print(f"Total: {disk_usage.total / (1024**3):.2f} GB")
    print(f"Used: {disk_usage.used / (1024**3):.2f} GB")
    print(f"Free: {disk_usage.free / (1024**3):.2f} GB")
except AttributeError:
    print("Disk usage not available on this platform")

print("\n11. File Permissions Management:")

# Create a file for permission testing
with open("permission_test.txt", "w") as file:
    file.write("Permission test file")

# Get current permissions
current_mode = os.stat("permission_test.txt").st_mode
print(f"Current permissions: {oct(current_mode)}")

# Make file executable (Unix-like systems)
try:
    os.chmod("permission_test.txt", current_mode | stat.S_IXUSR)
    print("Made file executable")
except OSError:
    print("Could not change file permissions")

# Check if executable
if os.access("permission_test.txt", os.X_OK):
    print("File is now executable")

print("\n12. Temporary Files and Directories:")

import tempfile

# Create temporary file
with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
    temp_file.write("Temporary content")
    temp_filename = temp_file.name
    print(f"Created temporary file: {temp_filename}")

# Create temporary directory
temp_dir = tempfile.mkdtemp()
print(f"Created temporary directory: {temp_dir}")

# Clean up
os.unlink(temp_filename)
shutil.rmtree(temp_dir)
print("Cleaned up temporary files")

print("\n13. File Locking (Platform Dependent):")


# Simple file locking simulation
def create_locked_file(filename):
    """Create a file and simulate locking."""
    with open(filename, "w") as file:
        file.write("Locked content")
    print(f"Created and 'locked' {filename}")


def read_locked_file(filename):
    """Read a 'locked' file."""
    try:
        with open(filename, "r") as file:
            content = file.read()
        print(f"Read {filename}: {content}")
    except PermissionError:
        print(f"Permission denied for {filename}")


create_locked_file("locked_file.txt")
read_locked_file("locked_file.txt")

print("\n=== END OF FILE INFORMATION AND DIRECTORY OPERATIONS ===")
