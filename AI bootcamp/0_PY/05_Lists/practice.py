# Python Lists Practice

print("=== PYTHON LISTS PRACTICE ===\n")

# 1. List Creation and Basic Operations
print("1. List Creation and Basic Operations:")
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", 3.14, True]

print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")
print(f"Length of numbers: {len(numbers)}")
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
print()

# 2. List Slicing
print("2. List Slicing:")
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"Original list: {data}")
print(f"First 3 elements: {data[:3]}")
print(f"Last 3 elements: {data[-3:]}")
print(f"Middle elements (3-7): {data[3:7]}")
print(f"Every second element: {data[::2]}")
print(f"Reverse: {data[::-1]}")
print()

# 3. List Methods - Adding Elements
print("3. List Methods - Adding Elements:")
numbers = [1, 2, 3]
print(f"Original: {numbers}")

numbers.append(4)
print(f"After append(4): {numbers}")

numbers.insert(1, 2)
print(f"After insert(1, 2): {numbers}")

numbers.extend([5, 6])
print(f"After extend([5, 6]): {numbers}")

numbers += [7, 8]
print(f"After += [7, 8]: {numbers}")
print()

# 4. List Methods - Removing Elements
print("4. List Methods - Removing Elements:")
numbers = [1, 2, 3, 2, 4, 2, 5]
print(f"Original: {numbers}")

numbers.remove(2)
print(f"After remove(2): {numbers}")

popped = numbers.pop(1)
print(f"After pop(1): {numbers}, popped: {popped}")

del numbers[0]
print(f"After del numbers[0]: {numbers}")

numbers.clear()
print(f"After clear(): {numbers}")
print()

# 5. List Methods - Finding Elements
print("5. List Methods - Finding Elements:")
fruits = ["apple", "banana", "orange", "apple", "grape"]
print(f"Fruits: {fruits}")

print(f"Index of 'apple': {fruits.index('apple')}")
print(f"Count of 'apple': {fruits.count('apple')}")
print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'kiwi' in fruits: {'kiwi' in fruits}")
print()

# 6. List Methods - Sorting and Reversing
print("6. List Methods - Sorting and Reversing:")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")

numbers.sort()
print(f"After sort(): {numbers}")

numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

numbers.reverse()
print(f"After reverse(): {numbers}")

# Using sorted() function
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(f"Original: {original}")
print(f"Sorted (new list): {sorted_list}")
print()

# 7. List Comprehension
print("7. List Comprehension:")
# Basic comprehension
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested comprehension
matrix = [[i + j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# Dictionary comprehension
word_lengths = {word: len(word) for word in ["apple", "banana", "orange"]}
print(f"Word lengths: {word_lengths}")
print()

# 8. Built-in Functions with Lists
print("8. Built-in Functions with Lists:")
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Any non-zero: {any(numbers)}")
print(f"All non-zero: {all(numbers)}")

# enumerate()
print("\nEnumerate:")
for index, value in enumerate(numbers):
    print(f"  Index {index}: {value}")

# zip()
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
print("\nZip:")
for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")
print()

# 9. List Operations
print("9. List Operations:")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"Combined: {combined}")

# Repetition
repeated = list1 * 3
print(f"Repeated: {repeated}")

# Comparison
print(f"list1 == list2: {list1 == list2}")
print(f"list1 < list2: {list1 < list2}")
print()

# 10. Practice Problems
print("10. Practice Problems:")


# Problem 1: Find the second largest number
def find_second_largest(numbers):
    if len(numbers) < 2:
        return None
    sorted_nums = sorted(numbers, reverse=True)
    return sorted_nums[1]


test_numbers = [10, 5, 8, 12, 3, 9]
second_largest = find_second_largest(test_numbers)
print(f"Second largest in {test_numbers}: {second_largest}")


# Problem 2: Remove duplicates while preserving order
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


duplicate_list = [1, 2, 2, 3, 4, 4, 5, 1]
unique_list = remove_duplicates(duplicate_list)
print(f"Original: {duplicate_list}")
print(f"Without duplicates: {unique_list}")


# Problem 3: Flatten a nested list
def flatten_list(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


nested_list = [1, [2, 3], [4, [5, 6]], 7]
flattened = flatten_list(nested_list)
print(f"Nested: {nested_list}")
print(f"Flattened: {flattened}")


# Problem 4: Find common elements between two lists
def find_common(list1, list2):
    return list(set(list1) & set(list2))


list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common = find_common(list_a, list_b)
print(f"List A: {list_a}")
print(f"List B: {list_b}")
print(f"Common elements: {common}")


# Problem 5: Rotate list by n positions
def rotate_list(lst, n):
    n = n % len(lst)  # Handle cases where n > len(lst)
    return lst[n:] + lst[:n]


original_list = [1, 2, 3, 4, 5]
rotated = rotate_list(original_list, 2)
print(f"Original: {original_list}")
print(f"Rotated by 2: {rotated}")


# Problem 6: Check if list is sorted
def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


sorted_test = [1, 2, 3, 4, 5]
unsorted_test = [1, 3, 2, 4, 5]
print(f"{sorted_test} is sorted: {is_sorted(sorted_test)}")
print(f"{unsorted_test} is sorted: {is_sorted(unsorted_test)}")


# Problem 7: Find missing number in sequence
def find_missing(numbers):
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum


sequence = [1, 2, 4, 5, 6]
missing = find_missing(sequence)
print(f"Sequence: {sequence}")
print(f"Missing number: {missing}")

print("\n=== END OF PRACTICE ===")
