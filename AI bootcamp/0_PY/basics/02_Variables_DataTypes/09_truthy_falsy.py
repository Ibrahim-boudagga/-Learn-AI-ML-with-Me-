# Truthy and Falsy Values

print("=== TRUTHY AND FALSY VALUES ===\n")

test_values = [0, 1, -1, "", "hello", [], [1, 2], None, True, False]

for value in test_values:
    truthiness = bool(value)
    print(f"Value: {value} -> bool(): {truthiness}")

print()

# Falsy values: False, 0, "", [], (), {}, None
# Truthy values: Everything else
# bool() function converts any value to True or False
# Useful for conditional statements and validation
