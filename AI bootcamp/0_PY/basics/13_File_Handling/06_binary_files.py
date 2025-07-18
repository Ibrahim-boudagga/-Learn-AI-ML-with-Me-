# Binary Files

print("=== BINARY FILES ===\n")

print("1. Basic Binary File Operations:")

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

print("\n2. Binary Data Types:")

# Different types of binary data
byte_data = b"Hello, Binary World!"
int_data = b"\x00\x01\x02\x03\x04\x05"
mixed_data = b"Text\x00\x01Numbers\x02\x03"

# Write different binary data
with open("byte_data.bin", "wb") as file:
    file.write(byte_data)

with open("int_data.bin", "wb") as file:
    file.write(int_data)

with open("mixed_data.bin", "wb") as file:
    file.write(mixed_data)

print("Created different binary files")

# Read and analyze
with open("byte_data.bin", "rb") as file:
    data = file.read()
    print(f"Byte data: {data}")
    print(f"Decoded: {data.decode('utf-8')}")

with open("int_data.bin", "rb") as file:
    data = file.read()
    print(f"Integer data: {list(data)}")

with open("mixed_data.bin", "rb") as file:
    data = file.read()
    print(f"Mixed data: {data}")

print("\n3. Binary File with Struct:")

import struct

# Pack data into binary format
# Format: 4-byte integer, 4-byte float, 8-byte string
packed_data = struct.pack("if8s", 42, 3.14159, b"Hello   ")

with open("struct_data.bin", "wb") as file:
    file.write(packed_data)

print("Created struct_data.bin")

# Unpack binary data
with open("struct_data.bin", "rb") as file:
    data = file.read()
    unpacked = struct.unpack("if8s", data)
    print(f"Unpacked data: {unpacked}")
    print(f"  Integer: {unpacked[0]}")
    print(f"  Float: {unpacked[1]}")
    print(f"  String: {unpacked[2].decode('utf-8').strip()}")

print("\n4. Binary File with Arrays:")

import array

# Create array of integers
int_array = array.array("i", [1, 2, 3, 4, 5])

with open("array_data.bin", "wb") as file:
    int_array.tofile(file)

print("Created array_data.bin")

# Read array from file
with open("array_data.bin", "rb") as file:
    loaded_array = array.array("i")
    loaded_array.fromfile(file, 5)  # Read 5 integers
    print(f"Loaded array: {list(loaded_array)}")

print("\n5. Binary File with Pickle:")

import pickle

# Create complex data structure
complex_data = {
    "numbers": [1, 2, 3, 4, 5],
    "text": "Hello, World!",
    "nested": {"a": 1, "b": 2},
}

# Serialize to binary
with open("pickle_data.bin", "wb") as file:
    pickle.dump(complex_data, file)

print("Created pickle_data.bin")

# Deserialize from binary
with open("pickle_data.bin", "rb") as file:
    loaded_data = pickle.load(file)
    print(f"Loaded pickle data: {loaded_data}")

print("\n6. Binary File with Images (Simulated):")

# Simulate image data (RGB pixels)
image_data = []
for y in range(10):
    for x in range(10):
        # Create a simple pattern
        r = (x * 25) % 256
        g = (y * 25) % 256
        b = ((x + y) * 10) % 256
        image_data.extend([r, g, b])

# Write as binary
with open("image_data.bin", "wb") as file:
    file.write(bytes(image_data))

print("Created image_data.bin (simulated image)")

# Read and analyze
with open("image_data.bin", "rb") as file:
    data = file.read()
    print(f"Image data length: {len(data)} bytes")
    print(f"Number of pixels: {len(data) // 3}")
    print(f"First few pixels: {list(data[:15])}")

print("\n7. Binary File with Compression:")

import gzip

# Create binary data
large_binary = b"X" * 10000

# Write uncompressed
with open("uncompressed.bin", "wb") as file:
    file.write(large_binary)

# Write compressed
with gzip.open("compressed.bin.gz", "wb") as file:
    file.write(large_binary)

print("Created uncompressed.bin and compressed.bin.gz")

# Compare sizes
import os

uncompressed_size = os.path.getsize("uncompressed.bin")
compressed_size = os.path.getsize("compressed.bin.gz")

print(f"Uncompressed size: {uncompressed_size} bytes")
print(f"Compressed size: {compressed_size} bytes")
print(f"Compression ratio: {compressed_size/uncompressed_size:.2%}")

print("\n8. Binary File with Encryption (Basic):")


# Simple XOR encryption (not secure, just for demonstration)
def xor_encrypt(data, key):
    """Simple XOR encryption."""
    return bytes(b ^ key for b in data)


