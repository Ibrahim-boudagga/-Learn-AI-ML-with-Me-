# Truthy and Falsy Values

print("=== TRUTHY AND FALSY VALUES ===\n")

# 7. Truthy and Falsy Values
print("7. Truthy and Falsy Values:")
# Falsy values
falsy_values = [False, None, 0, "", [], {}, ()]

print("Falsy values:")
for value in falsy_values:
    if value:
        print(f"  {value} is truthy")
    else:
        print(f"  {value} is falsy")

# Truthy values
truthy_values = [True, 1, "hello", [1, 2], {"a": 1}]

print("\nTruthy values:")
for value in truthy_values:
    if value:
        print(f"  {value} is truthy")
    else:
        print(f"  {value} is falsy")
print()

# Additional truthy/falsy examples
print("More truthy/falsy examples:")

# Numeric values
print("Numeric values:")
print(f"  0: {bool(0)}")
print(f"  1: {bool(1)}")
print(f"  -1: {bool(-1)}")
print(f"  0.0: {bool(0.0)}")
print(f"  0.1: {bool(0.1)}")

# String values
print("\nString values:")
print(f"  '': {bool('')}")
print(f"  'hello': {bool('hello')}")
print(f"  '0': {bool('0')}")
print(f"  'False': {bool('False')}")

# Container types
print("\nContainer types:")
print(f"  []: {bool([])}")
print(f"  [1, 2]: {bool([1, 2])}")
print(f"  (): {bool(())}")
print(f"  (1,): {bool((1,))}")
print(f"  {{}}: {bool({})}")
print(f"  {{'a': 1}}: {bool({'a': 1})}")

# Special values
print("\nSpecial values:")
print(f"  None: {bool(None)}")
print(f"  True: {bool(True)}")
print(f"  False: {bool(False)}")

# Practical examples
print("\nPractical examples:")

# Checking if list is empty
my_list = []
if my_list:
    print("List has items")
else:
    print("List is empty")

# Checking if string is empty
name = ""
if name:
    print(f"Hello, {name}!")
else:
    print("Please enter your name")

# Checking if dictionary has keys
user_data = {}
if user_data:
    print("User data available")
else:
    print("No user data")

# Checking if number is non-zero
count = 0
if count:
    print(f"Found {count} items")
else:
    print("No items found")

print("\n=== END ===")
