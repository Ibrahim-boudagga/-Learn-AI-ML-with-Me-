# Python Sets Practice

print("=== PYTHON SETS PRACTICE ===\n")

# 1. Set Creation
print("1. Set Creation:")
# Empty set
empty_set = set()
print(f"Empty set: {empty_set}")

# Set with elements
fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}
print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")

# From list (removes duplicates)
numbers_from_list = set([1, 2, 2, 3, 3, 4])
print(f"From list (removes duplicates): {numbers_from_list}")

# From string (creates set of characters)
char_set = set("hello")
print(f"From string 'hello': {char_set}")

# Set comprehension
squares = {x**2 for x in range(5)}
print(f"Set comprehension (squares): {squares}")
print()

# 2. Set Properties
print("2. Set Properties:")
# Sets only contain unique elements
duplicate_set = {1, 2, 2, 3, 3, 4}
print(f"Duplicate set: {duplicate_set}")

# Sets are unordered
set1 = {3, 1, 4, 1, 5, 9, 2, 6}
print(f"Unordered set: {set1}")

# Sets can contain different types
mixed_set = {1, "hello", 3.14, True}
print(f"Mixed set: {mixed_set}")

# Sets cannot contain mutable elements
valid_set = {1, (2, 3), frozenset([4, 5])}
print(f"Valid set with immutable elements: {valid_set}")
print()

# 3. Set Operations
print("3. Set Operations:")
fruits = {"apple", "banana"}

# Adding elements
fruits.add("orange")
print(f"After add('orange'): {fruits}")

fruits.add("apple")  # No effect (already exists)
print(f"After add('apple') again: {fruits}")

# Adding multiple elements
fruits.update(["grape", "kiwi"])
print(f"After update(['grape', 'kiwi']): {fruits}")

# Removing elements
fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

fruits.discard("kiwi")
print(f"After discard('kiwi'): {fruits}")

popped = fruits.pop()
print(f"Popped element: {popped}")
print(f"After pop(): {fruits}")

fruits.clear()
print(f"After clear(): {fruits}")
print()

# 4. Set Membership
print("4. Set Membership:")
fruits = {"apple", "banana", "orange"}

print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
print(f"'apple' not in fruits: {'apple' not in fruits}")

print(f"Length: {len(fruits)}")
print(f"Boolean value: {bool(fruits)}")
print()

# 5. Mathematical Set Operations
print("5. Mathematical Set Operations:")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union = set1 | set2
print(f"Union: {union}")

# Intersection
intersection = set1 & set2
print(f"Intersection: {intersection}")

# Difference
difference = set1 - set2
print(f"Difference (set1 - set2): {difference}")

# Symmetric difference
symmetric_diff = set1 ^ set2
print(f"Symmetric difference: {symmetric_diff}")

# In-place operations
set1_copy = set1.copy()
set1_copy |= set2
print(f"In-place union: {set1_copy}")

set1_copy = set1.copy()
set1_copy &= set2
print(f"In-place intersection: {set1_copy}")
print()

# 6. Set Methods
print("6. Set Methods:")
fruits = {"apple", "banana", "orange", "grape"}

# Set comparison
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4}
set_c = {1, 2, 3}

print(f"set_a.issubset(set_b): {set_a.issubset(set_b)}")
print(f"set_b.issuperset(set_a): {set_b.issuperset(set_a)}")
print(f"set_a.isdisjoint({4, 5, 6}): {set_a.isdisjoint({4, 5, 6})}")

# Using operators
print(f"set_a <= set_b: {set_a <= set_b}")
print(f"set_b >= set_a: {set_b >= set_a}")
print()

# 7. Set Comprehension
print("7. Set Comprehension:")
# Basic comprehension
squares = {x**2 for x in range(5)}
print(f"Basic comprehension: {squares}")

# With condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"With condition: {even_squares}")

# From existing set
fruits = {"apple", "banana", "orange"}
upper_fruits = {fruit.upper() for fruit in fruits}
print(f"From existing set: {upper_fruits}")

# Complex comprehension
vowels = {"a", "e", "i", "o", "u"}
text = "hello world"
consonants = {char for char in text if char.isalpha() and char not in vowels}
print(f"Complex comprehension (consonants): {consonants}")
print()

# 8. Frozen Sets
print("8. Frozen Sets:")
# Frozen sets are immutable
frozen_fruits = frozenset(["apple", "banana", "orange"])
print(f"Frozen set: {frozen_fruits}")

# Frozen sets can be used as dictionary keys
set_dict = {frozen_fruits: "fruit set"}
print(f"Dictionary with frozen set key: {set_dict}")

# Frozen sets support set operations
set1 = frozenset([1, 2, 3])
set2 = frozenset([3, 4, 5])
union = set1 | set2
print(f"Frozen set union: {union}")
print(f"Type of result: {type(union)}")
print()

# 9. Built-in Functions with Sets
print("9. Built-in Functions with Sets:")
fruits = {"apple", "banana", "orange"}

print(f"Length: {len(fruits)}")
print(f"Maximum: {max(fruits)}")
print(f"Minimum: {min(fruits)}")
print(f"Any: {any(fruits)}")
print(f"All: {all(fruits)}")

# sorted() with sets
sorted_fruits = sorted(fruits)
print(f"Sorted fruits: {sorted_fruits}")
print()

# 10. Practice Problems
print("10. Practice Problems:")


# Problem 1: Remove duplicates from list
def remove_duplicates(lst):
    return list(set(lst))


