# List Methods - Removing Elements

print("=== LIST METHODS - REMOVING ELEMENTS ===\n")

# Starting with a list containing duplicates
numbers = [1, 2, 3, 2, 4, 2, 5]
print(f"Original: {numbers}")

# remove() - removes first occurrence of value
numbers.remove(2)
print(f"After remove(2): {numbers}")

# pop() - removes and returns element at index
popped = numbers.pop(1)
print(f"After pop(1): {numbers}, popped: {popped}")

# del statement - removes element at index
del numbers[0]
print(f"After del numbers[0]: {numbers}")

# pop() without index - removes and returns last element
last_popped = numbers.pop()
print(f"After pop(): {numbers}, last popped: {last_popped}")

# clear() - removes all elements
numbers.clear()
print(f"After clear(): {numbers}")

# Demonstrating remove() with non-existent element
fruits = ["apple", "banana", "orange"]
print(f"\nFruits: {fruits}")

try:
    fruits.remove("kiwi")
except ValueError as e:
    print(f"Error removing 'kiwi': {e}")

print("\n=== END ===")
