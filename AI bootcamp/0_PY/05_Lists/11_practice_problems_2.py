# Practice Problems - Part 2

print("=== PRACTICE PROBLEMS - PART 2 ===\n")


# Problem 1: Flatten a nested list
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
print(f"Problem 1 - Nested: {nested_list}")
print(f"Flattened: {flattened}")


# Problem 2: Rotate list by n positions
def rotate_list(lst, n):
    n = n % len(lst)  # Handle cases where n > len(lst)
    return lst[n:] + lst[:n]


original_list = [1, 2, 3, 4, 5]
rotated = rotate_list(original_list, 2)
print(f"\nProblem 2 - Original: {original_list}")
print(f"Rotated by 2: {rotated}")


# Problem 3: Find missing number in sequence
def find_missing(numbers):
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum


sequence = [1, 2, 4, 5, 6]
missing = find_missing(sequence)
print(f"\nProblem 3 - Sequence: {sequence}")
print(f"Missing number: {missing}")


# Problem 4: Find the longest increasing subsequence
def longest_increasing_subsequence(lst):
    if not lst:
        return 0

    # Initialize LIS array
    lis = [1] * len(lst)

    # Compute LIS values
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[i] > lst[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)


test_sequence = [10, 22, 9, 33, 21, 50, 41, 60]
lis_length = longest_increasing_subsequence(test_sequence)
print(f"\nProblem 4 - Sequence: {test_sequence}")
print(f"Longest increasing subsequence length: {lis_length}")


# Problem 5: Find the majority element
def find_majority_element(lst):
    if not lst:
        return None

    # Boyer-Moore voting algorithm
    candidate = lst[0]
    count = 1

    for num in lst[1:]:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Verify if it's actually majority
    if lst.count(candidate) > len(lst) // 2:
        return candidate
    return None


majority_test = [2, 2, 1, 1, 1, 2, 2]
majority_element = find_majority_element(majority_test)
print(f"\nProblem 5 - List: {majority_test}")
print(f"Majority element: {majority_element}")

print("\n=== END ===")
