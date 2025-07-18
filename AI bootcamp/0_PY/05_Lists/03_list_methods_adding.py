# List Methods - Adding Elements

print("=== LIST METHODS - ADDING ELEMENTS ===\n")

# Starting with a basic list
numbers = [1, 2, 3]
print(f"Original: {numbers}")

# append() - adds element to the end
numbers.append(4)
print(f"After append(4): {numbers}")

# insert() - adds element at specific position
numbers.insert(1, 2)
print(f"After insert(1, 2): {numbers}")

# extend() - adds multiple elements from iterable
numbers.extend([5, 6])
print(f"After extend([5, 6]): {numbers}")

# += operator - concatenates lists
numbers += [7, 8]
print(f"After += [7, 8]: {numbers}")

# insert() at different positions
numbers.insert(0, 0)  # Insert at beginning
print(f"After insert(0, 0): {numbers}")

numbers.insert(-1, 9)  # Insert before last element
print(f"After insert(-1, 9): {numbers}")

# extend() with different iterables
numbers.extend((10, 11))  # Tuple
print(f"After extend((10, 11)): {numbers}")

# String characters can't be added to a list of integers
# numbers.extend("abc")  # This would cause a type error
print(f"Current numbers: {numbers}")

print("\n=== END ===")
