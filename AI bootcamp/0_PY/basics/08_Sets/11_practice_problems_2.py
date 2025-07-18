# Practice Problems 2

print("=== PRACTICE PROBLEMS 2 ===\n")


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

print("\n=== END ===")