def xor_decrypt(data, key):
    """Simple XOR decryption (same as encryption)."""
    return xor_encrypt(data, key)


# Encrypt binary data
key = 0x42
original_data = b"Secret binary data"
encrypted_data = xor_encrypt(original_data, key)

with open("encrypted.bin", "wb") as file:
    file.write(encrypted_data)

print("Created encrypted.bin")

# Decrypt data
with open("encrypted.bin", "rb") as file:
    encrypted = file.read()
    decrypted = xor_decrypt(encrypted, key)
    print(f"Original: {original_data}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

print("\n9. Binary File with Memory Mapping:")

import mmap

# Create a large binary file
large_data = b"Data block " * 1000

with open("mapped_data.bin", "wb") as file:
    file.write(large_data)

print("Created mapped_data.bin")

# Memory map the file
with open("mapped_data.bin", "rb") as file:
    with mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as mm:
        print(f"Mapped file size: {len(mm)} bytes")
        print(f"First 50 bytes: {mm[:50]}")

        # Search in mapped file
        position = mm.find(b"Data block")
        if position != -1:
            print(f"Found 'Data block' at position: {position}")

print("\n10. Binary File with Chunked Reading:")


def read_binary_in_chunks(filename, chunk_size=1024):
    """Read binary file in chunks."""
    with open(filename, "rb") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk


# Create large binary file
large_binary = b"Chunk " + b"data " * 100

with open("chunked_data.bin", "wb") as file:
    file.write(large_binary)

print("Created chunked_data.bin")

# Read in chunks
print("Reading in chunks:")
chunk_count = 0
total_bytes = 0
for chunk in read_binary_in_chunks("chunked_data.bin", chunk_size=20):
    chunk_count += 1
    total_bytes += len(chunk)
    print(f"  Chunk {chunk_count}: {len(chunk)} bytes")

print(f"Total chunks: {chunk_count}")
print(f"Total bytes: {total_bytes}")

print("\n11. Binary File with Endianness:")

import struct

# Data with different endianness
data = 0x12345678

# Little-endian
with open("little_endian.bin", "wb") as file:
    file.write(struct.pack("<I", data))  # Little-endian unsigned int

# Big-endian
with open("big_endian.bin", "wb") as file:
    file.write(struct.pack(">I", data))  # Big-endian unsigned int

print("Created little_endian.bin and big_endian.bin")

# Read and compare
with open("little_endian.bin", "rb") as file:
    little_data = struct.unpack("<I", file.read(4))[0]
    print(f"Little-endian: 0x{little_data:08X}")

with open("big_endian.bin", "rb") as file:
    big_data = struct.unpack(">I", file.read(4))[0]
    print(f"Big-endian: 0x{big_data:08X}")

print("\n12. Binary File with Error Handling:")


def safe_binary_read(filename):
    """Safely read binary file."""
    try:
        with open(filename, "rb") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except PermissionError:
        print(f"Permission denied for {filename}")
        return None
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None


def safe_binary_write(filename, data):
    """Safely write binary data."""
    try:
        with open(filename, "wb") as file:
            file.write(data)
        return True
    except Exception as e:
        print(f"Error writing {filename}: {e}")
        return False


# Test safe operations
test_data = b"Test binary data"
if safe_binary_write("test_safe.bin", test_data):
    print("Successfully wrote test_safe.bin")

loaded_data = safe_binary_read("test_safe.bin")
if loaded_data:
    print(f"Successfully read: {loaded_data}")

print("\n13. Binary File with Metadata:")

import json

# Create binary file with metadata
metadata = {"version": 1, "created": "2023-01-01", "description": "Test binary file"}

# Convert metadata to binary
metadata_bytes = json.dumps(metadata).encode("utf-8")
metadata_length = len(metadata_bytes)

# Create binary data
binary_content = b"Actual binary content here"

# Combine metadata and content
with open("metadata_binary.bin", "wb") as file:
    # Write metadata length (4 bytes)
    file.write(struct.pack("I", metadata_length))
    # Write metadata
    file.write(metadata_bytes)
    # Write binary content
    file.write(binary_content)

print("Created metadata_binary.bin")

# Read with metadata
with open("metadata_binary.bin", "rb") as file:
    # Read metadata length
    metadata_len = struct.unpack("I", file.read(4))[0]
    # Read metadata
    metadata_bytes = file.read(metadata_len)
    metadata = json.loads(metadata_bytes.decode("utf-8"))
    # Read content
    content = file.read()

    print(f"Metadata: {metadata}")
    print(f"Content length: {len(content)} bytes")

print("\n=== END OF BINARY FILES ===")
