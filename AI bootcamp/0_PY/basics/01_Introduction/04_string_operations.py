# String Operations

print("=== STRING OPERATIONS ===\n")

first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

greeting = f"Hello, {full_name}!"
print(f"Greeting: {greeting}")

print(f"Upper case: {full_name.upper()}")
print(f"Lower case: {full_name.lower()}")
print(f"Title case: {full_name.title()}")
print(f"Length: {len(full_name)}")
print()

# String concatenation with +
# f-strings for formatting
# String methods: upper(), lower(), title()
# len() to get string length
