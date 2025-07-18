# Tuple Methods

print("=== TUPLE METHODS ===\n")

# 3. Tuple Methods
print("3. Tuple Methods:")
fruits = ("apple", "banana", "orange", "apple", "grape")
print(f"Fruits: {fruits}")

print(f"Count of 'apple': {fruits.count('apple')}")
print(f"Index of 'banana': {fruits.index('banana')}")
print(f"'orange' in fruits: {'orange' in fruits}")
print(f"'kiwi' in fruits: {'kiwi' in fruits}")
print()

# Additional method examples
print("More method examples:")
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"Numbers: {numbers}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of first 2: {numbers.index(2)}")

# Membership testing
print(f"\nMembership testing:")
print(f"1 in numbers: {1 in numbers}")
print(f"6 in numbers: {6 in numbers}")
print(f"2 not in numbers: {2 not in numbers}")

# Length and iteration
print(f"\nLength and iteration:")
print(f"Length: {len(numbers)}")
print("Iterating through tuple:")
for item in numbers:
    print(f"  {item}")

print("\n=== END ===")