test_list = [1, 2, 2, 3, 3, 4, 5, 5]
unique_list = remove_duplicates(test_list)
print(f"Original: {test_list}")
print(f"Without duplicates: {unique_list}")


# Problem 2: Find common elements between two lists
def find_common(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 & set2)


list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common = find_common(list_a, list_b)
print(f"List A: {list_a}")
print(f"List B: {list_b}")
print(f"Common elements: {common}")


# Problem 3: Check if two lists have any common elements
def has_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return not set1.isdisjoint(set2)


list_c = [1, 2, 3]
list_d = [4, 5, 6]
list_e = [3, 4, 5]

print(f"List C and D have common elements: {has_common_elements(list_c, list_d)}")
print(f"List C and E have common elements: {has_common_elements(list_c, list_e)}")


# Problem 4: Find unique elements in either list but not both
def unique_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 ^ set2)


unique = unique_elements(list_a, list_b)
print(f"Unique elements (not in both): {unique}")


# Problem 5: Check if string has all unique characters
def has_unique_chars(text):
    return len(text) == len(set(text))


test_strings = ["python", "hello", "algorithm", "unique"]
for text in test_strings:
    result = has_unique_chars(text)
    print(f"'{text}' has unique characters: {result}")


# Problem 6: Find missing number in sequence
def find_missing_number(numbers):
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum


def find_missing_using_sets(numbers):
    complete_set = set(range(1, len(numbers) + 2))
    numbers_set = set(numbers)
    missing = complete_set - numbers_set
    return missing.pop() if missing else None


sequence = [1, 2, 4, 5, 6]
missing1 = find_missing_number(sequence)
missing2 = find_missing_using_sets(sequence)
print(f"Sequence: {sequence}")
print(f"Missing number (sum method): {missing1}")
print(f"Missing number (set method): {missing2}")


# Problem 7: Find all subsets of a set
def find_subsets(s):
    if not s:
        return [set()]

    element = s.pop()
    subsets = find_subsets(s)
    new_subsets = []
    for subset in subsets:
        new_subsets.append(subset)
        new_subsets.append(subset | {element})

    return new_subsets


test_set = {1, 2, 3}
subsets = find_subsets(test_set.copy())
print(f"Subsets of {test_set}: {subsets}")


# Problem 8: Check if one set is subset of another
def is_subset(set1, set2):
    return set1.issubset(set2)


def is_proper_subset(set1, set2):
    return set1 < set2


set_x = {1, 2}
set_y = {1, 2, 3, 4}
set_z = {1, 2}

print(f"{set_x} is subset of {set_y}: {is_subset(set_x, set_y)}")
print(f"{set_x} is proper subset of {set_y}: {is_proper_subset(set_x, set_y)}")
print(f"{set_x} is proper subset of {set_z}: {is_proper_subset(set_x, set_z)}")


# Problem 9: Find symmetric difference of multiple sets
def symmetric_difference_multiple(*sets):
    if not sets:
        return set()

    result = sets[0]
    for s in sets[1:]:
        result = result ^ s

    return result


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {5, 6, 7, 8}

sym_diff = symmetric_difference_multiple(set1, set2, set3)
print(f"Symmetric difference of {set1}, {set2}, {set3}: {sym_diff}")


# Problem 10: Create a set-based cache
class SetCache:
    def __init__(self, max_size=100):
        self.cache = set()
        self.max_size = max_size

    def add(self, item):
        if len(self.cache) >= self.max_size:
            # Remove oldest item (simple implementation)
            self.cache.pop()
        self.cache.add(item)

    def contains(self, item):
        return item in self.cache

    def remove(self, item):
        self.cache.discard(item)

    def size(self):
        return len(self.cache)

    def clear(self):
        self.cache.clear()


# Test set cache
cache = SetCache(max_size=3)
cache.add("user1")
cache.add("user2")
cache.add("user3")
cache.add("user4")  # This will evict user1

print(f"Cache contains 'user1': {cache.contains('user1')}")
print(f"Cache contains 'user2': {cache.contains('user2')}")
print(f"Cache size: {cache.size()}")


# Problem 11: Find all unique combinations
def unique_combinations(items, r):
    from itertools import combinations

    return set(combinations(items, r))


test_items = [1, 2, 3, 4]
combinations = unique_combinations(test_items, 2)
print(f"Unique combinations of {test_items} (r=2): {combinations}")


# Problem 12: Set-based data validation
def validate_data(data, required_fields, optional_fields):
    data_fields = set(data.keys())
    required_set = set(required_fields)
    optional_set = set(optional_fields)

    # Check if all required fields are present
    missing_required = required_set - data_fields
    if missing_required:
        return False, f"Missing required fields: {missing_required}"

    # Check if all fields are valid
    valid_fields = required_set | optional_set
    invalid_fields = data_fields - valid_fields
    if invalid_fields:
        return False, f"Invalid fields: {invalid_fields}"

    return True, "Data is valid"


# Test data validation
required = ["name", "age"]
optional = ["email", "phone"]
valid_data = {"name": "Alice", "age": 25, "email": "alice@example.com"}
invalid_data = {"name": "Bob", "city": "New York"}  # Missing age, invalid city

valid_result = validate_data(valid_data, required, optional)
invalid_result = validate_data(invalid_data, required, optional)

print(f"Valid data result: {valid_result}")
print(f"Invalid data result: {invalid_result}")

print("\n=== END OF PRACTICE ===")
