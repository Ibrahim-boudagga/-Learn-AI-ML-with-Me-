# String Validation

print("=== STRING VALIDATION ===\n")

test_strings = ["Hello123", "Hello", "123", "   ", "Hello World", "hello"]

for s in test_strings:
    print(f"'{s}':")
    print(f"  isalpha(): {s.isalpha()}")
    print(f"  isdigit(): {s.isdigit()}")
    print(f"  isalnum(): {s.isalnum()}")
    print(f"  isspace(): {s.isspace()}")
    print(f"  startswith('Hello'): {s.startswith('Hello')}")
    print(f"  endswith('World'): {s.endswith('World')}")
    print()

# String validation methods:
# isalpha() : Check if all characters are alphabetic
# isdigit() : Check if all characters are digits
# isalnum() : Check if all characters are alphanumeric
# isspace() : Check if all characters are whitespace
# startswith() : Check if string starts with prefix
# endswith() : Check if string ends with suffix
