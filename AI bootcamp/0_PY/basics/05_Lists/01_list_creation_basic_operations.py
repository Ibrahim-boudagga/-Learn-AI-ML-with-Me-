# List Creation and Basic Operations

print("=== LIST CREATION AND BASIC OPERATIONS ===\n")

# List Creation
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", 3.14, True]

print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")

# Basic Operations
print(f"\nLength of numbers: {len(numbers)}")
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")

# Accessing elements
print(f"\nSecond element: {numbers[1]}")
print(f"Third from last: {numbers[-3]}")

# Checking if element exists
print(f"\nIs 3 in numbers? {3 in numbers}")
print(f"Is 'apple' in fruits? {'apple' in fruits}")

print("\n=== END ===")
