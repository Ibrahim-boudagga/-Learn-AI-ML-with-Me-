# List Methods - Finding Elements

print("=== LIST METHODS - FINDING ELEMENTS ===\n")

# Sample list with duplicates
fruits = ["apple", "banana", "orange", "apple", "grape"]
print(f"Fruits: {fruits}")

# index() - finds first occurrence of value
print(f"Index of 'apple': {fruits.index('apple')}")
print(f"Index of 'banana': {fruits.index('banana')}")

# count() - counts occurrences of value
print(f"Count of 'apple': {fruits.count('apple')}")
print(f"Count of 'grape': {fruits.count('grape')}")
print(f"Count of 'kiwi': {fruits.count('kiwi')}")

# in operator - checks if element exists
print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'kiwi' in fruits: {'kiwi' in fruits}")

# not in operator
print(f"'kiwi' not in fruits: {'kiwi' not in fruits}")


# Finding all occurrences
def find_all_occurrences(lst, value):
    return [i for i, x in enumerate(lst) if x == value]


apple_indices = find_all_occurrences(fruits, "apple")
print(f"All indices of 'apple': {apple_indices}")

# Finding with start and end parameters
numbers = [1, 2, 3, 2, 4, 2, 5]
print(f"\nNumbers: {numbers}")
print(f"Index of 2 from start: {numbers.index(2)}")
print(f"Index of 2 from index 2: {numbers.index(2, 2)}")
print(f"Index of 2 from index 2 to 5: {numbers.index(2, 2, 5)}")

print("\n=== END ===")
